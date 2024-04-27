# Day 22

# Bài tập về sự ngẫu nhiên - dùng vòng lặp while

import random


def random_number_with_condition( total ):
	random.seed(0)
	count = 0
	isStart = True
	result = 0
	while isStart:
		count += 1
		a = random.randint(1, 20)
		b = random.randint(1, 20)
		result = a + b
		if result == total:
			isStart = False

	return count


print(random_number_with_condition(40))
print(random_number_with_condition(20))
print(random_number_with_condition(35))


# Cài đặt hàm find_divisible_number(a) tìm số nguyên dương nhỏ nhất lớn hơn 100 và chia hết cho số nguyên dương a


def find_divisible_number( a ):
	start = 100

	while True:
		start += 1
		if start % a == 0:
			break
	return start


print(find_divisible_number(5))
print(find_divisible_number(17))

# Cài đặt hàm find_squared_root(a) tìm căn bậc hai cho một số a bất kì với e=0.001

import math


def find_squared_root( a ):
	EPSILON = 0.001
	x = a
	while True:
		if abs(((math.pow(x, 2) - a) / (2 * x))) < EPSILON:
			break
		x = x - ((math.pow(x, 2) - a) / (2 * x))
	return x


print(f"- Test case 1: find_squared_root(2)-> {find_squared_root(2)} ")
print(f"- Test case 1: find_squared_root(3)-> {find_squared_root(3)} ")
