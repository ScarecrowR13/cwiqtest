def iq_test(numbers):
    z = numbers.split()
    odds = []
    evens = []
    for x in z:
        if x % 2 != 0:
            j = z.index(x)
            odds.append(j + 1)
        elif x % 2 == 0:
            j = z.index(x)
            evens.append(j + 1)
    g = len(odds)
    h = len(evens)
    if g < h:
        return (odds[0])
    else:
        return (evens[0])

iq_test("2 4 7 8 10")
