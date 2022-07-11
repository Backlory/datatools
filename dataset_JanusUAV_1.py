import os
import numpy as np
import cv2
import torch
import copy
import time
import random
from torchvision.transforms import functional as T_F
import torch.nn.functional as F 

from _base_dataset_generater import _Dataset_Generater_Base
from _tools import janus_uav_tools as tools

class Dataset_JanusUAV(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={'ifDataAugment':True, 'img_size_h':640, 'img_size_w':640}) -> None:
        print('initializating Dataset_JanusUAV...')
        super().__init__(dataset_path, args)
        random.seed(int( time.time()*1000000))
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
            if self.args['ifDatasetAllTheSameTrick']: 
                index = 0
        except:
            pass
        paths, _, path_gt = self.data_list[index]
        img = cv2.imread(paths, cv2.IMREAD_COLOR)
        
        target = cv2.imread(path_gt, cv2.IMREAD_GRAYSCALE)
        ret, target = cv2.threshold(target, 127, 255, cv2.THRESH_BINARY_INV)
        target = cv2.merge([target, 255 - target])

        if self.args['ifDataAugment']:
            img, target = self.transform(img, target)

        img = torch.tensor(img/255).float().permute(2,0,1)    #hwc->chw
        _,h,w = img.shape
        img = img.view(3,-1)
        img_mean = img.mean(1)
        img_std = img.std(1)
        img[0] = (img[0] - img_mean[0]) / img_std[0]
        img[1] = (img[1] - img_mean[1]) / img_std[1]
        img[2] = (img[2] - img_mean[2]) / img_std[2]
        
        target = torch.tensor(target/255).float().permute(2,0,1)
        #
        img, target = self.preprocess(img, target)
        #
        return img, target

    def transform(self, img:np.array, target):
        if True:                        #随机裁剪至原始尺寸的70%~100%
            h, w, _ = img.shape
            th, tw = int(h*(np.random.rand()*0.3+0.7)), int(w*(np.random.rand()*0.3+0.7))
            x1 = np.random.randint(0, w - tw)
            y1 = np.random.randint(0, h - th)
            img= img[y1: y1 + th,x1: x1 + tw, :]
            target = target[y1: y1 + th,x1: x1 + tw]
        if np.random.rand() >0.5:    #高斯噪声
            gaussian_noise = np.zeros_like(img, dtype=np.float)
            gaussian_noise = (cv2.randn(gaussian_noise, (0,0,0), (1,1,1))/ 5 * (random.random()*10 + 5)).astype(np.int)
            img = img + gaussian_noise
            img = np.clip(img, 0, 255)
            img = img.astype(np.uint8)
        if np.random.rand() >0.5:    #水平翻转
            img = cv2.flip(img, 1)
            target = cv2.flip(target, 1)
        if np.random.rand() >0.5:    #垂直翻转
            img = cv2.flip(img, 0)
            target = cv2.flip(target, 0)
        if np.random.rand() >0.5:    #旋转
            temp_r = np.random.randint(-30, 30)
            (h,w)=img.shape[:2]
            center=(w//2,h//2)
            M = cv2.getRotationMatrix2D(center,temp_r, 1.0)
            img = cv2.warpAffine(img, M, (w, h))
            target = cv2.warpAffine(target, M, (w, h))
        img = cv2.resize(img, (640, 640))
        target = cv2.resize(target, (640, 640))
        return img, target

    def preprocess(self, img, target):
        return img, target

if __name__=="__main__":
    from mypath import Path

    Dataset_generater = Dataset_JanusUAV(Path.db_root_dir('janus_uav'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    img_t0_t4, gt_t0_t4 = Dataset_train[0]
    print(img_t0_t4.shape)
    print(gt_t0_t4.shape)
    
    from torch.utils.data import DataLoader
    dataloader = DataLoader(Dataset_train, 8)
    for i, item in enumerate(dataloader):
        img, target = item

        print(img.shape)
        img = (img[0] * 255).numpy().transpose(1,2,0).astype(np.uint8)
        cv2.imwrite(f"{i}.png", img)

        target = (target[0] * 255).numpy().transpose(1,2,0).astype(np.uint8)
        cv2.imwrite(f"gt_{i}.png", target)