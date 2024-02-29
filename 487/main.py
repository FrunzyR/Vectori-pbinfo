def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def solve(lista):
    cont = 0
    suma = sum(lista)
    ma = suma / len(lista)

    for i in lista:
        if i > ma:
            cont += 1
    return cont


if __name__ == "__main__":
    a = read()
    print(solve(a))
    