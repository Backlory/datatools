import os
from _base_dataset_generater import _Dataset_Generater_Base
from _tools import chairsd_tools as tools

import cv2
from _Chairsio import readFlow
class Dataset_ChairsSDHomio(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={}) -> None:
        print('initializating Dataset_ChairsSDHomio...')
        super().__init__(dataset_path, args)
        #
    def get_alldata_from_dataset_path(self):
        data, data_piece = tools.getall_data_train(self.dataset_path)
        label, _ = tools.getall_label_train(self.dataset_path)
        data_all = list(zip(data, data_piece, label ))
        #
        data_len = len(data)
        temp1 = int(data_len * 0.7)
        data_list_tri = data_all[:temp1]
        data_list_val = data_all[temp1:]
        
        data, data_piece = tools.getall_data_test(self.dataset_path)
        label, _ = tools.getall_label_test(self.dataset_path)
        data_list_test = list(zip(data, data_piece, label ))


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
    Dataset_generater = Dataset_ChairsSDHomio(Path.db_root_dir('chairsd'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    Dataset_train[0]

    