'''

Dataset_generater = Dataset_COCO2017_warp(dataset_path, args=self.args)

Dataset_train = Dataset_generater.generate('train')
Dataset_valid = Dataset_generater.generate('valid')
Dataset_test = Dataset_generater.generate('test')
'''
import numpy as np
import torch
from abc import abstractmethod
import os, sys, stat
import random
import copy
from torch.utils.data import Dataset
import time
try:
    from utils.mics import colorstr
except:
    colorstr = lambda x,y:x

class _Dataset_Generater_Base(Dataset):
    '''
    数据集生成器。
    '''
    def __init__(self, dataset_path=[],args={}) -> None:
        super(_Dataset_Generater_Base, self).__init__()
        self.dataset_path = dataset_path
        self.args = args
        # 获取数据
        self.data_tri, self.data_val, self.data_test = self.get_alldata_from_dataset_path()
        temp = len(self.data_tri) + len(self.data_val) + len(self.data_test)
        temp = f'Dataset has been load, {temp} raw data detected.\n' 
        temp += f'Trainset Volume:\t{len(self.data_tri)} data.\n' 
        temp += f'Validset Volume:\t{len(self.data_val)} data.\n' 
        temp += f'Testset  Volume:\t{len(self.data_test)} data.\n' 
        print(colorstr(temp,'yellow'))
        random.seed(int(time.time())*100000)    #打乱训练集、测试集、验证集内部的顺序
        random.shuffle(self.data_tri)
        random.shuffle(self.data_val)
        random.shuffle(self.data_test)
        self.data_list = []
    
    def get_alldata_from_dataset_path(self):
        '''
        从dataset_path中读取出 trainset validset testset。这里要做的：
        1、listdir形式，按顺序获取三数据集所有文件的路径
        2、该函数决定了哪些数据进入训练集，哪些数据进入测试集。不用在数据集内部打乱，但要考虑是否在外部打乱。
        3、最后返回的变量可能不是某一个特定文件，因为有的训练需要多个训练输入；但是要能够唯一标识【一组】训练数据。
        eg. data_tri=[(图片1，图片2，图片3)，标签，大类标签]
        '''
        data_tri, data_val, data_test = [], [], []
        return data_tri, data_val, data_test

    def _temp_list_clean(self):
        '''清空临时列表'''
        del self.data_tri
        del self.data_val
        del self.data_test

    def generate(self, state=''):
        '''根据state生成子数据集.
        state = 'train', 'valid', 'test'
        '''
        children = copy.deepcopy(self)
        if state == 'train':
            children.data_list = children.data_tri
        elif state == 'valid':
            children.data_list = children.data_val
            children.args['ifDataAugment'] = False
        elif state == 'test':
            children.data_list = children.data_test
            children.args['ifDataAugment'] = False
        children._temp_list_clean()
        temp = f'dataset_{state} has been generated with id={id(children)}.'
        print(colorstr(temp,'yellow'))
        return children
    #
    @abstractmethod
    def __getitem__(self, index):
        assert(self.data_list != [])

    #
    def __len__(self):
        if 'datasetLenTrick' not in self.args.keys():
            return len(self.data_list)
        else:
            if self.args['datasetLenTrick'] > 0:
                return self.args['datasetLenTrick']
            else:
                return len(self.data_list)
        
