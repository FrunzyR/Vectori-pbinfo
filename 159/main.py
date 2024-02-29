def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def solve(lista):
    new_list = []

    for element in lista:
        new_list.append(str(element))
        if element % 2 == 0:
            new_list.append(str(element*2))

    return " ".join(new_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))
