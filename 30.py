print(sum(n for n in range(2, 6*9**5 + 1)
    if n == sum(int(d)**5 for d in str(n))))
