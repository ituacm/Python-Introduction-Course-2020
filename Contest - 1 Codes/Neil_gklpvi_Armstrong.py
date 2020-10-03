a = int(input())
armstrong = 0

if a < 10:
    armstrong = a
elif a < 100:
    birler = a % 10
    onlar = a//10
    armstrong = (birler ** 2) + (onlar ** 2)
else:
    birler = a % 10
    onlar = ((a % 100) - birler) // 10
    yuzler = (a - birler - (onlar * 10)) // 100
    armstrong = (birler ** 3) + (onlar ** 3) + (yuzler ** 3)

if armstrong == a:
    print("YES")
else:
    print("NO")