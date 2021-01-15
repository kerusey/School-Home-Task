from sympy import divisors

for i in range(251811, 251826):
	if len(divisors(i)) == 4:
		print(i)
