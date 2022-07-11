import os, sys

class Path(object):
    @staticmethod
    def db_root_dir(dataset):
        dataset = dataset.lower()
        if sys.platform == 'linux':
            mypath = "/media/newdisk/home2/liyaning2/Desktop/dataset/"
        elif sys.platform == "win32":
            mypath = "E:\\dataset\\"
        path_largeimg = 'dataset-large-img'
        path_fg_det = 'dataset-fg-det'
        path_optical = 'dataset-opticalflow'

        # ====================================================
        # 大型基准图片数据集，多用途
        if dataset == 'coco': 
            return os.path.join(mypath, path_largeimg, 'COCO2017')
        # ====================================================
        # fg_det
        elif dataset == 'au_air': 
            return os.path.join(mypath, path_fg_det, 'au_air')
        elif dataset in ['cdnet2014' ,'cdnet14' ] :
            return os.path.join(mypath, path_fg_det, 'CDnet2014')
        elif dataset == 'davis2017':
            return os.path.join(mypath, path_fg_det, 'DAVIS2017')
        elif dataset == 'janus_uav':
            return os.path.join(mypath, path_fg_det, 'Janus_UAV_Dataset')
        elif dataset == 'okutama_action':
            raise NotImplementedError("这个数据集不行")
            return os.path.join(mypath, path_fg_det, 'Okutama-Action_Dataset')
        elif dataset == 'uav123fps10':
            return os.path.join(mypath, path_fg_det, 'UAV123_10fps')
        elif dataset == 'kitti_mod':
            return os.path.join(mypath, path_fg_det, 'KITTI_MOD_fixed')
        elif dataset == 'pesmod':
            return os.path.join(mypath, path_fg_det, 'PESMOD')
        # ====================================================
        # 光流
        elif dataset == 'chairsd':
            return os.path.join(mypath, path_optical, 'ChairsSDHom')
        elif dataset == 'flyingchairs':
            return os.path.join(mypath, path_optical, 'FlyingChairs_release')
        elif dataset == 'flyingthings3d':
            raise NotImplementedError("这个数据集不行")
            return os.path.join(mypath, path_optical, 'flyingthings3d')
        elif dataset == 'kitti_flow':
            return os.path.join(mypath, path_optical, 'KITTI-flow2012')
            raise NotImplementedError("这个数据集不行")
        elif dataset == 'sintel':
            return os.path.join(mypath, path_optical, 'Sintel')
            
        # ==========================================================
        else:
            print('Dataset {} not available.'.format(dataset))
            raise NotImplementedError('Dataset {} not available.'.format(dataset))


if __name__ == "__main__":
    for datasetname in ['coco',
                        'au_air','cdnet2014','davis2017','janus_uav','uav123fps10 ','kitti_mod','pesmod',
                        'chairsd','flyingchairs','sintel']:
        temp = Path.db_root_dir(datasetname)
        assert(os.listdir(temp) != [])
        print(temp)