numbers = []
for i in range(0, 1000):
    if i % 3 == 0 or i % 5 == 0:
        numbers.append(i)

print(sum(numbers))