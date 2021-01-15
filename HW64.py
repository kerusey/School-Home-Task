from sympy import isprime

cashe = [i for i in range(2532000, 2532160) if isprime(i) and i % 10 == 7]

print(cashe[:5])