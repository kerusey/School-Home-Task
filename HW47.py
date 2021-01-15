from sympy import isprime

cashe = [i for i in range(4730727, 4730817)]
count = 1
for item in cashe:
	if isprime(item):
		print(count, item)
		count += 1
