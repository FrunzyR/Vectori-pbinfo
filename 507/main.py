def read():
    n = int(input())
    x = list(map(int, input().split()))
    m = int(input())
    y = list(map(int, input().split()))
    return x, y


def verify(b, x):
    for c in x:
        if b == c:
            return True
    return False


def solve(lista):
    result = []
    for b in lista[1]:
        if verify(b, lista[0]):
            result.append(1)
        else:
            result.append(0)
    return result


if __name__ == "__main__":
    vectors = read()
    result = solve(vectors)
    print(" ".join(map(str, result)))
