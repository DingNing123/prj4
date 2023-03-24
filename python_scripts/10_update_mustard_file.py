'''
update_mustard_file.py
'''

from global_configs import mustard_file
from global_configs import mustard_2023_file
import pickle
import os

def formatsize(bytes):
    try:
        bytes = float(bytes)  # 默认字节
        kb = bytes / 1024  # 换算KB
    except:
        print("字节格式有误")
        return "Error"


    if kb >= 1024:
        M = kb / 1024  # KB换成M
        if M >= 1024:
            G = M / 1024
            return "%fG" % G
        else:
            return "%fM" % M
    else:
        return "%fkb" % kb


# 获取文件大小
def Getfile(path):
    try:
        size = os.path.getsize(path)
        return formatsize(size)
    except:
        print("获取文件大小错误")



def update_mustard(data, file_path):
    output = open(file_path, 'wb')
    pickle.dump(data,  output)
    print('success dumped to ', file_path)

def update_info(data, str1):
    data['info'].append(str1)

def update_1(data):
    '''
    Add info structure
    '''
    data['info'] = []
    str1 = "info : Records the feature structure information of the data set and the updated log info：记录mustard数据集特特征结构信息，更新的日志"
    update_info(data,str1)

def update_2(data):
    '''
    Add info structure
    '''
    str2 = """更新键的值，让它更加通用。
比如audio_feature -》 audio
video_features_p -> vision
bert_indices->text_bert_indices
...
首先是要打印这些形状，做一些确认工作
"""
    update_info(data,str2)

def update_3(data):
    '''
    Add info structure
    '''
    print(data.keys())
    # ['train', 'valid', 'test', 'info']
    for one in ['train', 'valid', 'test'] :
        print(one, "-"*50)
        example = data[one]
        # print(example.keys())
        # ['audio_feature', 'video_features_p', 'bert_indices', 'box_pad_indices', 'big_graphs', 'labels', 'vision_full_feature', 'video_ids']
        # print(example['audio_feature'].shape)
        # 更新key(键)
        example['acoustic'] = example.pop("audio_feature")
        example['vision'] = example.pop("vision_full_feature")
        example['box_vision'] = example.pop("video_features_p")
        example['label'] = example.pop("labels")
        example['text_bert_indices'] = example.pop("bert_indices")
        example['text_box_indices'] = example.pop("box_pad_indices")
        print('acoustic', example['acoustic'].shape)
        print('vision', example['vision'].shape)
        print('box_vision', example['box_vision'].shape)
        print('text_bert_indices', example['text_bert_indices'].shape)
        print('text_box_indices', example['text_box_indices'].shape)
        print('label', example['label'].shape, example['label'][:10])
        print('video_ids', example['video_ids'].shape, example['video_ids'][:10])
        from global_configs import bert_base_uncased
        from transformers import BertTokenizer
        x = example['text_bert_indices']
        # text_bert_indices (554, 20)
        tokenizer = BertTokenizer.from_pretrained(bert_base_uncased)
        word = []
        for x_i in x:
            token_ids = x_i
            tokened_text = tokenizer.convert_ids_to_tokens(token_ids)
            word.append(tokened_text)
        # print('len word: ', len(word))
        # print('word :2 ', word[:2])
        example['word'] = word
        print('word: ', example['word'][:3])
        print(example.keys())




if __name__=="__main__":
    with open(mustard_file,'rb') as f:
        data = pickle.load(f)
    update_1(data)
    update_2(data)
    update_3(data)
    print('debug exit : Avoid writing files over and over again')
    exit()
    update_mustard(data, mustard_2023_file)
    print('@'*20)
    with open(mustard_2023_file,'rb') as f:
        data = pickle.load(f)
    print(data.keys())
    print(data['info'])
    print(f'{mustard_file} : ', Getfile(mustard_file))
    print(f'{mustard_2023_file} : ', Getfile(mustard_2023_file))


