LIMIT = 28123
def sum_proper_divisors(n: int) -> int:
    if n < 2:
        return 0
    s = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            s += i
            j = n // i
            if j != i:
                s += j
        i += 1
    return s
abundants = [n for n in range(1, LIMIT + 1) if sum_proper_divisors(n) > n]
can = [False] * (LIMIT + 1)
for i in range(len(abundants)):
    for j in range(i, len(abundants)):
        s = abundants[i] + abundants[j]
        if s > LIMIT:
            break
        can[s] = True
result = sum(n for n in range(1, LIMIT + 1) if not can[n])
print(result) 
