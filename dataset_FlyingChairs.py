import os
from data.dataset.datatools._base_dataset_generater import _Dataset_Generater_Base

class Dataset_FlyingChairs(_Dataset_Generater_Base):
    def __init__(self, dataset_path='data/FlyingChaire_release/data',args=None) -> None:
        print('initializating Dataset_FlyingChairs...')
        super().__init__(dataset_path, args)
        #
    
    def get_alldata_from_dataset_path(self, dataset_path):
        path_tri, path_val, path_test = dataset_path
        #
        temp = [str(1+i).zfill(5) for i in range(22872)]
        temp1 = int(len(temp) * 0.7)
        temp2 = int(len(temp) * 0.9)
        data_list_tri = temp[:temp1]
        data_list_val = temp[temp1:temp2]
        data_list_test = temp[temp2:]
        #
        data_list_tri = [path_tri + "/" + dirname for dirname in data_list_tri]
        data_list_val = [path_val + "/" + dirname for dirname in data_list_val]
        data_list_test = [path_test + "/" + dirname for dirname in data_list_test]
        #
        return data_list_tri, data_list_val, data_list_test
