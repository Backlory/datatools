import os, sys
import numpy as np
import cv2
import torch
import copy
import time
import random
from torchvision.transforms import functional as T_F
import torch.nn.functional as F 

#from utils.flow_viz import flow_to_image
        
from _base_dataset_generater import _Dataset_Generater_Base

def getall_data_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "Train")
    data, metadata = [], []
    for videoname in os.listdir(path_tri):  # video: 'video_1'
        frames = sorted(os.listdir(os.path.join(path_tri, videoname, "flow_ten")))
        for idx in range(len(frames)):
            temp1 = os.path.join(path_tri, videoname, 'flow_ten', frames[idx])
            temp2 = os.path.join(path_tri, videoname, 'fea_ten', frames[idx])
            temp3 = os.path.join(path_tri, videoname, 'flow', frames[idx])
            data.append([temp1, temp2, temp3])
            metadata.append(videoname)
    return data, metadata

def getall_label_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "Train")
    data, metadata = [], []
    for videoname in os.listdir(path_tri):  # video: 'video_1'
        frames = sorted(os.listdir(os.path.join(path_tri, videoname, "flow_ten")))
        for idx in range(len(frames)):
            temp = os.path.join(path_tri, videoname, 'gt_mov', frames[idx][0:3]+".png")
            data.append(temp)
            metadata.append(videoname)
    return data, metadata


class Dataset_JanusFLOW(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={'ifDataAugment':True, 'img_size_h':640, 'img_size_w':640}) -> None:
        print('initializating Dataset_JanusUAV...')
        super().__init__(dataset_path, args)
        random.seed(int( time.time()*1000000))
        #
    
    def get_alldata_from_dataset_path(self):
        #
        data, data_piece = getall_data_train(self.dataset_path)
        label, _ = getall_label_train(self.dataset_path)
        tri = list(zip(data, data_piece, label ))

        split_ = int(len(tri) * 0.7)
        data_list_tri = tri[:split_]
        data_list_val = tri[split_:]
        data_list_test = []
        #
        return data_list_tri, data_list_val, data_list_test
        
    def __getitem__(self, index):
        try:
            if self.args['ifDatasetAllTheSameTrick']: 
                index = 0
        except:
            pass
        paths, _, path_gt = self.data_list[index]
        path_flow_ten, path_fea, path_flow = paths

        flow_ten = torch.load(path_flow_ten)[0].float()
        fea_ten = torch.load(path_fea)[0].float()
        inputs = [flow_ten, fea_ten]

        target = cv2.imread(path_gt, cv2.IMREAD_GRAYSCALE)
        ret, target = cv2.threshold(target, 127, 255, cv2.THRESH_BINARY_INV)
        target = cv2.merge([target, 255 - target])

        #flo = flow_to_image(flow_ten.permute(1,2,0).cpu().numpy())
        #cv2.imwrite("1.png", flo)
        #cv2.imwrite("1.png", target[:,:,0])

        target = torch.tensor(target/255).float().permute(2,0,1)
        #
        inputs, target = self.preprocess(inputs, target)
        #
        return inputs, target

    def preprocess(self, img, target):
        return img, target

if __name__=="__main__":
    from mypath import Path

    Dataset_generater = Dataset_JanusFLOW(Path.db_root_dir('janus_uav'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    
    from torch.utils.data import DataLoader
    dataloader = DataLoader(Dataset_train, 8)
    for i, item in enumerate(dataloader):
        inputs, target = item
        flow_ten, fea_ten = inputs

        print(flow_ten.shape)
        print(fea_ten.shape)
        
        target = (target[0] * 255).numpy().transpose(1,2,0).astype(np.uint8)
        cv2.imwrite(f"1.png", target[:,:,0])