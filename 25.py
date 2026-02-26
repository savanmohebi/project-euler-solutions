def fibonacci(n):
    a,b=1,1
    count=2
    while len(str(b)) < n :  
        a, b = b , a+b
        count+=1
    return b , count
val,index = fibonacci(1000)
print(val,index)



    