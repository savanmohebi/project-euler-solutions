def D(number):
    sumd = 0
    for i in range(1, number):
        if number % i == 0:
            sumd += i
    return sumd
result = 0
for a in range(1, 10000):
    b = D(a)
    if b != a and D(b) == a:
        result += a

print(result)
