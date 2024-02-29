def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def verify(lista):
    if len(lista) < 2:
        return False

    for i in range(len(lista) //2 ):
        first_el = lista[i]
        second_el = lista[-(i+1)]

        if first_el % 2 != second_el % 2:
            return False

    return True


def solve(lista):
    for element in lista:
        if verify(lista):
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    a = read()
    if solve(a):
        print("DA")
    else:
        print("NU")
        