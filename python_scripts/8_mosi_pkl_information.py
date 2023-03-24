'''
information of mosi.pkl
'''


from global_configs import PATH_FEATURE 
from global_configs import mosi_file

import pickle

def info_mosi():
    # args_dataset = "mosi"
    # data_path = f"{PATH_FEATURE}"+f"{args_dataset}.pkl"
    data_path = mosi_file
    with open(data_path, "rb") as handle:
        data = pickle.load(handle)
    print("keys: ", data.keys())
    train_data = data["train"]
    dev_data = data["dev"]
    test_data = data["test"]
    print("len train_data : ", len(train_data), "type: ", type(train_data))
    print("-"*20)
    train_data_0 = train_data[0]
    info_mosi_a_example(train_data_0)
    train_data_1 = train_data[1]
    info_mosi_a_example(train_data_1)


def info_mosi_a_example(train_data_0): 
    print("len train_data_0: ", len(train_data_0), "type:", type(train_data_0))
    (words, visual, acoustic), label_id, segment = train_data_0 
    print("words: ",type(words) , words)
    print("visual: ", type(visual), visual.shape)
    print("acoustic: ", type(acoustic), acoustic.shape)
    print("label_id: ", type(label_id), label_id.shape)
    print("segment: ", type(segment), segment)
    print("-"*20)



info_mosi()

