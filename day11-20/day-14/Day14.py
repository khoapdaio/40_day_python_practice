#Day 14

# Câu 1: Viết chương trình tạo hai Numpy array, Pytorch tensor,Tensorflow tensor với các trị số nguyên ngẫu nhiên trong khoảng [-10,10] với ích thước (3,4). Sau đó chuyển vị array, tensor thứ 2 và thực hiện phép nhân matrix multiplication. Lưu ý: sử dụng seed=2024

# Sử dụng Numpy

import numpy as np


np.random.seed(2024)


array1= np.random.randint(-10,11,size=(3,4))

array2= np.random.randint(-10,11,size=(3,4))

array2_transposed=np.transpose(array2)

result_numpy =np.dot(array1,array2_transposed)

print("NumPy Array 1:")
print(array1)
print("\nNumPy Array 2 Transposed:")
print(array2_transposed)
print("\nResult of Matrix Multiplication:")
print(result_numpy)



# Sử dụng Pytorch

import torch


torch.manual_seed(2024)

tensor1 = torch.randint(-10,11,size=(3,4))

tensor2 = torch.randint(-10,11,size=(3,4))

tensor2_transposed = torch.transpose(tensor2,0,1)

result_pytorch=torch.matmul(tensor1,tensor2_transposed)

print("PyTorch Tensor 1:")
print(tensor1)
print("\nPyTorch Tensor 2 Transposed:")
print(tensor2_transposed)
print("\nResult of Matrix Multiplication:")
print(result_pytorch)



# Sử dụng tensorflow

import tensorflow as tf

tf.random.set_seed(2024)


tensor1_tf= tf.random.uniform((3,4),minval=-10,maxval=11,dtype=tf.int32)

tensor2_tf= tf.random.uniform((3,4),minval=-10,maxval=11,dtype=tf.int32)


tensor2_transposed_tf= tf.transpose(tensor2_tf)

result_tensorflow =tf.matmul(tensor1_tf, tensor2_transposed_tf)

print("TensorFlow Tensor 1:")
print(tensor1_tf)
print("\nTensorFlow Tensor 2 Transposed:")
print(tensor2_transposed_tf)
print("\nResult of Matrix Multiplication:")
print(result_tensorflow)

# Câu 2: Viết chương trình tạo một Numpy array, Pytorch tensor, Tensorflow tensor với các giá trị số nguyên ngẫu nhiên trong khaorng [-10,10] với kích thước (3,3). Sau đó hãy tính tổng của toàn bộ , tensor, array, tiếp theo tính tổng theo chiều dọc, chiều ngang. Lưu ý, sử dụng seed =2024

# sử dụng numpy

import numpy as np

# Thiết lập seed
np.random.seed(2024)

# Tạo một mảng NumPy với giá trị ngẫu nhiên trong khoảng [-10, 10]
array_np = np.random.randint(-10, 11, size=(3, 3))

# Tính tổng của toàn bộ mảng
sum_total_np = np.sum(array_np)

# Tính tổng theo chiều dọc và chiều ngang
sum_axis_0_np = np.sum(array_np, axis=0)
sum_axis_1_np = np.sum(array_np, axis=1)

print("NumPy Array:")
print(array_np)
print("\nTổng của toàn bộ mảng NumPy:", sum_total_np)
print("Tổng theo chiều dọc:", sum_axis_0_np)
print("Tổng theo chiều ngang:", sum_axis_1_np)

# sử dụng pytorch

import torch

# Thiết lập seed
torch.manual_seed(2024)

# Tạo một PyTorch tensor với giá trị ngẫu nhiên trong khoảng [-10, 10]
tensor_pt = torch.randint(-10, 11, size=(3, 3))

# Tính tổng của toàn bộ tensor
sum_total_pt = torch.sum(tensor_pt)

# Tính tổng theo chiều dọc và chiều ngang
sum_axis_0_pt = torch.sum(tensor_pt, dim=0)
sum_axis_1_pt = torch.sum(tensor_pt, dim=1)

print("PyTorch Tensor:")
print(tensor_pt)
print("\nTổng của toàn bộ PyTorch Tensor:", sum_total_pt)
print("Tổng theo chiều dọc:", sum_axis_0_pt)
print("Tổng theo chiều ngang:", sum_axis_1_pt)

# Sử dụng tensorflow

import tensorflow as tf

# Thiết lập seed
tf.random.set_seed(2024)

# Tạo một TensorFlow tensor với giá trị ngẫu nhiên trong khoảng [-10, 10]
tensor_tf = tf.random.uniform((3, 3), minval=-10, maxval=11, dtype=tf.int32)

# Tính tổng của toàn bộ tensor
sum_total_tf = tf.reduce_sum(tensor_tf)

# Tính tổng theo chiều dọc và chiều ngang
sum_axis_0_tf = tf.reduce_sum(tensor_tf, axis=0)
sum_axis_1_tf = tf.reduce_sum(tensor_tf, axis=1)

print("TensorFlow Tensor:")
print(tensor_tf)
print("\nTổng của toàn bộ TensorFlow Tensor:", sum_total_tf.numpy())
print("Tổng theo chiều dọc:", sum_axis_0_tf.numpy())
print("Tổng theo chiều ngang:", sum_axis_1_tf.numpy())