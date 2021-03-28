def main():
    total = 0
    for i in range(5):
        total += i
    assert total == 10
    i = 0
    while i < 8:
        i += 2
    assert i == 8

    for j in range(5, 0, -1):
        print(j)


if __name__ == '__main__':
    main()
