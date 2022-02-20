import xml.etree.ElementTree as ET
from importlib.metadata import metadata
import os, sys


def xml_reader(filename):
    """ Parse a PASCAL VOC xml file """
    tree = ET.parse(filename)
    objects = []
    for obj in tree.findall('object'):
        obj_struct = {}
        obj_struct['name'] = obj.find('name').text
        bbox = obj.find('bndbox')
        obj_struct['bbox'] = [int(float(bbox.find('xmin').text)),
                              int(float(bbox.find('ymin').text)),
                              int(float(bbox.find('xmax').text)),
                              int(float(bbox.find('ymax').text))]   
        objects.append(obj_struct)
    return objects



def getall_data_train(datasetpath:str):
    temppath = os.path.join(datasetpath, "dataset")
    data, metadata = [], []
    for setname in os.listdir(temppath):
        path_img = os.path.join(temppath, setname, 'images')
        for i in range(len(os.listdir(path_img))):
            data.append(os.path.join(path_img,'frame' + str(i+1).zfill(4) + '.jpg'))
            metadata.append(setname)
    return data, metadata

def getall_label_train(datasetpath:str):
    temppath = os.path.join(datasetpath, "dataset")
    data, metadata = [], []
    for setname in os.listdir(temppath):
        path_img = os.path.join(temppath, setname, 'annotations')
        for i in range(len(os.listdir(path_img))):
            xmlpath = os.path.join(path_img,'frame' + str(i+1).zfill(4) + '.xml')
            temp = xml_reader(xmlpath)
            data.append(temp)   #xmin, ymin, xmax, ymax
            metadata.append(setname)
    return data, metadata

def getall_data_valid(datasetpath:str):
    raise ValueError("there is no valid set!")

def getall_label_valid(datasetpath:str):
    raise ValueError("there is no valid set!")

def getall_data_test(datasetpath:str):
    raise ValueError("there is no test set!")

def getall_label_test(datasetpath:str):
    raise ValueError("there is no test set!")

if __name__ == "__main__":
    from _mypath import Path
    mypath = Path.db_root_dir('PESMOD')
    
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