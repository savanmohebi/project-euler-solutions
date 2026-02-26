def prime_finder(n):
    factor = 2
    largest = 1
    while n > 1:
        if n % factor == 0:
            largest = factor
            n //= factor
        else:
            factor += 1
    return largest

x = int(input("Enter a number: "))
print(prime_finder(x))
