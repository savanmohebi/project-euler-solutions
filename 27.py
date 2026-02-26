def primefounder(x):
    if x < 2  : return False
    if x %2 == 0 : return x == 2
    for i in range (3,int(x**0.5)+1,2):
        if x % i == 0:
            return False
    return True
def  consecutive_prime_run(a: int, b: int) :
    n = 0
    while True:
        v = n*n + a*n + b
        if v < 2 or not primefounder(v):
            return n
        n+=1
best,besta,bestb=0,0,0
primebs=[b for b in range(1,1000+1) if primefounder(b)]
for a in range(-999,1000) :
    for b in primebs:
        run = consecutive_prime_run(a,b)
        if run > best :
            best = run
            besta = a
            bestb = b
print(best,besta,bestb)