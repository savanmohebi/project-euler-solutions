def chain_counter(numb):
    chaincnt = 1   
    while numb != 1:
        if numb % 2 == 0:
            numb = numb // 2 
        else:
            numb = 3 * numb + 1
        chaincnt += 1
    return chaincnt
max_len = 0
max_num = 0
for i in range(1, 1_000_000):
    length = chain_counter(i)
    if length > max_len:
        max_len = length
        max_num = i

print(max_num)
print(max_len)
