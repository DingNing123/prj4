import os
import torch

# os.environ["CUDA_VISIBLE_DEVICES"] = "2"
# os.environ["WANDB_PROGRAM"] = "main_mib.py"

# DEVICE = torch.device("cuda:0")

# check if CUDA is available
# if yes, set default tensor type to cuda
if torch.cuda.is_available():
    # torch.set_default_tensor_type(torch.cuda.FloatTensor)
    print("using cuda:", torch.cuda.get_device_name(0))
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
else:
    print("using cpu .")
    DEVICE = torch.device("cpu")
    

# MOSI SETTING
ACOUSTIC_DIM = 74
VISUAL_DIM = 47
TEXT_DIM = 768
'''
# MOSEI SETTING
ACOUSTIC_DIM = 74
VISUAL_DIM = 35
TEXT_DIM = 768
'''

# The location of the three data set feature files
PATH_FEATURE = "/home/dn/Desktop/deep_learning_tools/"
mosi_file = "/home/dn/Desktop/deep_learning_tools/mosi.pkl"

feature_file = "/media/dn/newdisk/deep_learning/2023/MustardIndepVit768.pkl"
mustard_file = "/media/dn/newdisk/deep_learning/2023/MustardIndepVit768.pkl"
mustard_2023_file = "/media/dn/newdisk/deep_learning/2023/Mustard2023IndepVit768.pkl"
bert_base_uncased = "/home/dn/Desktop/deep_learning_tools/bert-base-uncased/"
