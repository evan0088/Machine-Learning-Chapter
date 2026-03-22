# 导包
import torch
import numpy as np

# TODO 1.tensor(data,dtype)创建张量: 可以指定数据和类型
print(torch.tensor(10))  # 此处10是数据
print(torch.tensor(10).ndim)  # 此处10是数据
print(torch.tensor([10]).ndim)
print(torch.tensor([[10]]).ndim)
print(torch.tensor([[[10]]]).ndim)
# 通过列表创建张量
print(torch.tensor([[1, 2, 3], [4, 5, 6]]))
print(torch.tensor([[1, 2, 3], [4, 5, 6]]).dtype)  # 默认torch.int64
# 通过numpy创建张量
print(torch.tensor(np.array([[1, 2, 3], [4, 5, 6]])))  # dtype=torch.int32
print('---------------------------------------------------')
# dtype 可以直接制定类型
print(torch.tensor([[1, 2, 3], [4, 5, 6]], dtype=torch.float32))
print(torch.tensor(np.array([[1, 2, 3], [4, 5, 6]]), dtype=torch.float32))
print('====================================================================')
# TODO 2.Tensor(data/size)创建张量: 注意: 不带[]默认是形状  注意:Tensor没有dtype参数
print(torch.Tensor(10))  # 此处10是形状 默认数据是0.
print(torch.Tensor(10).ndim)  # 此处10是形状 默认数据是0.
print(torch.Tensor([10]).ndim)
print(torch.Tensor([[10]]).ndim)
print(torch.Tensor([[[10]]]).ndim)
print(torch.Tensor(2, 3))  # 此处2,3是形状 默认数据是0.
print(torch.Tensor(size=(2, 3)))
# 通过列表创建张量
print(torch.Tensor([[1, 2, 3], [4, 5, 6]]))
print(torch.Tensor([[1, 2, 3], [4, 5, 6]]).dtype)  # 默认torch.float32
# 通过numpy创建张量
print(torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]])))
print(torch.Tensor(np.array([[1, 2, 3], [4, 5, 6]])).dtype)  # torch.float32
print('---------------------------------------------------')
# TODO 3.IntTensor()/FloatTensor()/LongTensor()/ShortTensor()/ByteTensor()/HalfTensor()创建张量
print(torch.ByteTensor([[1, 2, 3], [4, 5, 6]]))
print(torch.ShortTensor([[1, 2, 3], [4, 5, 6]]))
print(torch.IntTensor([[1, 2, 3], [4, 5, 6]]))
print(torch.LongTensor([[1, 2, 3], [4, 5, 6]]))  # 默认int64
print(torch.HalfTensor([[1, 2, 3], [4, 5, 6]]))
print(torch.FloatTensor([[1, 2, 3], [4, 5, 6]]))  # 默认float32
print(torch.DoubleTensor([[1, 2, 3], [4, 5, 6]]))
