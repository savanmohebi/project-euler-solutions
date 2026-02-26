def isprime(n):
    totalprime = 0
    for k in range(2, n):  
        is_prime = True
        for i in range(2, int(k**0.5) + 1):
            if k % i == 0:   
                is_prime = False
                break
        if is_prime:
            totalprime += k
    print(totalprime)
n = int(input("Enter a number: "))
isprime(n)
