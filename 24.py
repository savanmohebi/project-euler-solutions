from itertools import permutations, islice
print(''.join(next(islice(permutations('0123456789'), 1_000_000-1, None))))
