
from importlib.metadata import metadata
import os, sys

def getall_data_train(datasetpath:str):
    temppath = os.path.join(datasetpath, "training", 'images')
    data, metadata = [], []
    templist = sorted(os.listdir(temppath))
    for filename in templist:
        if filename[:2] == 'sf':continue    #跳帧的不要
        data.append(os.path.join(temppath, filename))
        metadata.append(filename[0:21])
    return data, metadata

def getall_label_train(datasetpath:str):
    temppath = os.path.join(datasetpath, "training", 'images')
    data, metadata = [], []
    templist = sorted(os.listdir(temppath))
    for filename in templist:
        if filename[:2] == 'sf':continue    #跳帧的不要
        temp = os.path.join(datasetpath, "training", 'boxes', filename[0:-3]+"txt")
        allbbox = []
        with open(temp, 'r') as f:
            line = f.readline().split(" ")
            allbbox.append(line)
        data.append(allbbox)
        metadata.append(filename[0:21])
    return data, metadata

def getall_data_valid(datasetpath:str):
    raise ValueError("there is no valid set!")

def getall_label_valid(datasetpath:str):
    raise ValueError("there is no valid set!")

def getall_data_test(datasetpath:str):
    temppath = os.path.join(datasetpath, "testing", 'images')
    data, metadata = [], []
    templist = sorted(os.listdir(temppath))
    for filename in templist:
        if filename[:2] == 'sf':continue    #跳帧的不要
        data.append(os.path.join(temppath, filename))
        metadata.append(filename[0:21])
    return data, metadata

def getall_label_test(datasetpath:str):
    temppath = os.path.join(datasetpath, "testing", 'images')
    data, metadata = [], []
    templist = sorted(os.listdir(temppath))
    for filename in templist:
        if filename[:2] == 'sf':continue    #跳帧的不要
        temp = os.path.join(datasetpath, "testing", 'boxes', filename[0:-3]+"txt")
        allbbox = []
        with open(temp, 'r') as f:
            line = f.readline()[:-1].split(" ")
            while line!=['']:
                allbbox.append(line)
                line = f.readline()[:-1].split(" ")
        data.append(allbbox)
        metadata.append(filename[0:21])
    return data, metadata

if __name__ == "__main__":
    from _mypath import Path
    mypath = Path.db_root_dir('kitti_mod')
    
    try:
        train_data, train_metadata = getall_data_train(mypath)
        train_label, train_metalabel = getall_label_train(mypath)
        print('len=', len(train_data),', ', train_data[0])
        print('len=', len(train_label),', ', train_label[0])
    except ValueError:
        pass
    
    try:
        valid_data, valid_metadata = getall_data_valid(mypath)
        valid_label, valid_metalabel = getall_label_valid(mypath)
        print('len=', len(valid_data),', ', valid_data[0])
        print('len=', len(valid_label),', ', valid_label[0])
    except ValueError:
        pass

    try:
        test_data, test_metadata = getall_data_test(mypath)
        test_label, test_metalabel = getall_label_test(mypath)
        print('len=', len(test_data),', ', test_data[0])
        print('len=', len(test_label),', ', test_label[0])
    except ValueError:
        pass
