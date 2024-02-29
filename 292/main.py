def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def multiplu(lista):
    for element in lista:
        if element % lista[-1] == 0:
            continue
        else:
            return False
    return True


def solve(lista):
    if multiplu(lista):
        print("DA")
    else:
        print("NU")


if __name__ == "__main__":
    a = read()
    solve(a)

