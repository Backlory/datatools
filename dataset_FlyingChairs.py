import os
import cv2
import random
import torch
import numpy as np
import copy
import torchvision.transforms.functional as T_F
import time
from _base_dataset_generater import _Dataset_Generater_Base
from _tools import flyingchairs_tools as tools

from _Chairsio import readFlow

class Dataset_FlyingChairs(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={'dataaugment':True, 'img_size_h':640, 'img_size_w':640}) -> None:
        print('initializating Dataset_FlyingChairs...')
        super().__init__(dataset_path, args)
        #
    
    def get_alldata_from_dataset_path(self):
        
        data, data_piece = tools.getall_data_train(self.dataset_path)
        label, _ = tools.getall_label_train(self.dataset_path)
        data_all = list(zip(data, data_piece, label ))
        #
        data_len = len(data)
        temp1 = int(data_len * 0.7)
        temp2 = int(data_len * 0.9)
        data_list_tri = data_all[:temp1]
        data_list_val = data_all[temp1:temp2]
        data_list_test = data_all[temp2:]
        return data_list_tri, data_list_val, data_list_test

    def __getitem__(self, index):
        try:
            if self.args['trick_dataset_allissame']: 
                index = 0
        except:
            pass
        paths, _, path_gt = self.data_list[index]
        path_img_t0, path_img_t1 = paths
        img_t0 = cv2.imread(path_img_t0, cv2.IMREAD_COLOR)
        img_t1 = cv2.imread(path_img_t1, cv2.IMREAD_COLOR)
        target = readFlow(path_gt)
        #
        img_t0 = torch.tensor(img_t0/255).float().permute(2,0,1)    #hwc->chw
        img_t1 = torch.tensor(img_t1/255).float().permute(2,0,1)
        target = torch.tensor(target).float().permute(2,0,1)
        if self.args['dataaugment']:
            img_t0, img_t1, target = self.transform(img_t0, img_t1, target)
        #
        H_ = self.args['img_size_h']
        W_ = self.args['img_size_w']
        _,H,W = target.shape
        img_t0 = torch.nn.functional.interpolate(   input=img_t0[None], size=(H_, W_), 
                                                    mode='bilinear',    align_corners=False)
        img_t1 = torch.nn.functional.interpolate(   input=img_t1[None], size=(H_, W_), 
                                                    mode='bilinear',    align_corners=False)
        target = torch.nn.functional.interpolate(input=target[None], size=(H_, W_), 
                                                        mode='bilinear',align_corners=False)
        target[:,0,:,:] = target[:,0,:,:] / (W/W_)
        target[:,1,:,:] = target[:,1,:,:] / (H/H_)
        #
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
            target = torch.zeros_like(target).float()  #无光流
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
            target[0,:,:] = -target[0,:,:]
        if random.random() >0.5:    #垂直翻转
            img_t0 = T_F.vflip(img_t0)
            img_t1 = T_F.vflip(img_t1)
            target = T_F.vflip(target)
            target[1,:,:] = -target[1,:,:]
        if random.random() >0.5:    #旋转
            temp = random.randrange(-30, 30)
            _, h,w = img_t0.shape
            img_t0 = T_F.rotate(img_t0, temp)
            img_t1 = T_F.rotate(img_t1, temp)
            target = T_F.rotate(target, temp)
            target_ = target.detach()
            target[0,:,:] =  np.cos(temp/180*3.14159)*target_[0,:,:] + np.sin(temp/180*3.14159)*target_[1,:,:]
            target[1,:,:] = -np.sin(temp/180*3.14159)*target_[0,:,:] + np.cos(temp/180*3.14159)*target_[1,:,:]
        return img_t0, img_t1, target

if __name__=="__main__":
    from mypath import Path
    Dataset_generater = Dataset_FlyingChairs(Path.db_root_dir('flyingchairs'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    img_t0, img_t1, gt = Dataset_train[0]
    print(img_t0.shape)
    print(img_t1.shape)
    print(gt.shape)

    import numpy as np
    cv2.imwrite('1.png', img_t0)
    cv2.imwrite('2.png', img_t1)
    cv2.imwrite('3.png',  (cv2.merge([ np.zeros_like(gt[:,:,1]), gt[:,:,0], gt[:,:,1] ]) + 100).astype(np.uint8))  #bgr是0wh 时，rgb是hw0 [0通道是w，1通道是h,右下为正]