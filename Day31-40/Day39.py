# Day 39

def is_prime( n: int ) -> bool:
	if n <= 1:
		return False
	else:
		for i in range(2, int(n ** 0.5 + 1)):
			if n % i == 0:
				return False
		return True


print(is_prime(2))
print(is_prime(10))
print(is_prime(432))
print(is_prime(13))
