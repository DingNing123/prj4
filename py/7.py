'''
clear warning :
    /Users/mac/Desktop/prj4/lmib.py:768: UserWarning: nn.init.xavier_normal 
    is now deprecated in favor of nn.init.xavier_normal_.
  xavier_normal(self.u1)
'''
from torch.nn.init import xavier_normal_
import torch 

x = torch.randn(2,3)
print(x)
print('-'*10)
xavier_normal_(x)
print(x)
