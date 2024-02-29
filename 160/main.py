from math import sqrt


def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def squared(element):
    if int(sqrt(element)) * int(sqrt(element)) == element:
        return True
    return False


def solve(lista):
    new_list = []
    for element in lista:
        if squared(element):
            new_list.append(str(int(sqrt(element))))
        new_list.append(str(element))
    return " ".join(new_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))
    