def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def div(element):
    return element % 10 == 0


def add_element(lista):
    new_list = []
    for element in lista:
        if div(element):
            new_list.append(element)
    return new_list


def sort(lista):
    for i in range(len(lista)):
        for j in range(i + 1, len(lista)):
            if lista[i] <= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return " ".join(map(str, lista))


if __name__ == "__main__":
    a = read()
    b = add_element(a)
    if not b:
        print("NU EXISTA")
    else:
        c = sort(b)
        print(c)
        