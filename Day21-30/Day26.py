# Day 26
#
# !apt-get -qq install -y libsm6 libxext6 && pip install -q -U opencv-python
# !pip install matplotlib
#
#
# Câu 1: Hãy đọc và hiển thị ảnh có tên 1.jpg trong tập dữ liệu trên
# Câu 2: Chuyển ảnh màu thành xám và hiển thị

import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("/content/drive/MyDrive/Colab Notebooks/Day26/1.jpg")
rgb_img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(rgb_img)
plt.show()

img = cv2.imread("/content/drive/MyDrive/Colab Notebooks/Day26/1.jpg",0)
plt.imshow(img,cmap='gray')
plt.show()

# Câu 3: Tăng cường độ sáng ảnh màu lên 50 đơn vị và giảm cường độ sáng xuống 80 đơn vị và hiện thị

img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

brightened_image = img.astype(np.float32) + 50
brightened_image = np.clip(brightened_image ,0,255)
brightened_image = brightened_image .astype(np.uint8)



darkened_image  = img.astype(np.float32)-80
darkened_image  = np.clip(darkened_image  ,0,255)
darkened_image  = darkened_image.astype(np.uint8)


plt.figure(figsize=(10,5))

plt.subplot(1,3,1)
plt.imshow(img)
plt.title('Original Image')


plt.subplot(1,3,2)
plt.imshow(brightened_image)
plt.title('Brightened Image')

plt.subplot(1,3,3)
plt.imshow(darkened_image)
plt.title('Darkened Image')