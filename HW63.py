from sympy import isprime

cashe = [i for i in range(2532000, 2532160) if isprime(i)]

print(cashe[:5])
