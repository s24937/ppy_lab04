def prime(*liczby_pierwsze):
    for i in liczby_pierwsze:
        pierwsza = True
        if (i == 0 or i == 1 or i % 2 == 0) and i != 2:
            pierwsza = False
        for j in range(2, int(i)):
            if i % j == 0:
                pierwsza = False
        if pierwsza:
            odp = " is prime"
        else:
            odp = " is not prime"

        print(str(i) + odp)


prime(0, 1, 2, 3, 4, 5)
