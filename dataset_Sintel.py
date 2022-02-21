import os

import numpy as np
from _base_dataset_generater import _Dataset_Generater_Base
from _tools import sintel_tools as tools

import cv2
from _Chairsio import readFlow
class Dataset_Sintel(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={}) -> None:
        print('initializating Dataset_Sintel...')
        super().__init__(dataset_path, args)
        
    def get_alldata_from_dataset_path(self):

        data, data_piece = tools.getall_data_train(self.dataset_path)
        label, _ = tools.getall_label_train(self.dataset_path)
        data_all = []
        for idx in range(len(data)-1):
            if data_piece[idx] != data_piece[idx+1]:
                continue
            data_all.append(
                (
                    (data[idx], data[idx+1]),
                    data_piece[idx],
                    label[idx]
                )
            )
        #
        data_len = len(data_all)
        temp1 = int(data_len * 0.7)
        temp2 = int(data_len * 0.9)
        data_list_tri = data_all[:temp1]
        data_list_val = data_all[temp1:temp2]
        data_list_test = data_all[temp2:]

        return data_list_tri, data_list_val, data_list_test

    def __getitem__(self, index):
        paths, _, path_gt = self.data_list[index]
        path_img_t0, path_img_t1 = paths
        img_t0 = cv2.imread(path_img_t0, cv2.IMREAD_COLOR)
        img_t1 = cv2.imread(path_img_t1, cv2.IMREAD_COLOR)
        gt_optflo = readFlow(path_gt)
        return img_t0, img_t1, gt_optflo


if __name__=="__main__":
    from mypath import Path
    Dataset_generater = Dataset_Sintel(Path.db_root_dir('sintel'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    img_t0, img_t1, gt = Dataset_train[0]
    print(img_t0.shape)
    print(img_t1.shape)
    print(gt.shape)

    
    cv2.imwrite('1.png', img_t0)
    cv2.imwrite('2.png', img_t1)
    cv2.imwrite('3.png',  (cv2.merge([ np.zeros_like(gt[:,:,1]), gt[:,:,0], gt[:,:,1] ]) + 100).astype(np.uint8))  #bgr是0wh 时，rgb是hw0 [0通道是w，1通道是h,右下为正]
    print(gt)
    print(gt)
