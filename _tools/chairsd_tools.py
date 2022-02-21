import os, sys

def getall_data_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "ChairsSDHom",'data', 'train','t0')
    data, metadata = [], []
    for idx in range(len(os.listdir(path_tri))):
        data.append(
                        (
                            os.path.join(path_tri, str(idx).zfill(5)+'.png'), 
                            os.path.join(path_tri, str(idx).zfill(5)+'.png').replace('t0','t1')
                        )
                    )
        metadata.append(None)
    return data, metadata

def getall_label_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "ChairsSDHom",'data', 'train','flow')
    data, metadata = [], []
    for idx in range(len(os.listdir(path_tri))):
        data.append(
                        os.path.join(path_tri, str(idx).zfill(5)+'.pfm'), 
                    )
        metadata.append(None)
    return data, metadata

def getall_data_valid(datasetpath:str):
    raise ValueError("there is no valid set!")
    return 

def getall_label_valid(datasetpath:str):
    raise ValueError("there is no valid set!")
    return 

def getall_data_test(datasetpath:str):
    path_tri = os.path.join(datasetpath, "ChairsSDHom",'data', 'test','t0')
    data, metadata = [], []
    for imgname in range(len(os.listdir(path_tri))):
        data.append(
                        (
                            os.path.join(path_tri, str(imgname).zfill(5)+'.png'), 
                            os.path.join(path_tri, str(imgname).zfill(5)+'.png').replace('t0','t1')
                        )
                    )
        metadata.append(None)
    sorted(data)
    return data, metadata

def getall_label_test(datasetpath:str):
    path_tri = os.path.join(datasetpath, "ChairsSDHom",'data', 'test','flow')
    data, metadata = [], []
    for imgname in range(len(os.listdir(path_tri))):
        data.append(
                        os.path.join(path_tri, str(imgname).zfill(5)+'.pfm'), 
                    )
        metadata.append(None)
    sorted(data)
    return data, metadata

if __name__ == "__main__":
    from _mypath import Path
    mypath = Path.db_root_dir('chairsd')
    
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