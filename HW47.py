from sympy import isprime

cashe = [i for i in range(4730727, 4730817)]
for item in cashe:
	if isprime(item):
		print(item)
	