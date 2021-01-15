from sympy import divisors
for i in range(190201, 190280):
	if len(list(filter(lambda item: item % 2 == 0, divisors(i)))) == 4:
		print([i for i in divisors(i) if i % 2 == 0])
