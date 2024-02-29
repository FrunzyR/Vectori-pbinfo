def read():
    first_line = input().split()
    k = int(first_line[1])
    number_line = input().split()
    return k, [int(x) for x in number_line]


def sort_asc(lista):
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] >= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return " ".join(map(str, lista))


def sort_desc(lista):
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] <= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return " ".join(map(str, lista))


if __name__ == "__main__":
    k, a = read()

    print(sort_asc(a[:k]) + ' ' + sort_desc(a[k:]))
    