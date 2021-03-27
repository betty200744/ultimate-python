"""
tuple are an ordered collection, cannot be modified at runtime
"""


def main():
    immutable = (1, 2, 3, 4)
    print(immutable[0])
    print(immutable[-1])
    print(immutable[:3])
    for i, num in enumerate(immutable):
        print(i, num)
    join_immutable = immutable + (5, 6)
    print(join_immutable)


if __name__ == '__main__':
    main()
