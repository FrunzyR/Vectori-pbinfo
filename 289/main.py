def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def even(lista):
    for element in lista:
        if element % 2 == 1:
            return True
    return False


def solve(lista):
    if even(lista):
        print("DA")
    else:
        print("NU")


if __name__ == "__main__":
    a = read()
    solve(a)
    