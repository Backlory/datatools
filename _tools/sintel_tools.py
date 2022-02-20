import os, sys

def getall_data_train(datasetpath:str):
    data, metadata = [], []
    path_tri = os.path.join(datasetpath, "MPI-Sintel-complete",'training','clean')
    for videoname in os.listdir(path_tri):
        path_video =  os.path.join(path_tri, videoname)
        for idx in range(1,1+len(os.listdir(path_video))):
            data.append(os.path.join(path_video, 'frame_'+str(idx).zfill(4)+'.png'))
            metadata.append('clean_'+videoname)
    #
    path_tri = os.path.join(datasetpath, "MPI-Sintel-complete",'training','albedo')
    for videoname in os.listdir(path_tri):
        path_video =  os.path.join(path_tri, videoname)
        for idx in range(1,1+len(os.listdir(path_video))):
            data.append(os.path.join(path_video, 'frame_'+str(idx).zfill(4)+'.png'))
            metadata.append('albedo_'+videoname)
    #
    path_tri = os.path.join(datasetpath, "MPI-Sintel-complete",'training','final')
    for videoname in os.listdir(path_tri):
        path_video =  os.path.join(path_tri, videoname)
        for idx in range(1,1+len(os.listdir(path_video))):
            data.append(os.path.join(path_video, 'frame_'+str(idx).zfill(4)+'.png'))
            metadata.append('final_'+videoname)
    return data, metadata

def getall_label_train(datasetpath:str):
    data, metadata = [], []
    path_tri = os.path.join(datasetpath, "MPI-Sintel-complete",'training','flow')
    for videoname in os.listdir(path_tri):
        path_video =  os.path.join(path_tri, videoname)
        for idx in range(1,1+len(os.listdir(path_video))):
            data.append(os.path.join(path_video, 'frame_'+str(idx).zfill(4)+'.flo'))
            metadata.append('flow_'+videoname)
        data.append('This is the 50th frame and this frame has not any flow information.')
        metadata.append('flow_'+videoname)
    data *= 3
    metadata *= 3
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
    mypath = Path.db_root_dir('sintel')
    
    try:
        train_data, train_metadata = getall_data_train(mypath)
        print('len=', len(train_data),', ', train_data[0])
        train_label, train_metalabel = getall_label_train(mypath)
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