import os
from data.dataset.datatools._base_dataset_generater import _Dataset_Generater_Base

class Dataset_COCO2017(_Dataset_Generater_Base):
    def __init__(self, dataset_path=['data/ChairsSDHom/data/train','data/ChairsSDHom/data/test'],args=None) -> None:
        print('initializating Dataset_COCO2017_warp...')
        super().__init__(dataset_path, args)

    def get_alldata_from_dataset_path(self, dataset_path):
        path_tri, path_val, path_test = dataset_path
        
        data_list_tri = os.listdir(path_tri)
        data_list_val = os.listdir(path_val)
        data_list_test = os.listdir(path_test)
        #
        data_list_tri = [path_tri + "/" + dirname for dirname in data_list_tri]
        data_list_val = [path_val + "/" + dirname for dirname in data_list_val]
        data_list_test = [path_test + "/" + dirname for dirname in data_list_test]
        #
        return data_list_tri, data_list_val, data_list_test