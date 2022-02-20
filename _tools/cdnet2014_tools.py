import os, sys

def getall_data_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "dataset")
    data, metadata = [], []
    for cdname in os.listdir(path_tri):
        path_cdname = os.path.join(path_tri, cdname)
        for videoname in os.listdir(path_cdname):
            with open(os.path.join(path_cdname, videoname, 'temporalROI.txt'), 'r') as f:
                idx_begin, idx_end = f.readline().split(" ")
                for idx in range(1, int(idx_end)+1):
                    data.append(os.path.join(path_cdname, videoname, "input", 'in'+str(idx).zfill(6)+'.jpg'))
                    metadata.append(
                        {
                        'videoname':cdname + "_" + videoname,
                        'maskpath':os.path.join(path_cdname, videoname, "ROI.bmp"),
                        'idx_begin':int(idx_begin),
                        'idx_end':int(idx_end)
                        }
                    )
    return data, metadata

def getall_label_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "dataset")
    data, metadata = [], []
    for cdname in os.listdir(path_tri):
        path_cdname = os.path.join(path_tri, cdname)
        for videoname in os.listdir(path_cdname):
            with open(os.path.join(path_cdname, videoname, 'temporalROI.txt'), 'r') as f:
                idx_begin, idx_end = f.readline().split(" ")
                for idx in range(1, int(idx_end)+1):
                    data.append(os.path.join(path_cdname, videoname, "groundtruth", 'gt'+str(idx).zfill(6)+'.png'))
                    metadata.append(None)
    return data, metadata

def getall_data_valid(datasetpath:str):
    raise ValueError("!")
    data, metadata = [], []
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
    mypath = Path.db_root_dir('cdnet2014')
    
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