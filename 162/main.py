def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def movement(lista, offset):
    moved_list = []
    list_length = len(lista)
    for i in range(list_length):
        offseted_number = str(lista[(i + offset) % list_length])
        moved_list.append(offseted_number)

    return " ".join(moved_list)


def solve(lista):
    for offset in range(len(lista)):
        print(movement(lista, offset))


if __name__ == "__main__":
    a = read()
    solve(a)
    