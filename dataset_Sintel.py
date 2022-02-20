import os
from data.dataset.datatools._base_dataset_generater import _Dataset_Generater_Base

class Dataset_Sintel(_Dataset_Generater_Base):
    def __init__(self, dataset_path=['data/ChairsSDHom/data/train','data/ChairsSDHom/data/test'],args=None) -> None:
        print('initializating Dataset_Sintel...')
        super().__init__(dataset_path, args)
        
    def get_alldata_from_dataset_path(self, dataset_path):
        path_tri, path_val, path_test = dataset_path
        temp = []
        for video in os.listdir(path_tri):  # video: 'alley_1'
            frames = sorted(os.listdir(path_tri + '/' + video))
            for idx in range(len(frames)-1):
                img_1_2 = (f'{video}/{frames[idx]}', f'{video}/{frames[idx+1]}')
                temp.append(img_1_2) #
        temp1 = int(len(temp) * 0.8)
        data_list_tri = temp[:temp1]
        data_list_val = temp[temp1:]
        data_list_test = []
        for video in os.listdir(path_test):  # video: 'alley_1'
            frames = sorted(os.listdir(path_test + '/' + video))
            for idx in range(len(frames)-1):
                img_1_2 = (f'{video}/{frames[idx]}', f'{video}/{frames[idx+1]}')
                data_list_test.append(img_1_2) #
        #
        data_list_tri = [(path_tri + "/" + dirname[0], path_tri + "/" + dirname[1]) for dirname in data_list_tri]
        data_list_val = [(path_val + "/" + dirname[0], path_val + "/" + dirname[1]) for dirname in data_list_val]
        data_list_test = [(path_test + "/" + dirname[0], path_test + "/" + dirname[1]) for dirname in data_list_test]
        return data_list_tri, data_list_val, data_list_test
    
    def load_flow(path):
        import numpy as np
        with open(path, 'rb') as f:
            magic = np.fromfile(f, np.float32, count=1)
            assert (202021.25 == magic), 'Magic number incorrect. Invalid .flo file'
            h = np.fromfile(f, np.int32, count=1)[0]
            w = np.fromfile(f, np.int32, count=1)[0]
            data = np.fromfile(f, np.float32, count=2 * w * h)
        data2D = np.resize(data, (w, h, 2))
        return data2D