from sympy import divisors

cashe = [{len(divisors(i)): i} for i in range(586132, 586430)]

cashe.sort(key = lambda item: list(item.keys())[0])

print(cashe) 