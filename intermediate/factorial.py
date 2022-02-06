def factorial(n):
	num = 1
	for i in range(n):
		num *= i
	return num

if __name__ == "__main__":
	print(factorial(10))