import os
import cv2, random
import numpy as np
import time
import torch
import torch.nn.functional as F
from _base_dataset_generater import _Dataset_Generater_Base
from _tools import coco2017_tools as tools

class Dataset_COCO2017(_Dataset_Generater_Base):
    def __init__(self, 
                dataset_path=[],
                args = {'ifDataAugment':True,
                        'ifDatasetAllTheSameTrick':False}) -> None:
        print('initializating Dataset_COCO2017_warp...')
        super().__init__(dataset_path, args)

    def get_alldata_from_dataset_path(self):
        data, data_piece = tools.getall_data_train(self.dataset_path)
        tri = list(zip(data, data_piece ))

        split_ = int(len(tri) * 0.7)
        data_list_tri = tri[:split_]
        data_list_val = tri[split_:]
        data_list_test = []
        #
        return data_list_tri, data_list_val, data_list_test

    def __getitem__(self, index):
        if self.args['ifDatasetAllTheSameTrick']: 
            index = 0
            np.random.seed(5)
        #
        path_img, _ = self.data_list[index]
        img_t0 = cv2.imread(path_img, cv2.IMREAD_GRAYSCALE)[:,:,np.newaxis]
        #
        if self.args['ifDataAugment']:
            img_t0 = self.transform_pre(img_t0)
        #
        ps = 128
        target = np.random.randn(4, 2)
        #target = (np.random.rand(4, 2) * 0.5 - 0.25) * 4
        img_shape = (int(ps*1.5), int(ps*1.5))
        img_t0 = cv2.resize(img_t0, img_shape)
        fp = np.array([(0.25,0.25),(1.25,0.25),(1.25,1.25),(0.25,1.25)],
                        dtype=np.float32) * ps
        pfp = np.float32(fp + target * ps/4/4 )
        H_warp = cv2.getPerspectiveTransform(fp, pfp)
        img_t1 = cv2.warpPerspective(img_t0, H_warp, img_shape)
        #
        patch_t0 = img_t0[int(0.25*ps):int(1.25*ps), int(0.25*ps):int(1.25*ps)][:,:,np.newaxis]
        patch_t1 = img_t1[int(0.25*ps):int(1.25*ps), int(0.25*ps):int(1.25*ps)][:,:,np.newaxis]
        '''
        已知target，求直接能够在patch上(128*128)使用的仿射变换矩阵H_warp_patch：
        ps = 128
        fp = np.array([(0.25,0.25),(1.25,0.25),(1.25,1.25),(0.25,1.25)],
                        dtype=np.float32) * ps
        pfp = np.float32(fp + target /16 * ps)
        H_warp = cv2.getPerspectiveTransform(fp, pfp)
        H2 = np.array([1,0,-ps*0.25, 0,1, -ps*0.25,0,0,1]).reshape(3,3)
        H_warp_patch = np.matmul(np.matmul(H2, H_warp), np.linalg.inv(H2)) 
        patch_t0_w = cv2.warpPerspective(patch_t0, H_warp_patch, (ps, ps))
        '''
        '''
        cv2.imshow("img_t0", img_t0)
        cv2.imshow("img_t1", img_t1)
        cv2.imshow("patch_t0", patch_t0)
        cv2.imshow("patch_t1", patch_t1)
        cv2.imshow("patch_t0_w", patch_t0_w)
        cv2.waitKey(0)'''
        #
        patch_t0 = torch.tensor(patch_t0/255).float().permute(2,0,1)    #hwc->chw
        patch_t1 = torch.tensor(patch_t1/255).float().permute(2,0,1)
        target = torch.tensor(target).float()
        
        if self.args['ifDataAugment']:
            patch_t0, patch_t1 = self.transform_post(patch_t0, patch_t1)
        #
        patch_t0 = patch_t0 * 2 - 1
        patch_t1 = patch_t1 * 2 - 1
        
        return img_t0[np.newaxis, :,:], patch_t0, patch_t1, target

    def transform_pre(self, img_t0):
        random.seed(int( time.time()*1000000))
        if True:                        #随机裁剪至原始尺寸的70%~100%
            h, w, _ = img_t0.shape
            th, tw = int(h*(random.random()*0.3+0.7)), int(w*(random.random()*0.3+0.7))
            x1 = random.randint(0, w - tw)
            y1 = random.randint(0, h - th)
            img_t0 = img_t0[y1: y1 + th,x1: x1 + tw, :]
        if random.random() >0.5:    #水平翻转
            img_t0 = cv2.flip(img_t0, 1)
        if random.random() >0.5:    #垂直翻转
            img_t0 = cv2.flip(img_t0, 0)
        if random.random() >0.5:    #旋转
            temp = random.randrange(-30, 30)
            M = cv2.getRotationMatrix2D((64, 64), temp, 1/np.cos(temp/180))
            img_t0 = cv2.warpAffine(img_t0, M, (128, 128))
        return img_t0

    def transform_post(self, patch_t0, patch_t1):
        if random.random() >0.5:    #高斯噪声
            temp = torch.rand(1)*50 + 50
            patch_t0 = patch_t0 + torch.randn(patch_t0.size())/temp
            patch_t1 = patch_t1 + torch.randn(patch_t0.size())/temp
            patch_t0 = torch.clip(patch_t0, 0, 1)
            patch_t1 = torch.clip(patch_t1, 0, 1)
        if random.random() > 0.3:   #光照噪声
            temp1 = torch.randn(1)*0.01
            temp2 = torch.randn(1)*0.01
            patch_t0 = patch_t0 + temp1
            patch_t1 = patch_t1 + temp2
            patch_t0 = torch.clip(patch_t0, 0, 1)
            patch_t1 = torch.clip(patch_t1, 0, 1)
        return patch_t0, patch_t1

if __name__=="__main__":
    from mypath import Path
    Dataset_generater = Dataset_COCO2017(Path.db_root_dir('coco'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    print(Dataset_train[0])