def larger_number(a,b):
    if a>b:
        return a
    return b


if __name__ == "__main__":
    assert larger_number(2, 7) == 7
    assert larger_number(7, 2) == 7
    assert larger_number(4, 4) == 4
    assert larger_number(-5, -2) == -2

#Работает :)
