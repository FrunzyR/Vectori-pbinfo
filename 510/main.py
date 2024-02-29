from math import sqrt


def read():
    _ = int(input())
    number_line = input().split()
    return [int(x) for x in number_line]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def verify(lista):
    new_list =[]
    for element in lista:
        if is_prime(element):
            new_list.append(element)
    return new_list


def sort(lista):
    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] >= lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
    return " ".join(map(str, lista))


if __name__ == "__main__":
    a = read()
    b = verify(a)
    c = sort(b)
    print(c)
    