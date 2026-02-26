for a in range(1, 500):
    for b in range(a + 1, 500):   
        c = (a**2 + b**2) ** 0.5
        if c.is_integer() and a + b + int(c) == 1000:
            c = int(c)
            print(a, b, c, "=>", a * b * c)
