import torch.nn as nn
import torch

m = nn.Softplus()
input = torch.randn(10)
output = m(input)
print(output)

