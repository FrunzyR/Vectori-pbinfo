def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def solve(lista):
    new_list = []
    maxi = max(lista)
    mini = min(lista)

    min_index = lista.index(mini)
    max_index = lista.index(maxi)

    if min_index < max_index:
        for i in range(lista.index(mini), lista.index(maxi) + 1):
            new_list.append(str(lista[i]))
    else:
        for i in range(lista.index(maxi), lista.index(mini) + 1):
            new_list.append(str(lista[i]))
    return " ".join(new_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))
    