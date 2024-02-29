def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def sort(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] >= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return " ".join(map(str, lista))


if __name__ == "__main__":
    a = read()
    print(sort(a))
    