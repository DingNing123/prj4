import torch.nn as nn
import torch
# 50+2*1-2-1+1=50
m = nn.Conv1d(16, 33, kernel_size = 3, stride=1,padding=1)
input = torch.randn(20, 16, 50)
output = m(input)
print(output.shape) # 20,33,50
