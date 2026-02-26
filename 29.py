AL = []
for a in range(2, 101):
    for b in range(2, 101):
        AL.extend((a**b, b**a))  

unique = set(AL)            
print(len(unique))          
