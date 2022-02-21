import os
from _base_dataset_generater import _Dataset_Generater_Base
from _tools import cdnet2014_tools as tools

class Dataset_CDNet2014(_Dataset_Generater_Base):
    def __init__(self, dataset_path='',args={}) -> None:
        print('initializating Dataset_CDNet2014...')
        super().__init__(dataset_path, args)
        #
    
    def get_alldata_from_dataset_path(self, dataset_path):
        #
        data, data_piece = tools.getall_data_train(self.path)
        label, _ = tools.getall_label_train(self.path)
        tri = list(zip(data, data_piece, label ))
        #
        data, data_piece = tools.getall_data_valid(self.path)
        label, _ = tools.getall_label_valid(self.path)
        val = list(zip(data, data_piece, label ))

        data, data_piece = tools.getall_data_test(self.path)
        label, _ = tools.getall_label_test(self.path)
        tes = list(zip(data, data_piece, label ))
        
        data_list_tri = tri
        data_list_val = val
        data_list_test = tes
        #
        return data_list_tri, data_list_val, data_list_test
        
    def __getitem__(self, index):
        return super().__getitem__(index)
        

if __name__=="__main__":
    from mypath import Path
    Dataset_generater = Dataset_CDNet2014(Path.db_root_dir('cdnet2014'))
    Dataset_train = Dataset_generater.generate('train')
    Dataset_valid = Dataset_generater.generate('valid')
    Dataset_test = Dataset_generater.generate('test')
    Dataset_train[0]