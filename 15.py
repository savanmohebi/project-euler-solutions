from math import comb

def lattice_paths(n, m=None):
    if m is None: 
        m = n
    return comb(n + m, n)

print(lattice_paths(20))


