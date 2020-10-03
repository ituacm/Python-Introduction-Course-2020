n = int(input())
len = 2 * n - 1

for i in range(len):
    for j in range(len):
        mn = i if i < j else j
        mn = len - i - 1 if mn >= len - i else mn
        mn = min(len - j - 1, mn)
        print(n - mn, end=" ")
    print()
