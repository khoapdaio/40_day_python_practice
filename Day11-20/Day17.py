#Day 17

# Tạo list 2D có tên là lst_data có dạng 3x3, gồm cá số từ 1 đến 9, ứng với các vị trí trong List.Sau đó tạo list khác có tên lst_sub_data là 2d list để lưu giá trị vị trí index thứ 0 và thứ 2 của lst_data chỉ sử dụng for . In ra màn hình kết quả của lst_sub_data

list_2D=[[j for j in range((i+((i-1)*2)),(i+((i-1)*2))+3)]for i in range(1,4)]

for  num in list_2D:
  del num[1]


print(list_2D)

# Câu 1: hãy tính tổng và hiệu 2 ma trận a+b

a =[[j for j in range((i+((i-1)*2)),(i+((i-1)*2))+3)]for i in range(1,4)]
b =[[2,4,6],[1,3,5],[1,0,1]]
c = [[0] * 3 for _ in range(3)]
d = [[0] * 3 for _ in range(3)]
e = [[0] * 3 for _ in range(3)]
print(type(c))
for i in range(len(a)):
  for j in range(len(a[i])):
    c[i][j] = a[i][j] + b[i][j]
    d[i][j]= a[i][j]-b[i][j]
    for k in range(len(a)):
      e[i][j] += a[i][k]*b[k][j]

print(f'- Tổng: {c}')
print(f'- Hiệu: {d}')
print(f'- Dot product: {e}')

