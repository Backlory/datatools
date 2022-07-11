import os
import numpy as np
import cv2
import torch
import copy
import time
import random
from torchvision.transforms import functional as T_F

from _base_dataset_generater import _Dataset_Generater_Base
from _tools import janus_uav_tools as tools

class Dataset_JanusUAV(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={'ifDataAugment':True, 'img_size_h':640, 'img_size_w':640}) -> None:
        print('initializating Dataset_JanusUAV...')
        super().__init__(dataset_path, args)
        #
    
    def get_alldata_from_dataset_path(self):
        #
        iQ =imageQuantity = 4
        #
        data, data_piece = tools.getall_data_train(self.dataset_path)
        label, _ = tools.getall_label_train(self.dataset_path)
        data =list( zip(data[0:-4], data[1:-3], data[2:-2], data[3:-1], data[4:]) )
        data_piece = list( zip(data_piece[0:-4], data_piece[4:]) )
        label =list( zip(label[0:-4], label[1:-3], label[2:-2], label[3:-1], label[4:]) )
        tri = list(zip(data, data_piece, label ))

        data, data_piece = tools.getall_data_valid(self.dataset_path)
        label, _ = tools.getall_label_valid(self.dataset_path)
        data =list( zip(data[0:-4], data[1:-3], data[2:-2], data[3:-1], data[4:]) )
        data_piece = list( zip(data_piece[0:-4], data_piece[4:]) )
        label =list( zip(label[0:-4], label[1:-3], label[2:-2], label[3:-1], label[4:]) )
        tes = list(zip(data, data_piece, label ))
        
        split_ = int(len(tri) * 0.7)
        data_list_tri = tri[:split_]
        data_list_val = tri[split_:]
        data_list_test = tes
        #
        return data_list_tri, data_list_val, data_list_test
        
    def __getitem__(self, index):
        try:
            if self.args['ifDatasetAllTheSameTrick']: 
                index = 0
        except:
            pass
        
        paths, video_pieces, path_gt = self.data_list[index]
        while video_pieces[0] != video_pieces[1]:
            if index>10:
                index -= 1
            else:
                index = 20
            paths, video_pieces, path_gt = self.data_list[index]
        
        img_t0_t4 = []
        for i in range(0, len(paths)):
            temp = cv2.imread(paths[i], cv2.IMREAD_COLOR)
            temp = torch.tensor(temp/255).float().permute(2,0,1)    #hwc->chw
            img_t0_t4.append(temp)
        gt_t0_t4 = []
        for i in range(0, len(path_gt)):
            temp = cv2.imread(path_gt[i], cv2.IMREAD_GRAYSCALE)
            ret, temp = cv2.threshold(temp, 127, 255, cv2.THRESH_BINARY_INV)
            temp = torch.tensor(temp[None]/255).float()
            gt_t0_t4.append(temp)
        #
        if self.args['ifDataAugment']:
            img_t0_t4, gt_t0_t4 = self.transform(img_t0_t4, gt_t0_t4)
        #
        H_ = self.args['img_size_h']
        W_ = self.args['img_size_w']
        for i in range(len(img_t0_t4)):
            img_t0_t4[i] = torch.nn.functional.interpolate( input=img_t0_t4[i][None], size=(H_, W_), 
                                                        mode='bilinear',    align_corners=False)[0]
            gt_t0_t4[i] = torch.nn.functional.interpolate(input=gt_t0_t4[i][None], size=(H_, W_), 
                                                        mode='bilinear',align_corners=False)[0]
        #
        # img preprocess
        img_t0_t4, gt_t0_t4 = self.preprocess(img_t0_t4, gt_t0_t4)
        #
        return img_t0_t4, gt_t0_t4

    def transform(self, img_list, target_list):
        random.seed(int( time.time()*1000000))
        if True:                        #随机裁剪至原始尺寸的70%~100%
            _, h, w = img_list[0].shape
            th, tw = int(h*(random.random()*0.3+0.7)), int(w*(random.random()*0.3+0.7))
            x1 = random.randint(0, w - tw)
            y1 = random.randint(0, h - th)
            for i in range(len(img_list)):
                img_list[i] = img_list[i][:, y1: y1 + th,x1: x1 + tw]
            for i in range(len(target_list)):
                target_list[i] = target_list[i][:, y1: y1 + th,x1: x1 + tw]
        if random.random() >0.95:    #恒等
            for i in range(len(target_list)):
                target_list[i] = torch.zeros_like(target_list[0]).float()  #无运动
            for i in range(len(img_list)):
                img_list[i] = copy.deepcopy(img_list[0])
        if random.random() >0.5:    #高斯噪声
            for i in range(len(img_list)):
                temp = img_list[i]
                temp_k = torch.rand(1)*90 + 20
                temp = temp + torch.randn(temp.size())/temp_k
                temp = torch.clip(temp, 0, 1)
                img_list[i] = temp
        if random.random() >0.5:    #水平翻转
            for i in range(len(img_list)):
                temp = img_list[i]
                temp = T_F.hflip(temp)
                img_list[i] = temp
            for i in range(len(target_list)):
                temp = target_list[i]
                temp = T_F.hflip(temp)
                target_list[i] = temp
        if random.random() >0.5:    #垂直翻转
            for i in range(len(target_list)):
                temp = target_list[i]
                temp = T_F.vflip(temp)
                target_list[i] = temp
            for i in range(len(img_list)):
                temp = img_list[i]
                temp = T_F.vflip(temp)
                img_list[i] = temp
        if random.random() >0.5:    #旋转
            temp_r = random.randrange(-30, 30)
            for i in range(len(img_list)):
                temp = img_list[i]
                temp = T_F.rotate(temp, temp_r)
                img_list[i] = temp
            for i in range(len(target_list)):
                temp = target_list[i]
                temp = T_F.rotate(temp, temp_r)
                target_list[i] = temp
        if random.random() >0.5:    #倒序播放
            img_list_inv = []
            target_list_inv = []
            lens = len(img_list)
            for i in range(lens):
                img_list_inv.append(img_list[lens-i-1])
                target_list_inv.append(target_list[lens-i-1])
            img_list = img_list_inv
            target_list = target_list_inv
        return img_list, target_list

    def preprocess(self, img_t0_t4, gt_t0_t4):
        return img_t0_t4, gt_t0_t4

if __name__=="__main__":
    from mypath import Path
    Dataset_generater = Dataset_JanusUAV(Path.db_root_dir('janus_uav'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    img_t0_t4, gt_t0_t4 = Dataset_train[0]
    print(len(img_t0_t4))
    print(len(gt_t0_t4))
    print(img_t0_t4[0].shape)
    print(gt_t0_t4[0].shape)
    for img in img_t0_t4:
        img = img.cpu().numpy()[0]
        #cv2.imwrite("1.png", img)
    
    from torch.utils.data import DataLoader
    dataloader = DataLoader(Dataset_train, 8)
    for i, item in enumerate(dataloader):
        imgs, gts = item
        for i, img in enumerate(imgs):
            temp = (img[0] * 255).numpy().transpose(1,2,0).astype(np.uint8)
            print(img.shape)
            cv2.imwrite(f"{i}.png", temp)
        for i, gt in enumerate(gts):
            print(gt.shape)
            temp = (gt[0] * 255).numpy().transpose(1,2,0).astype(np.uint8)
            cv2.imwrite(f"gt_{i}.png", temp)
        #print(imgs[0])