import os, sys
from pycocotools.coco import COCO

def getall_data_train(datasetpath:str):
    ds = COCO(os.path.join(datasetpath, 'annotations','instances_train2017.json'))
    data, metadata = [], []
    for i in range(len(ds.dataset['images'])):
        data.append(
            os.path.join(
                datasetpath, 'images', 'train2017', ds.dataset['images'][i]['file_name']
                )
            )
        metadata.append(ds.dataset['images'][i]['id'])
    return data, metadata

def getall_label_train(datasetpath:str):
    raise ValueError("!")
    #ds = COCO(os.path.join(mypath, 'annotations','instances_train2017.json'))
    data, metadata = [], []
    #for i in range(len(ds.dataset['images'])):
    #    data.append(
    #        ds.getAnnIds(imgIds=[ds.dataset['images'][i]['id']])
    #        )
    #    metadata.append(        ds.dataset['images'][i]['id'])
    return data, metadata

def getall_data_valid(datasetpath:str):
    ds = COCO(os.path.join(datasetpath, 'annotations','instances_val2017.json'))
    data, metadata = [], []
    for i in range(len(ds.dataset['images'])):
        data.append(
            os.path.join(
                datasetpath, 'images', 'val2017', ds.dataset['images'][i]['file_name']
                )
            )
        metadata.append(ds.dataset['images'][i]['id'])
    return data, metadata

def getall_label_valid(datasetpath:str):
    raise ValueError("!")
    data, metadata = [], []
    return data, metadata

def getall_data_test(datasetpath:str):
    raise ValueError("!")
    data, metadata = [], []
    return data, metadata

def getall_label_test(datasetpath:str):
    raise ValueError("!")
    data, metadata = [], []
    return data, metadata

if __name__ == "__main__":
    from _mypath import Path
    mypath = Path.db_root_dir('coco')

    try:
        train_data, train_metadata = getall_data_train(mypath)
        print('len=', len(train_data),', ', train_data[0])
        train_label, train_metalabel = getall_label_train(mypath)
        print('len=', len(train_label),', ', train_label[0])
    except ValueError:
        pass
    
    try:
        valid_data, valid_metadata = getall_data_valid(mypath)
        print('len=', len(valid_data),', ', valid_data[0])
        valid_label, valid_metalabel = getall_label_valid(mypath)
        print('len=', len(valid_label),', ', valid_label[0])
    except ValueError:
        pass

    try:
        test_data, test_metadata = getall_data_test(mypath)
        print('len=', len(test_data),', ', test_data[0])
        test_label, test_metalabel = getall_label_test(mypath)
        print('len=', len(test_label),', ', test_label[0])
    except ValueError:
        pass