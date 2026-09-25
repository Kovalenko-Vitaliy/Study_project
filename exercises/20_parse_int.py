def parse_int(text:str)->int|None:
    try:
        return int(text)
    except ValueError:
        return None


if __name__ == "__main__":
    assert parse_int("42") == 42
    assert parse_int("-7") == -7
    assert parse_int(" 12 ") == 12
    assert parse_int("0") == 0
    assert parse_int("abc") is None
    assert parse_int("3.5") is None
    assert parse_int("") is None

    assert parse_int( " 1 2 " ) is None

#Работает :)
