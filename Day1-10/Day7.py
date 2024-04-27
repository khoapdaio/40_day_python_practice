# câu 1: tạo mới một list có tên list_data gồm các số chẵn từ 1 đến 12
list_data = [i for i in range(1, 13) if i % 2 == 0]
print(list_data)

# Câu 2: Xóa tất cả các số chia hết cho 3 trong list_data
for i in list_data:
	if i % 3 == 0:
		list_data.remove(i)
print(list_data)

# Câu 3: Thêm vào cuối list_data các số từ 1 đến 3 , và thêm vào cị trí index=3 một chuỗi các số từ 6 đến 8
for i in range(1, 10):
	if 0 < i < 4:
		list_data.append(i)
print(list_data)

for i in range(8, 5, -1):
	if 5 < i < 9:
		list_data.insert(3, i)

print(list_data)

# Câu 4: Nếu các số trong list_data chia hết cho 2 hoặ chi hết cho 5 thì cập nhật thành số 0
for i in range(len(list_data)):
	if list_data[i] % 2 == 0 or list_data[i] % 5 == 0:
		list_data[i] = 0

print(list_data)
