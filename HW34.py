from sympy import divisors

cashe = [{len(divisors(i)): i} for i in range(586132, 586430)]

cashe.sort(key = lambda item: list(item.keys())[0])

majorNumberDivisors = list(cashe[-3].keys())[0]
majorNumber = cashe[-3][majorNumberDivisors]

minorNumberDivisors = list(cashe[-1].keys())[0]
minorNumber = cashe[-1][minorNumberDivisors]

print(majorNumberDivisors, majorNumber, majorNumber // divisors(majorNumber)[1])

print(minorNumberDivisors, minorNumber, minorNumber // divisors(minorNumber)[1])
