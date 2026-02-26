ans = 1
primes = [2, 3, 5, 7, 11, 13, 17, 19]

for p in primes:
    pk = p
    while pk * p <= 20:  
        pk *= p
    ans *= pk

print(ans)  
