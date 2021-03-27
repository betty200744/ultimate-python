"""
sets are an unordered collection of unique value, can be modified at runtime
"""


def main():
    set_one = {1, 2, 3}
    set_one.add(3)
    print(set_one)
    set_two = set()
    set_two.add(1)
    print(set_two)


if __name__ == '__main__':
    main()
