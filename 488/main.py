def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def solve(lista):
    indici_pari = []
    indici_impari = []
    for i in range(len(lista)):
        if (i + 1) % 2 == 0:
            indici_pari.append(str(lista[i]))
        else:
            indici_impari.append(str(lista[i]))

    indici_impari = reversed(indici_impari)
    return " ".join(indici_pari) + "\n" + " ".join(indici_impari)


if __name__ == "__main__":
    a = read()
    print(solve(a))
    