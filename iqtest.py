def iq_test(numbers):
    z = numbers.split()
    odds = []
    evens = []
    for x in z:
        if int(x) % 2 != 0:
            j = z.index(x)
            odds.append(j + 1)
        elif int(x) % 2 == 0:
            j = z.index(x)
            evens.append(j + 1)
    g = len(odds)
    h = len(evens)
    if g < h:
        return (odds[0])
    else:
        return (evens[0])
