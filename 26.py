def cycle_length(d):
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d == 1: return 0
    k, r = 1, 10 % d
    while r != 1:
        r = (r * 10) % d
        k += 1
    return k
best = max(range(2, 1000), key=cycle_length)
print(best, cycle_length(best))