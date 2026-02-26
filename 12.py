"""lastnumber = 1
num = 1

def divisorcounter(number):
    divisor = 0
    for i in range(1, number + 1):
        if number % i == 0:
            divisor += 1
    return divisor   

while True:
    divisors = divisorcounter(lastnumber)
    if divisors > 5000:       
        break
    num += 1
    lastnumber += num   
print("First triangular number with more than 5 divisors is:", lastnumber)"""

#it hink this one is better : 
import math

lastnumber = 1
num = 1

def divisorcounter(n):
    if n == 1:
        return 1
    cnt = 0
    r = int(math.isqrt(n))
    for i in range(1, r + 1):
        if n % i == 0:
            cnt += 2
    if r * r == n:
        cnt -= 1
    return cnt

while True:
    divisors = divisorcounter(lastnumber)
    if divisors > 500:
        break
    num += 1
    lastnumber += num

print("First triangular number with more than 500 divisors is:", lastnumber)

