def add(x, y):
    return x + y


def sum_until(fn, n):
    total = 0
    for i in range(n):
        total += fn(i)
    return total


def main():
    add_result = add(1, 2)
    assert add_result == 3
    sum_result = sum_until(lambda i: i * 100, 5)
    assert sum_result == 1000


if __name__ == '__main__':
    main()
