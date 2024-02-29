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


def solve(lista):
    return " ".join([str(x) for x in lista if not is_prime(x)])


if __name__ == "__main__":
    a = read()
    solution = solve(a)
    if solution != '':
        print(solution)
