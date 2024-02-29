def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def element_in_list(lista, element):
    for i in lista:
        if i == element:
            return True
    return False


def solve(lista):
    three_char_numbers = [x for x in lista if 100 <= x < 1000]
    new_list = []
    frequency = [0 for i in range(1000)]
    for element in three_char_numbers:
        frequency[element] = 1

    cont = 0
    for i in range(len(frequency) - 1, 0, -1):
        if cont == 2:
            break
        if frequency[i] == 0:
            new_list.append(i)
            cont += 1

    if cont != 2:
        return "NU EXISTA"

    return " ".join(map(str, reversed(new_list)))


if __name__ == "__main__":
    a = read()
    result = solve(a)
    print(result)
