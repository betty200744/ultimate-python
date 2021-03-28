# CustomError
class CustomError(Exception):
    """"""


# DivisionError
class DivisionError(CustomError):
    """"""


def divide_number(dividend, divisor):
    if dividend <= 0:
        raise DivisionError(f"Non-positive dividend: {dividend}")
    if divisor <= 0:
        raise DivisionError(f"Non-positive divisor: {divisor}")
    return dividend // divisor


def main():
    print("main")
    for dividend, divisor in [[0, 1], [1, 0]]:
        division_failed = False
        try:
            divide_number(dividend, divisor)
        except DivisionError as e:
            division_failed = True
            assert str(e).startswith("Non-positive")
        assert division_failed is True
    print(divide_number(10, 2))


if __name__ == '__main__':
    main()
