# Day 24,25

# q1
n = 0
for i in range(0, 1000, 100):
	n += i
print(n)


# ans b

# q2

def a_function_helper( x ):
	if x > 0:
		return 'pos'
	else:
		return 'neg'


def a_function( data ):
	res = [a_function_helper(x) for x in data]
	return res


data = [1, 0, -1, 2]
print(a_function(data))
# ans b

# q3
data = "Python Programming"

print(data.split()[0])
# ans a

# q4

"elephant" * 1 > "ant" * 100

"""
nguyên tắc so sánh một chuỗi với một chuỗi ký tự:
- so sánh lần lượt từng ký tự, nếu ký tự giống nhau bỏ qua,
nếu khác nhau thì chuyển ký tự đó về mã unicode để so sánh giá trị của nó
và kết thúc so sánh
- luôn so sánh với giá trị unicode làm chuẩn
"""


# q5
def my_function( signal ):
	var = True
	while var:
		var = False
		for i in range(len(signal) - 1):
			if signal[i] > signal[i + 1]:
				signal[i], signal[i + 1] = signal[i + 1], signal[i]
				var = True


my_signal = [1, 0, 0, 1, 1, 1]
my_function(my_signal)
print(my_signal)

# Thuật toán sắp xếp tang dần

# q6

n = 0
for i in range(10):
	n += i
	if n > 0 and n % 2 == 0:
		break

print(n)


# Với tổng > 0 và tổng chia hết cho 2 thì kết thúc vòng lặp
# ta có 0 + 1 + 2 + 3 = 6 ->đạt đủ điều kiện để thoát vòng lặp
# ans c

# q7
def my_function( list_nums = [1, 2, 3, 4] ):
	var = 0
	for i in list_nums:
		var += i
	return var / len(list_nums)


my_function()
# vì đối sô list_nums có giá trị default nên khi dùng phương thức không cần truyền tham số vào a


# q8

space1 = "It's sunny here!"

space2 = "Is it hot here in the spring?"

space = space1 + space2
print(space[-7:-1])

# với python có hỗ trợ việc trỏ dữ liệu của một tập hợp
# từ phía cuối cúng phần tử cuối cùng sẽ là -1 rồi các phần tử
# trước phần từ cuối cùng giá trị lần lượt trừ đi 1
# res a

# q9

data = [1, 2, 3, "I", "am", "AI"]
new_data = sorted(data)
print(new_data)

# rule của việc sắp xếp của một list là là cùng một loại kiểu dữ liệu

# q10
my_string = "Duo, come here!"
my_bag_of_word = []
for element in my_string:
	if element not in my_bag_of_word:
		my_bag_of_word.append(element)
print(my_bag_of_word)

# ans d

# q11

my_string = "It's rainning cats and dogs "
results = my_string.count('s')

print(results)


# ans 3

# q12
def my_function( x ):
	for i in range(x):
		for j in range(x):
			if i == j:
				print("1 ", end = " ")
			else:
				print("0 ", end = " ")
		print()


my_function(3)


# q13
def my_function( y ):
	var = 1
	while (y > 1):
		var = var * y
		y = y - 1
	return var


print(my_function(3))

# res 6

# q14
even_numbers = [x for x in range(3, 12) if x % 3 == 0]

print(even_numbers)
# res c

# q15
x = [[1, 1, 2],
     [3, 51, 99],
     [5, 81, 23]]

result = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
for i in range(len(x)):
	for j in range(len(x[0])):
		result[j][i] = x[i][j]
for r in result:
	print(r)


# res a
# lật mặt với việc giữ nguyên đường chéo 1,51,23

# q16

def my_function( my_data ):
	rs = 0
	for i in my_data:
		rs += i
	return rs


my_list = [2, 3, 4, 5]
print(my_function(my_data = my_list))


# q17
def my_function( my_data ):
	result = []
	for element in my_data:
		if element not in result:
			result.append(element)
	return result


data = [{'friend': ['Tom', 'Mike', 'Taylor']}, 2002, 2099, 3000, 'moon']

print(my_function(data))


# list của python có thể nhận đa dạng kiểu dữ liệu trong một list


# q18
def my_function( data, max, min ):
	result = []
	for i in data:
		if i < min:
			result.append(min)
		elif i > max:
			result.append(max)
		else:
			result.append(i)
	return result


my_list = [1, 2, 3, 4, 5, 6, 7]
max = 5
min = 2
print(my_function(max = max, min = min, data = my_list))


# biến những số nhỏ hơn min -> min , những số lớn hơn max -> max
# res c

# q19

def my_function( x, y ):
	x.extend(y)
	return x


list_num1 = [-1, -4, -9]
list_num2 = [2, 3, 5]
list_num3 = [0, 0, 0]

my_function(list_num1, my_function(list_num2, list_num3))


# extend một list  => += list
# res a

# q20

def check_the_number( N ):
	list_of_numbers = []
	result = ""
	for i in range(1, 10, 3):
		list_of_numbers.append(i)
	if N in list_of_numbers:
		results = "True"
	if N not in list_of_numbers:
		results = "False"
	return results


N = 0
N = + 5
print(N)
results = check_the_number(N)

print(results)

# res d

# q21

data = "['dog','cat',[1,2]]"
print(type(data))


# q22
def my_function( n ):
	x = n[0]
	for i in n:
		if i < x:
			x = i
	return x


my_list = [-7, 99, 100, 2, 0, -20]

my_function(my_list)

# tìm giá trị nhỏ nhất của danh sách
# res c

# q23
Ann = '@ThiS tEst is Very eaSy @@'
David = "i love iT!"
txt = Ann.strip('@').capitalize() + David.title()

print(txt)


# strip("ký tự cần loại bỏ ở hai đầu")
# capitalize viết hoa ký tự đầu tiên còn lại sẽ là ký tự thường
# title viết hoa ký tự đầu tiên của một chữ

# res a

# q24

def my_function( n ):
	x = n[0]
	for i in n:
		if i > x:
			x = i
	return x


my_list = [-200, -99, -100, -2004, 0, -20]
my_function(my_list)


# tìm giá tị lớn nhất của danh sách
# res c

# q25

def my_function( integers, number = -999 ):
	return any([True if i == number else False for i in integers])


my_list = [1, 3, 6, 9, -100, 19, 2004, 2023]
my_function(my_list, 2004)

# phương thức any trả về true với tồn tại ít nhất một phần tử  trong một danh sách, sẽ trả là false nếu danh sách rỗng
# res c


# q26

my_exam = "I do my      homework every evening!"
print(my_exam.strip('!').split())


# q27

def function_helper( x, data ):
	for i in data:
		if x == i:
			return 0
	return 1


def a_function( data ):
	res = []
	for i in data:
		if function_helper(i, res):
			res.append(i)

	return res


lst = [1, 1, 2, 2, 3]

print(a_function(lst))


# trả ra một danh sách gồm các phần tử không lặp
# res a

# q28

def my_function( signal1, signal2 ):
	var = False
	for s1 in signal1:
		for s2 in signal2:
			if s1 == s2:
				var = True
				return var


print(my_function([0, 1, 1, 0], [100, 11, 110]))


# không bao giờ chạy vào phần thân của câu lệnh if

# res d

# q29

def my_function( signal1, signal2 ):
	var = False
	for s1 in signal1:
		for s2 in signal2:
			if s1 == s2:
				var = True
				return var


print(my_function([0, 1, 1, 9], [9, 9, 9]))


# res b


# q30
def my_function( data ):
	var = []
	for i in data:
		if i % 2 == 0:
			var.append(i)
	return var


print(my_function([1, 2, -4, 5, 7, 23]))


# lấy những phần tử chia hết cho 2
# res d

# q31

def square( num ):
	'''
	return the square of the number entered.
	The number entered must be an integer
	'''
	return num ** 2


print(square.__doc__)


# in ra đoạn comment mặc định mô tả phương thức
# res e

# q32

def a_function( x ):
	res = ""
	for i in x:
		res = i + res
	return res


x = 'cat'

print(a_function(x))

# đảo ngược vị trí các ký tự trong một chuỗi
# res b

my_list = [1, 1, 2, 3, 5]
odd = 1
even = 0

for number in my_list:
	if number % 3 == 0:
		even += number
	else:
		odd += number
print(f"odd:{odd}, even:{even}")

# res c
