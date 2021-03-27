def main():
    list_words = ["cat", "dog", "horse", "cat"]
    tuple_word_len = tuple(len(list_words) for word in list_words)
    print(list_words)
    print(tuple_word_len)
    set_words = {word for word in list_words}
    print(set_words)


if __name__ == '__main__':
    main()
