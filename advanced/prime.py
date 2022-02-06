
def check_prime(n):
    for i in range(1,n):
        if i % n == 0:
            return True
    return False

if __name__ == "__main__":
	print(check_prime(2))