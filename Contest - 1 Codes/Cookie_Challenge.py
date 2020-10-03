b = int(input())
z = int(input())
r = int(input())
i = 1
while True:
    if b>=i:
        b-=i
        i+=1
    else:
        print("Berkay")
        break
    if z>=i:
        z-=i
        i+=1
    else:
        print("Zuafir")
        break
    if r>=i:
        r-=i
        i+=1
    else:
        print("Ruazir")
        break