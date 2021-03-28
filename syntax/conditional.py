def main():
    x = 1
    y = x + 2
    ran_1 = False
    if y == 3:
        ran_1 = True
    assert ran_1 is True
    ran_2 = False
    if not y == 1:
        ran_2 = True
    assert ran_2 is True

    if y == 1:
        ran_3 = False
    else:
        ran_3 = True
    assert ran_3 is True


if __name__ == '__main__':
    main()
