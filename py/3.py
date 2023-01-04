import torch.nn as nn
import torch
# (L+2*padding-(kernel-1)-1)/2 + 1
# (50+2*0-2-1)/2+1=47/2+1 = 23+1 = 24 
m = nn.Conv1d(16, 33, 3, stride=2)
input = torch.randn(20, 16, 50)
output = m(input)
print(output.shape) # 20,33,24
