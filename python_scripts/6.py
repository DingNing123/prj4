from torch.nn.init import xavier_normal
import torch 

x = torch.randn(2,3)
print(x)
print('-'*10)
xavier_normal(x)
print(x)
