a = []
for i in range(10):
    a.append(int(input()))

print(str(a[9] + a[8] + sum(a[:8]) / 2) + "00000")