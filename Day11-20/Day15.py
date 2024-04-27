# Day 15

# Tạo list có tên lst_data=[1,1.1,None,1.4, None ,1.5, None,2.0]. Sau đó , áp dụng phương pháp nội suy Nearest Neighbor để gắn giá trị None có trong lst_data

lst_data = [1, 1.1, None, 1.4, None, 1.5, None, 2.0]

for i, num in enumerate(lst_data):
	if num == None:
		lst_data[i] = lst_data[i - 1]
print(lst_data)
