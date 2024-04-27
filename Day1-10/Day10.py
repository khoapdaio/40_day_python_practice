


import numpy as np
import tensorflow as tf
import torch

# Câu 1: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor từ danh sách 1 chiều ?
list_1D = [i for i in range(1, 11)]
arr_1D = np.array(list_1D)
print("- Mảng 1 chiều Numpy:", arr_1D, type(arr_1D), sep = "\n", end = "\n")

tensor_1D = torch.tensor(list_1D)
print("- Tensor Pytorch 1 chiều:", tensor_1D, type(tensor_1D), tensor_1D.device, sep = "\n", end = "\n")

tensor_1D_tf = tf.convert_to_tensor(list_1D)
print("- Tensor TensorFlow 1 chiều:", tensor_1D_tf, type(tensor_1D_tf), tensor_1D_tf.device, sep = "\n", end = "\n")


# Câu 2: Hãy viết chương trình tạo Numpy array, Tensorflow tensor, Pytorch tensor từ danh sách 2 chiều. Sau đó thực hiện kiểm tra thuộc tính shape, dtype, type, device từ các array, tensor vừa tạo
list_2D=[[j for j in range((i+((i-1)*2)),(i+((i-1)*2))+3)]for i in range(1,4)]
print(list_2D)


arr_2D= np.array(list_2D)
print("Hình dạng của mảng: ",arr_2D.shape)
print("Kiểu dữ liệu của mảng: ",arr_2D.dtype)
print("Loại của mảng: ",type(arr_2D))
print("Mảng:\n",arr_2D)

arr_2D_pt= torch.tensor(list_2D)
print("Hình dạng của tensor: ",arr_2D_pt.shape)
print("Kiểu dữ liệu của tensor: ",arr_2D_pt.dtype)
print("Loại của tensor: ",type(arr_2D_pt))
print("Tensor:\n",arr_2D_pt)

arr_2D_tf= tf.convert_to_tensor(list_2D)
print("Hình dạng của tensor: ",arr_2D_tf.shape)
print("Kiểu dữ liệu của tensor: ",arr_2D_tf.dtype)
print("Loại của tensor: ",type(arr_2D_tf))
print("Tensor:\n",arr_2D_tf)