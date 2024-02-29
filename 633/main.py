def citire():
    n = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def rezolvare(lista):
    par = 0
    impar = 0
    for i in lista:
        if is_even(i):
            par += 1
        else:
            impar += 1
    dif = par - impar

    if dif < 0:
        return dif * -1
    return dif


def is_even(number):
    return number % 2 == 0


if __name__ == "__main__":
    a = citire()
    print(rezolvare(a))
    