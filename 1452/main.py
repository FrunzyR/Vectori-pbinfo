def read():
    n, p = map(int, input().split())
    number_line = input().split()
    return n, p, [int(x) for x in number_line]


def solve(n, p, lista):
    new_list = []
    for i in range(1, len(lista)+1):
        if i != p:
            new_list.append(lista[i-1])
    return new_list


if __name__ == "__main__":
    n, p, a = read()
    result = solve(n, p, a)
    print(" ".join(map(str, result)))

