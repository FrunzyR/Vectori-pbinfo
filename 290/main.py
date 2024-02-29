def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def even(lista):
    new_list = [element for element in lista if element % 2 == 0]
    return new_list


def solve(new_list):
    for i in range(1, len(new_list)):
        if new_list[i-1] <= new_list[i]:
            continue
        else:
            return False
    return True


if __name__ == "__main__":
    a = read()
    b = even(a)
    if solve(b):
        print("DA")
    else:
        print("NU")
        