def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def solve(lista):
    new_list = [str(element) for element in lista if element % lista[-1] == 0]
    return " ".join(new_list)


if __name__ == "__main__":
    a = read()
    print(solve(a))

