# Câu 1: Tạo mới một List gồm các số từ 1 đến 10

lists = [i for i in range(1, 11)]
print(lists)
# Câu 2: In ra kết quả 5 phần tử đầu tiên có trong List trên
print(lists[:5])
# Câu 3: In ra kết quả phần tử có giá trị không chia hết cho 2
for x in (i for i in lists if i % 2 != 0):
    print(x)

# Câu 4:In ra kết quả tổng các giá trị trong list dùng kết hợp với vòng lặp for
print((sum(i for i in lists)))
