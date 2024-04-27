# Day 34

# - Bộ lọc Gauss là một kỹ thuật xử lý ảnh phổ biến được sử dụng để làm mịn ảnh và loại bỏ nhiễu. Nó hoạt động bằng cách áp dụng một ma trận Gauss lên từng pixel của ảnh
# - Hàm Gauss là một hàm phân phối xác xuất có dạng hình chuông. giá trị của hàm Gauss tại mỗi pixel được xác định bởi độ lệnh chuẩn sigma của hàm. Sigma càng lớn, mức độ làm mịn càn cao. Công thức tổng quát của Gaussian Filter như sau:
#
#
# Bài tập Hãy đọc và hiển thị ảnh có tên 2.jpg trong tập dữ liệu trên, áp dụng kỹ thuật Gaussian Filter trong thư viện OpenCv theo 2 cách cài đặt với các sigma khác nhau [2.5,5.0,10.0]
import cv2
import matplotlib.pyplot as plt

# def gaussian_kernel ( size , sigma ) :
#   if size % 2 == 0:
#     size = size + 1
#     max_point = size // 2 # both directions (x,y) maximum
#     min_point = - max_point # both directions (x,y) minimum
#
#   K = np . zeros (( size , size ) ) # kernel matrix
#   for x in range ( min_point , max_point + 1) :
#     for y in range ( min_point , max_point + 1) :
#       value = # Gaussian Filter Forumla Here #
#       K [ x - min_point , y - min_point ] = value
#
#   return K
#
# kernel = gaussian_kernel (5 , 1.4)
# img = cv2 . imread (" image_path ", 0)
# img_gaussian = cv2 . filter2D ( img , -1 , kernel )

import cv2
import matplotlib.pyplot as plt

# Đọc ảnh từ tệp 2.jpg
image = cv2.imread('/content/drive/MyDrive/Colab Notebooks/2.jpg')

# Chuyển đổi ảnh sang dạng gray (nếu cần)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

plt.subplot(1, 4, 1)
plt.title('Sigma = origin')
plt.imshow(cv2.cvtColor(image_gray, cv2.COLOR_BGR2RGB))
# Các giá trị sigma khác nhau
sigmas = [2.5, 5.0, 10.0]

# Áp dụng bộ lọc Gaussian với các sigma khác nhau và hiển thị ảnh
plt.figure(figsize=(10, 5))
for i, sigma in enumerate(sigmas):
    # Áp dụng bộ lọc Gaussian
    gaussian_image = cv2.GaussianBlur(image_gray, (5, 5), sigma)

    # Hiển thị ảnh
    plt.subplot(1, len(sigmas)+1, i+1)
    plt.title(f'Sigma = {sigma}')
    plt.imshow(cv2.cvtColor(gaussian_image, cv2.COLOR_BGR2RGB))
    plt.axis('off')

plt.show()

