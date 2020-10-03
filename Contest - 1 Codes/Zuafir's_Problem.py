sira = int(input())

n = 1
toplam = 0
onceki1, onceki2 = 1, 1

while n <= sira:
    if n == 1:
        toplam += onceki1
    elif n == 2:
        toplam = onceki1 + onceki2
    else:
        onceki1 = onceki1 + onceki2
        onceki2 = onceki1 - onceki2
        toplam += onceki1

    n += 1

print(toplam)