def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def verify(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] == lista[j]:
                return False
    return True


def solve(lista):
    if verify(lista):
        print("DA")
    else:
        print("NU")


if __name__ == "__main__":
    a = read()
    solve(a)
    