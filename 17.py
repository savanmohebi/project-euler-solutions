ones={0:0,1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8}
tens={20:6,30:6,40:5,50:5,60:5,70:7,80:6,90:6}

def letters(n):
    if n==1000:return 11
    h,r=divmod(n,100)
    s=0
    if h:
        s+=ones[h]+7
        if r:s+=3
    if r:
        if r<20:s+=ones[r]
        else:s+=tens[(r//10)*10]+ones[r%10]
    return s

print(sum(letters(i) for i in range(1,1001)))


