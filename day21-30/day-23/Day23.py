#Day 23

# Câu 1: Hãy viết chương trình tạo Numpy array , Tensorflow tensor, Pytorch tensor trong khoảng [0,10] với step = 1

import numpy as np

# Tạo numpy array từ 0 đến 10 với bước là 1
numpy_array = np.arange(0, 11, 1)

print("NumPy Array:")
print(numpy_array)

import tensorflow as tf

# Tạo TensorFlow tensor từ 0 đến 10 với bước là 1
tf_tensor = tf.range(0, 11, 1)

print("TensorFlow Tensor:")
print(tf_tensor.numpy())

import torch

# Tạo PyTorch tensor từ 0 đến 10 với bước là 1
torch_tensor = torch.arange(0, 11, 1)

print("PyTorch Tensor:")
print(torch_tensor)


# Câu 2: hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor là ma trận đơn vị với kích thước (3,3)

import numpy as np

# Tạo numpy array là ma trận đơn vị kích thước (3,3)
numpy_array = np.eye(3)

print("NumPy Array (Identity Matrix):")
print(numpy_array)


import tensorflow as tf

# Tạo TensorFlow tensor là ma trận đơn vị kích thước (3,3)
tf_tensor = tf.eye(3)

print("TensorFlow Tensor (Identity Matrix):")
print(tf_tensor.numpy())


import torch

# Tạo PyTorch tensor là ma trận đơn vị kích thước (3,3)
torch_tensor = torch.eye(3)

print("PyTorch Tensor (Identity Matrix):")
print(torch_tensor)


# Câu 3: Hãy viết chương trình tạo Numpy array, tensorflow tensor , pytorch tensor ngẫu nhiên trong khoảng giá trị [0,1] với kích thước (3,4). Tiếp theo hãy tạo array, tensor với các giá trị là số nguyên trong khoảng [-10,10]. Lưu ý trong bài tập này, các bạn sẽ sử dụng seed =2024 để đảm bảo ra kết quả giống với đáp án ta cài đặt seed =2024

import numpy as np

# Đặt seed
np.random.seed(2024)

# Tạo numpy array ngẫu nhiên trong khoảng [0,1] kích thước (3,4)
numpy_array_random = np.random.rand(3, 4)

# In numpy array ngẫu nhiên
print("NumPy Array Random (0-1):")
print(numpy_array_random)

# Tạo numpy array ngẫu nhiên nguyên trong khoảng [-10,10]
numpy_array_int = np.random.randint(-10, 11, size=(3, 4))

# In numpy array ngẫu nhiên nguyên
print("\nNumPy Array Random Integer (-10 to 10):")
print(numpy_array_int)


import tensorflow as tf

# Đặt seed
tf.random.set_seed(2024)

# Tạo TensorFlow tensor ngẫu nhiên trong khoảng [0,1] kích thước (3,4)
tf_tensor_random = tf.random.uniform((3, 4))

# In TensorFlow tensor ngẫu nhiên
print("TensorFlow Tensor Random (0-1):")
print(tf_tensor_random.numpy())

# Tạo TensorFlow tensor ngẫu nhiên nguyên trong khoảng [-10,10]
tf_tensor_int = tf.random.uniform((3, 4), minval=-10, maxval=11, dtype=tf.int32)

# In TensorFlow tensor ngẫu nhiên nguyên
print("\nTensorFlow Tensor Random Integer (-10 to 10):")
print(tf_tensor_int.numpy())


import torch

# Đặt seed
torch.manual_seed(2014)

# Tạo PyTorch tensor ngẫu nhiên trong khoảng [0,1] kích thước (3,4)
torch_tensor_random = torch.rand(3, 4)

# In PyTorch tensor ngẫu nhiên
print("PyTorch Tensor Random (0-1):")
print(torch_tensor_random)

# Tạo PyTorch tensor ngẫu nhiên nguyên trong khoảng [-10,10]
torch_tensor_int = torch.randint(-10, 11, (3, 4))

# In PyTorch tensor ngẫu nhiên nguyên
print("\nPyTorch Tensor Random Integer (-10 to 10):")
print(torch_tensor_int)
