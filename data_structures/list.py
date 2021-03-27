"""
List are a sequence of value, can be modified at runtime

"""


def main():
    letters = ["c", "b", "a"]
    print(letters[1:])
    print(letters[0:2])
    print(letters[:3])
    letters.reverse()
    print(letters)
    letters.sort()
    print(letters)
    letters.pop()
    print(letters)
    letters.append("d")
    print(letters)
    for letter in letters:
        print(letter)
        assert letter.isalpha()
    matrix = [[1, 2, 3], [4, 5, 6]]
    print(matrix)


if __name__ == '__main__':
    main()
