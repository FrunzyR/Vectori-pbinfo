def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def minim(lista):
    mini = lista[0]

    for element in lista:
        if element < mini:
            mini = element
    return mini


def solve(lista):
    new_list = []
    mini = minim(lista)

    for i in range(0, len(lista)):
        new_list.append(str(lista[i]))
        if lista[i] == mini:
            new_list.append(str(lista[i]))
    return " ".join(new_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))
    