def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result
number = int(input("Enter a number: "))
fact = factorial(number)
digits = [int(d) for d in str(fact)]
digit_sum = sum(digits)
print(digit_sum)
