number = int(input())

for i in range(number):
    yazi = input()
    yeniyazi = ""
    for harf in yazi:
        harf = harf.lower()
        if (harf == 'a') or (harf == 'e') or (harf == 'u') or (harf == 'i') or (harf == 'o'):
            yeniyazi += "AA"
        else:
            yeniyazi += harf
    print(yeniyazi)