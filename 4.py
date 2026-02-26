for i in range(999, 99, -1):
    pal = int(str(i) + str(i)[::-1])
    for d in range(990, 99, -11):   
        if pal % d == 0:
            other = pal // d
            if 100 <= other <= 999:
                print(pal, (d, other))
                exit()
