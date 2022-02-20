import os, sys

def getall_data_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "Train")
    data, metadata = [], []
    for videoname in os.listdir(path_tri):  # video: 'video_1'
        frames = sorted(os.listdir(os.path.join(path_tri, videoname, "video")))
        for idx in range(len(frames)):
            data.append(os.path.join(path_tri, videoname, 'video', frames[idx]))
            metadata.append(videoname)
    return data, metadata

def getall_label_train(datasetpath:str):
    path_tri = os.path.join(datasetpath, "Train")
    data, metadata = [], []
    for videoname in os.listdir(path_tri):  # video: 'video_1'
        frames = sorted(os.listdir(os.path.join(path_tri, videoname, "gt_mov")))
        for idx in range(len(frames)):
            data.append(os.path.join(path_tri, videoname, 'gt_mov', frames[idx]))
            metadata.append(videoname)
    return data, metadata

def getall_data_valid(datasetpath:str):
    path_tri = os.path.join(datasetpath, "Validation")
    data, metadata = [], []
    for videoname in os.listdir(path_tri):  # video: 'video_1'
        frames = sorted(os.listdir(os.path.join(path_tri, videoname, "video")))
        for idx in range(len(frames)):
            data.append(os.path.join(path_tri, videoname, 'video', frames[idx]))
            metadata.append(videoname)
    return data, metadata

def getall_label_valid(datasetpath:str):
    path_tri = os.path.join(datasetpath, "Validation")
    data, metadata = [], []
    for videoname in os.listdir(path_tri):  # video: 'video_1'
        frames = sorted(os.listdir(os.path.join(path_tri, videoname, "gt_mov")))
        for idx in range(len(frames)):
            data.append(os.path.join(path_tri, videoname, 'gt_mov', frames[idx]))
            metadata.append(videoname)
    return data, metadata

def getall_data_test(datasetpath:str):
    raise ValueError("there is no test set!")
    return 

def getall_label_test(datasetpath:str):
    raise ValueError("there is no test set!")
    return

if __name__ == "__main__":
    from _mypath import Path
    mypath = Path.db_root_dir('janus_uav')
    
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