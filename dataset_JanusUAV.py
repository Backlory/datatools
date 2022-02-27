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
    def __init__(self, dataset_path='',args={'dataaugment':True, 'img_size_h':640, 'img_size_w':640}) -> None:
        print('initializating Dataset_JanusUAV...')
        super().__init__(dataset_path, args)
        #
    
    def get_alldata_from_dataset_path(self):
        #
        data, data_piece = tools.getall_data_train(self.dataset_path)
        label, _ = tools.getall_label_train(self.dataset_path)
        tri = list(zip(data, data_piece, label ))

        data, data_piece = tools.getall_data_valid(self.dataset_path)
        label, _ = tools.getall_label_valid(self.dataset_path)
        tes = list(zip(data, data_piece, label ))
        
        split_ = int(len(tri) * 0.7)
        data_list_tri = tri[:split_]
        data_list_val = tri[split_:]
        data_list_test = tes
        #
        return data_list_tri, data_list_val, data_list_test
        
    def __getitem__(self, index):
        try:
            if self.args['trick_dataset_allissame']: 
                index = 0
        except:
            pass
        if index > len(self.data_list) - 2:
            index = len(self.datalist) - 2
        if self.data_list[index][1] != self.data_list[index+1][1]:
            index += 1
        path_img_t0 = self.data_list[index][0]
        path_img_t1 = self.data_list[index+1][0]
        path_gt = self.data_list[index][2]
        img_t0 = cv2.imread(path_img_t0, cv2.IMREAD_COLOR)
        img_t1 = cv2.imread(path_img_t1, cv2.IMREAD_COLOR)
        gt = cv2.imread(path_gt, cv2.IMREAD_GRAYSCALE)[None]
        target = np.where(gt>129+3, 255, 0).astype(np.uint8)
        target = np.where(gt<129-3, 255, target).astype(np.uint8)
        #
        img_t0 = torch.tensor(img_t0/255).float().permute(2,0,1)    #hwc->chw
        img_t1 = torch.tensor(img_t1/255).float().permute(2,0,1)
        target = torch.tensor(target/255).float()
        print(img_t0.shape)
        print(img_t1.shape)
        print(target.shape)
        print(target.max())
        if self.args['dataaugment']:
            img_t0, img_t1, target = self.transform(img_t0, img_t1, target)
        #
        H_ = self.args['img_size_h']
        W_ = self.args['img_size_w']
        img_t0 = torch.nn.functional.interpolate(   input=img_t0[None], size=(H_, W_), 
                                                    mode='bilinear',    align_corners=False)
        img_t1 = torch.nn.functional.interpolate(   input=img_t1[None], size=(H_, W_), 
                                                    mode='bilinear',    align_corners=False)
        target = torch.nn.functional.interpolate(input=target[None], size=(H_, W_), 
                                                        mode='bilinear',align_corners=False)
        img_t0, img_t1, target = img_t0[0], img_t1[0], target[0]
        #
        return img_t0, img_t1, target

    def transform(self, img_t0, img_t1, target):
        random.seed(int( time.time()*1000000))
        if True:                        #随机裁剪至原始尺寸的70%~100%
            _, h, w = img_t0.shape
            th, tw = int(h*(random.random()*0.3+0.7)), int(w*(random.random()*0.3+0.7))
            x1 = random.randint(0, w - tw)
            y1 = random.randint(0, h - th)
            img_t0  =  img_t0[:, y1: y1 + th,x1: x1 + tw]
            img_t1  =  img_t1[:, y1: y1 + th,x1: x1 + tw]
            target =   target[:, y1: y1 + th,x1: x1 + tw]
        if random.random() >0.8:    #恒等
            img_t1 = copy.deepcopy(img_t0)
            target = torch.zeros_like(target).float()  #无运动
        if random.random() >0.5:    #高斯噪声
            temp = torch.rand(1)*90 + 10
            img_t0 = img_t0 + torch.randn(img_t0.size())/temp
            img_t1 = img_t1 + torch.randn(img_t0.size())/temp
            img_t0 = torch.clip(img_t0, 0, 1)
            img_t1 = torch.clip(img_t1, 0, 1)
        if random.random() >0.5:    #水平翻转
            img_t0 = T_F.hflip(img_t0)
            img_t1 = T_F.hflip(img_t1)
            target = T_F.hflip(target)
        if random.random() >0.5:    #垂直翻转
            img_t0 = T_F.vflip(img_t0)
            img_t1 = T_F.vflip(img_t1)
            target = T_F.vflip(target)
        if random.random() >0.5:    #旋转
            temp = random.randrange(-30, 30)
            img_t0 = T_F.rotate(img_t0, temp)
            img_t1 = T_F.rotate(img_t1, temp)
            target = T_F.rotate(target, temp)
        return img_t0, img_t1, target

if __name__=="__main__":
    from mypath import Path
    Dataset_generater = Dataset_JanusUAV(Path.db_root_dir('janus_uav'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    img_t0, img_t1, gt = Dataset_train[0]
    print(img_t0.shape)
    print(img_t1.shape)
    print(gt.shape)