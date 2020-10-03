n = int(input())
if n%2 == 1:
    print("Weird")
else:
    if 1<n<6:
        print("Not Weird")
    elif 5<n<21:
        print("Weird")
    else:
        print("Not Weird")