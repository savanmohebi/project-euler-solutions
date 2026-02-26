sumofsquare=0
sum=0
for i in range(1,101) :
    sum = sum + i 

squareofsum=sum*sum

for i in range(1,101):
    sumofsquare =  sumofsquare + i*i 

print(squareofsum-sumofsquare)