# Với việc sử dụng 3 ngoặc đơn hoặc 3 ngoặc kép ta có thể viết xuống dòng trong một biến thuộc kiểu String
a = """Test
thử
xem
có
chạy
được
không"""
b = '''
test
tương
tự
'''
print(a)
print(b)

# Mảng trong chuỗi
a = "Hello, World!"
print(a[1])

# Vòng lặp trong chuỗi
for x in "hello":
	print(x)


# Độ dài của chuỗi
a = "Hello, world!"
print(len(a))


#Kiểm tra chuỗi
txt="kiểm tra một chữ trong một chuỗi"
print("một" in txt)
if "một" in txt:
  print("có nha")
if "hai" not in txt:
  print("không có nha")



#Cắt chuỗi
txt = "Ví dụ cắt chuỗi"
#chuỗi[start:(end+1)]
print(txt[:4])
print(txt[1:4])
print(txt[1:])


# Sửa đổi chuỗi
txt = " Ví dụ sửa đổi chuỗi "
#đây là một số hàm cơ bản
print(txt.lower())
print(txt.upper())
print(txt.strip())
print(txt.rstrip())
print(txt.lstrip())
print(txt.replace("h","k"))
print(txt.split(" "))

# Format chuỗi

txt = "{0} kiểm tra {1} thật vui {2}"
a = "Ví dụ"
b = ", "
c = " :)"
#Số thứ tư trong text để fomat theo thứ tự từ 0->(n-1) và không quan tâm vị trí của nó
#hàm format(biến 1: 0,biến 2:1,....,biến n : n-1)
print(txt.format(a,b,c))


# Ký tự gạch chéo backslash
print("Ví dụ gạch chéo \"gạch chéo nè\" \' đây nữa nè\'")


y=2+3*5.
print(2/4)
x=1
x = x == x
print(x)

nums=[1,2,3]
vals=nums[-3:-2]

print(vals)
print(nums)

z=10
y=0
x= y<z and z>y or y>z and z<y
print(x)

my_list=[1,2,3]
for v in range(len(my_list)):
  my_list.insert(1,my_list[v])
print(my_list)

