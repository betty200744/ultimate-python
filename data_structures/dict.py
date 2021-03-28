"""
dictionaries are a mapping of keys to values
"""


def main():
    review = {"title": "t", "price": 1, "content": "c"}
    print(len(review))
    print(review.values())
    print(review.keys())
    review.pop("title")
    print(review)
    print(review.get("price"))


if __name__ == '__main__':
    main()
