# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?

# num = 30
# prime_product = 1

# if num > 1:
# 	for i in range(2, num):
# 		if (num % 2 == 0):
# 			num *= i
# 			print i 

# print num 

# for i in range(1,29):
# 	for j in range(1, 29):
# 		if (num % num == 0 and num % i != 0):
# 			num *=

p = 100
n = 2
while (n * n) < p:
	while p % n == 0:
		p = p / n
	n += 1
print p

# first task to do - find prime numbers

# create an array of known_primes
known_primes = [2,3]
def is_prime(n):
	total_primes = len(known_primes)
	for i in range(0,total_primes):
		if(n % known_primes[i] == 0):
			# NOT PRIME!!
			return False
		else:
			# it might be prime, it might not.
			# its just not divisble by this number
			continue
	# each time the code spits out a prime number (not divisible by 2 or 3) add it to known list
	known_primes.append(n)
	return True
print is_prime(5)



























