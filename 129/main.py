def read():
    with open("sortare.in", "r") as file:
        _ = file.readline()
        number_line = file.readline().split()
        return [int(x) for x in number_line]


def sort_desc(lista):
    for i in range(0, len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] <= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return lista


def my_print(output):
    with open("sortare.out", "w") as file:
        string_list = [str(z) for z in output]
        file.write(" ".join(string_list))


if __name__ == "__main__":
    a = read()
    my_print(sort_desc(a))
    