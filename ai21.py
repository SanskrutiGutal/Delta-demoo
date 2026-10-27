from itertools import permutations

letters = "SENDMORY"
digits = range(10)

for values in permutations(digits, len(letters)):
    d = dict(zip(letters, values))

    if d['S'] == 0 or d['M'] == 0:
        continue

    SEND = 1000*d['S'] + 100*d['E'] + 10*d['N'] + d['D']
    MORE = 1000*d['M'] + 100*d['O'] + 10*d['R'] + d['E']
    MONEY = (
        10000*d['M'] + 1000*d['O'] +
        100*d['N'] + 10*d['E'] + d['Y']
    )

    if SEND + MORE == MONEY:
        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        print("Letter assignments:", d)
        break