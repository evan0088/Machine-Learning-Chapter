import torch

# TODO 1.创建线性张量
# todo arange() 连续 包左不包右,默认从0开始
print(torch.arange(10))  # 不指定start默认从0开始
print(torch.arange(2, 10))
print(torch.arange(2, 10, 2))
print('-------------------------------------')
# todo linspace() 等差 包左包右
print(torch.linspace(2, 10, 5))
print(torch.linspace(2, 10, 6))
print('==================================================')
# TODO 2.创建随机张量
print(torch.rand(2, 3))  # rand随机生成0-1的浮点数张量
print(torch.randn(2, 3))  # randn随机生成正态分布的浮点数张量
print(torch.randint(0, 10, size=(2, 3)))  # randint随机生成整数张量
print(torch.randint(10, 20, size=(2, 3)))
print('--------------------------------------')
# TODO 随机种子的设置和获取
# manual_seed() : 设置随机种子,保证随机数生成一致
print(torch.manual_seed(666))
print(torch.rand(2, 3))
print(torch.randn(2, 3))
print(torch.randint(10, (2, 3)))
print(torch.randint(10, 20, (2, 3)))
# initial_seed(): 获取当前随机种子
print(torch.initial_seed())
