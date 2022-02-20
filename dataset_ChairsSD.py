import os
from _base_dataset_generater import _Dataset_Generater_Base
import data.dataset.datatools._tools.chairsd_tools as tools

class Dataset_ChairsSDHomio(_Dataset_Generater_Base):
    def __init__(self, dataset_path=[],args=None) -> None:
        print('initializating Dataset_ChairsSDHomio...')
        super().__init__(dataset_path, args)
        #
    def get_alldata_from_dataset_path(self, dataset_path):
        path_tri, path_val, path_test = dataset_path
        temp = os.listdir(path_val + '/t0')
        temp1 = int(len(temp) * 0.7)
        data_list_tri = temp[:temp1]
        data_list_val = temp[temp1:]
        data_list_test = os.listdir(path_test + '/t0')  #只读取t0即可，其他的好改
        #
        data_list_tri = [path_tri + "/t0/" + dirname[:-4] for dirname in data_list_tri]
        data_list_val = [path_val + "/t0/" + dirname[:-4] for dirname in data_list_val]
        data_list_test = [path_test + "/t0/" + dirname[:-4] for dirname in data_list_test]
        #
        return data_list_tri, data_list_val, data_list_test

