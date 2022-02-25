import os, sys
from pydoc import doc

seqUAV123_10fps = [
    ('name','bike1','path','bike1','startFrame',1,'endFrame',1029,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','bike2','path','bike2','startFrame',1,'endFrame',185,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','bike3','path','bike3','startFrame',1,'endFrame',145,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','bird1_1','path','bird1','startFrame',1,'endFrame',85,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','bird1_2','path','bird1','startFrame',259,'endFrame',493,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','bird1_3','path','bird1','startFrame',525,'endFrame',813,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat1','path','boat1','startFrame',1,'endFrame',301,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat2','path','boat2','startFrame',1,'endFrame',267,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat3','path','boat3','startFrame',1,'endFrame',301,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat4','path','boat4','startFrame',1,'endFrame',185,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat5','path','boat5','startFrame',1,'endFrame',169,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat6','path','boat6','startFrame',1,'endFrame',269,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat7','path','boat7','startFrame',1,'endFrame',179,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat8','path','boat8','startFrame',1,'endFrame',229,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','boat9','path','boat9','startFrame',1,'endFrame',467,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','building1','path','building1','startFrame',1,'endFrame',157,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','building2','path','building2','startFrame',1,'endFrame',193,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','building3','path','building3','startFrame',1,'endFrame',277,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','building4','path','building4','startFrame',1,'endFrame',263,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','building5','path','building5','startFrame',1,'endFrame',161,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car1_1','path','car1','startFrame',1,'endFrame',251,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car1_2','path','car1','startFrame',251,'endFrame',543,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car1_3','path','car1','startFrame',543,'endFrame',877,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car2','path','car2','startFrame',1,'endFrame',441,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car3','path','car3','startFrame',1,'endFrame',573,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car4','path','car4','startFrame',1,'endFrame',449,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car5','path','car5','startFrame',1,'endFrame',249,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car6_1','path','car6','startFrame',1,'endFrame',163,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car6_2','path','car6','startFrame',163,'endFrame',603,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car6_3','path','car6','startFrame',603,'endFrame',985,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car6_4','path','car6','startFrame',985,'endFrame',1309,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car6_5','path','car6','startFrame',1309,'endFrame',1621,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car7','path','car7','startFrame',1,'endFrame',345,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car8_1','path','car8','startFrame',1,'endFrame',453,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car8_2','path','car8','startFrame',453,'endFrame',859,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car9','path','car9','startFrame',1,'endFrame',627,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car10','path','car10','startFrame',1,'endFrame',469,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car11','path','car11','startFrame',1,'endFrame',113,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car12','path','car12','startFrame',1,'endFrame',167,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car13','path','car13','startFrame',1,'endFrame',139,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car14','path','car14','startFrame',1,'endFrame',443,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car15','path','car15','startFrame',1,'endFrame',157,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car16_1','path','car16','startFrame',1,'endFrame',139,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car16_2','path','car16','startFrame',139,'endFrame',665,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car17','path','car17','startFrame',1,'endFrame',353,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car18','path','car18','startFrame',1,'endFrame',403,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group1_1','path','group1','startFrame',1,'endFrame',445,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group1_2','path','group1','startFrame',445,'endFrame',839,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group1_3','path','group1','startFrame',839,'endFrame',1309,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group1_4','path','group1','startFrame',1309,'endFrame',1625,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group2_1','path','group2','startFrame',1,'endFrame',303,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group2_2','path','group2','startFrame',303,'endFrame',591,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group2_3','path','group2','startFrame',591,'endFrame',895,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group3_1','path','group3','startFrame',1,'endFrame',523,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group3_2','path','group3','startFrame',523,'endFrame',943,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group3_3','path','group3','startFrame',943,'endFrame',1457,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','group3_4','path','group3','startFrame',1457,'endFrame',1843,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person1','path','person1','startFrame',1,'endFrame',267,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person2_1','path','person2','startFrame',1,'endFrame',397,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person2_2','path','person2','startFrame',397,'endFrame',875,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person3','path','person3','startFrame',1,'endFrame',215,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person4_1','path','person4','startFrame',1,'endFrame',501,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person4_2','path','person4','startFrame',501,'endFrame',915,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person5_1','path','person5','startFrame',1,'endFrame',293,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person5_2','path','person5','startFrame',293,'endFrame',701,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person6','path','person6','startFrame',1,'endFrame',301,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person7_1','path','person7','startFrame',1,'endFrame',417,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person7_2','path','person7','startFrame',417,'endFrame',689,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person8_1','path','person8','startFrame',1,'endFrame',359,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person8_2','path','person8','startFrame',359,'endFrame',509,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person9','path','person9','startFrame',1,'endFrame',221,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person10','path','person10','startFrame',1,'endFrame',341,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person11','path','person11','startFrame',1,'endFrame',241,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person12_1','path','person12','startFrame',1,'endFrame',201,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person12_2','path','person12','startFrame',201,'endFrame',541,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person13','path','person13','startFrame',1,'endFrame',295,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person14_1','path','person14','startFrame',1,'endFrame',283,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person14_2','path','person14','startFrame',283,'endFrame',605,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person14_3','path','person14','startFrame',605,'endFrame',975,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person15','path','person15','startFrame',1,'endFrame',447,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person16','path','person16','startFrame',1,'endFrame',383,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person17_1','path','person17','startFrame',1,'endFrame',501,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person17_2','path','person17','startFrame',501,'endFrame',783,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person18','path','person18','startFrame',1,'endFrame',465,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person19_1','path','person19','startFrame',1,'endFrame',415,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person19_2','path','person19','startFrame',415,'endFrame',931,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person19_3','path','person19','startFrame',931,'endFrame',1453,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person20','path','person20','startFrame',1,'endFrame',595,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person21','path','person21','startFrame',1,'endFrame',163,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person22','path','person22','startFrame',1,'endFrame',67,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','person23','path','person23','startFrame',1,'endFrame',133,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','truck1','path','truck1','startFrame',1,'endFrame',155,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','truck2','path','truck2','startFrame',1,'endFrame',129,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','truck3','path','truck3','startFrame',1,'endFrame',179,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','truck4_1','path','truck4','startFrame',1,'endFrame',193,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','truck4_2','path','truck4','startFrame',193,'endFrame',421,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav1_1','path','uav1','startFrame',1,'endFrame',519,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav1_2','path','uav1','startFrame',519,'endFrame',793,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav1_3','path','uav1','startFrame',825,'endFrame',1157,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav2','path','uav2','startFrame',1,'endFrame',45,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav3','path','uav3','startFrame',1,'endFrame',89,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav4','path','uav4','startFrame',1,'endFrame',53,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav5','path','uav5','startFrame',1,'endFrame',47,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav6','path','uav6','startFrame',1,'endFrame',37,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav7','path','uav7','startFrame',1,'endFrame',125,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','uav8','path','uav8','startFrame',1,'endFrame',101,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard1','path','wakeboard1','startFrame',1,'endFrame',141,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard2','path','wakeboard2','startFrame',1,'endFrame',245,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard3','path','wakeboard3','startFrame',1,'endFrame',275,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard4','path','wakeboard4','startFrame',1,'endFrame',233,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard5','path','wakeboard5','startFrame',1,'endFrame',559,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard6','path','wakeboard6','startFrame',1,'endFrame',389,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard7','path','wakeboard7','startFrame',1,'endFrame',67,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard8','path','wakeboard8','startFrame',1,'endFrame',515,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard9','path','wakeboard9','startFrame',1,'endFrame',119,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','wakeboard10','path','wakeboard10','startFrame',1,'endFrame',157,'nz',6,'ext','jpg','init_rect',[0,0,0,0]),
    ('name','car1_s','path','car1_s','startFrame',1,'endFrame',492,'nz',6,'ext','jpg','init_rect', [0,0,0,0]),
    ('name','car2_s','path','car2_s','startFrame',1,'endFrame',107,'nz',6,'ext','jpg','init_rect', [0,0,0,0]),
    ('name','car3_s','path','car3_s','startFrame',1,'endFrame',434,'nz',6,'ext','jpg','init_rect', [0,0,0,0]),
    ('name','car4_s','path','car4_s','startFrame',1,'endFrame',277,'nz',6,'ext','jpg','init_rect', [0,0,0,0]),
    ('name','person1_s','path','person1_s','startFrame',1,'endFrame',534,'nz',6,'ext','jpg','init_rect', [0,0,0,0]),
    ('name','person2_s','path','person2_s','startFrame',1,'endFrame',84,'nz',6,'ext','jpg','init_rect', [0,0,0,0]),
    ('name','person3_s','path','person3_s','startFrame',1,'endFrame',169,'nz',6,'ext','jpg','init_rect', [0,0,0,0])]


def getall_data_train(datasetpath:str):
    data, metadata = [], []
    path_tri = os.path.join(datasetpath, "data_seq",'UAV123_10fps')
    for i in range(123):
        _,label_name,_,videoname,_,startFrame,_, endFrame, _,_,_,_,_,_ = seqUAV123_10fps[i]
        for idx in range(startFrame, endFrame+1):
            data.append(os.path.join(path_tri, videoname, str(idx).zfill(6)+'.jpg'))
            metadata.append(videoname)
    return data, metadata

def getall_label_train(datasetpath:str):
    label, metadata = [], []
    for i in range(123):
        _,label_name,_,videoname,_,startFrame,_, endFrame, _,_,_,_,_,_ = seqUAV123_10fps[i]
        with open(os.path.join(datasetpath, "anno",'UAV123_10fps', label_name+'.txt'), 'r') as f:
            for line in f.readlines():
                temp = line[:-1].split(",")
                if "NaN" in temp:
                    label.append([{'bbox':[0,0,0,0]}])
                else:
                    temp = [int(x) for x in temp]
                    temp = [{'bbox':[temp[0], temp[1], temp[0]+temp[2], temp[1]+temp[3]]}]
                    label.append(temp)
    return label, metadata

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
    mypath = Path.db_root_dir('uav123fps10')
    
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
