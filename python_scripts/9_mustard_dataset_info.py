'''
2023-3-24-Friday
Explore the structure of mustard's feature file
'''
import pickle
import numpy as np
from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from global_configs import feature_file

class MUStardDataset(Dataset):
    def __init__(self,mode = 'train',feature_path=feature_file):
        '''
        par mode: train|valid|test
        '''
        with open(feature_path,'rb') as f:
            data = pickle.load(f)
        self.feature_dict = data[mode]
        # [-1,1] -> [0,1]
        self.feature_dict['labels'] = ((self.feature_dict['labels'] + 1)/2).astype(np.int64)

    def __getitem__(self,index):
        feature ={}
        feature['audio_feature'] = self.feature_dict['audio_feature'][index]
        feature['video_features_p'] = self.feature_dict['video_features_p'][index]
        feature['bert_indices'] = self.feature_dict['bert_indices'][index]
        feature['box_pad_indices'] = self.feature_dict['box_pad_indices'][index]
        feature['big_graphs'] = self.feature_dict['big_graphs'][index]
        feature['labels'] = self.feature_dict['labels'][index]
        feature['video_ids'] = self.feature_dict['video_ids'][index]
        feature['index'] = index

        return feature
    def __len__(self):
        labels = self.feature_dict['labels']
        length = labels.shape[0]
        return length

    def get_one_sample(self,index):
        x = self.feature_dict.keys()
        print(x)
        # dict_keys(['audio_feature', 'video_features_p', 'bert_indices', 'box_pad_indices', 'big_graphs', 'labels', 'vision_full_feature', 'video_ids'])
        shape_dict = {}
        shape_dict['audio_feature'] = self.feature_dict['audio_feature'][index].shape
        shape_dict['video_features_p'] = self.feature_dict['video_features_p'][index].shape
        shape_dict['bert_indices'] = self.feature_dict['bert_indices'][index].shape
        shape_dict['box_pad_indices'] = self.feature_dict['box_pad_indices'][index].shape
        shape_dict['big_graphs'] = self.feature_dict['big_graphs'][index].shape
        shape_dict['labels_type'] = type(self.feature_dict['labels'][index])
        shape_dict['labels'] = self.feature_dict['labels'][index]
        shape_dict['vision_full_feature'] = self.feature_dict['vision_full_feature'][index].shape
        shape_dict['video_ids'] = self.feature_dict['video_ids'][index]
        return shape_dict


if __name__=="__main__":
    train_data = MUStardDataset('train')
    valid_data = MUStardDataset('valid')
    test_data = MUStardDataset('test')
    print('len train_data : ', len(train_data))
    print('len valid_data : ', len(valid_data))
    print('len test_data : ', len(test_data))
    print('-'*20)
    print('train_data_0 : ', train_data.get_one_sample(0))
    print('-'*20)
    print('train_data_1 : ', train_data.get_one_sample(1))

    # dl = DataLoader(d, batch_size=2, num_workers=0, shuffle=False)
    # batch_sample = iter(dl).next()
    # print(batch_sample.keys())
    # print(batch_sample['audio_feature'].size(2))
    # print(batch_sample['video_features_p'].size(2))
    '''
    dict_keys(['audio_feature', 'video_features_p', 'bert_indices', 'box_pad_indices', 'big_graphs', 'labels', 'video_ids', 'index'])
    33
    768
    '''

    
