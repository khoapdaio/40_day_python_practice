# Day twelve

# Câu 1: Hãy viết chương tình sử dụng hàm zeros tạo Numpy array, Tensorflow tensor, Pytorch tensor chỉ chứa giá trị là số 0 với kích thước 3,4

import numpy as np

# tạo array toàn số 0
arr_zeros = np.zeros((3, 4))
print(arr_zeros)

import torch

# tạo tensor toàn số 0
tensor_zeros = torch.zeros((3, 4))
print(tensor_zeros)

import tensorflow as tf

# tạo tensor toàn là số 0
tensor_zeros = tf.zeros((3, 4))
print(tensor_zeros)

# câu 2: Hãy viết chương tình sử dụng hàm zeros tạo Numpy array, Tensorflow tensor, Pytorch tensor chỉ chứa giá trị là số 1 với kích thước 3,4

import numpy as np

# tạo array toàn số 1
arr_zeros = np.ones((3, 4))
print(arr_zeros)

import torch

# tạo tensor toàn số 1
tensor_zeros = torch.ones((3, 4))
print(tensor_zeros)

import tensorflow as tf

# tạo tensor toàn là số 1
tensor_zeros = tf.ones((3, 4))
print(tensor_zeros)

# Câu 3: Hãy viết chương tình sử dụng hàm zeros tạo Numpy array, Tensorflow tensor, Pytorch tensor chỉ chứa giá trị là số 5 với kích thước 3,4

import numpy as np

# tạo array toàn số 1
arr_zeros = np.full((3, 4), 5)

print(arr_zeros)

import torch

# tạo tensor toàn số 1
tensor_zeros = torch.full((3, 4), 5)
print(tensor_zeros)

import tensorflow as tf

# tạo tensor toàn là số 1
tensor_zeros = tf.fill((3, 4), 5)
print(tensor_zeros)
