def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def alternativ(lista):
    for i in range(1, len(lista)):
        if lista[i] == 0 or lista[i-1] == 0:
            continue
        else:
            return False
    return True


def solve(lista):
    for element in lista:
        if alternativ(lista):
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
        