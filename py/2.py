from itertools import chain
x = chain('aaa','bbb')
for x0 in x:
    print(x0)
    
# chain 把几个迭代对象串联为一个更大的可迭代对象。
# --------------------------------

import torch.optim as optim
x = getattr(optim,'Adam')
print(x)
from torch.optim import Adam
x = Adam
print(x)