def main():
    a = 1
    b = 2.0
    c = True
    d = "hello"
    # type
    type_a = type(a)
    type_b = type(b)
    type_c = type(c)
    type_d = type(d)
    assert type_a is int
    assert type_b is float
    assert type_c is bool
    assert type_d is str
    #  print
    print(a)
    print(b)
    print(c)
    print(d)
    # everything is object in python
    assert isinstance(type_a, object) and isinstance(a, object)
    assert isinstance(type_b, object) and isinstance(b, object)
    assert isinstance(type_c, object) and isinstance(c, object)
    assert isinstance(type_d, object) and isinstance(d, object)


if __name__ == "__main__":
    main()
