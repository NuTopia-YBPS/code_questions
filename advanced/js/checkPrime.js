function checkPrime(n) {
	for(i = 1; i < n; i++) {
		if (n % i == 0) {
			return true
		}
	}
	return false
}

console.log(checkPrime(3))