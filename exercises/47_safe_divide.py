def safe_divide(a:int, b:int)->int|None:
    try:
        return a / b
    except ZeroDivisionError:
        return None



if __name__ == "__main__":
    assert safe_divide(6, 3) == 2.0
    assert isinstance(safe_divide(6, 3), float)
    assert safe_divide(5, 2) == 2.5
    assert safe_divide(-6, 3) == -2.0
    assert safe_divide(0, 5) == 0.0
    assert safe_divide(1, 0) is None
    assert safe_divide(0, 0) is None

    assert safe_divide(1, 0) is None
    assert safe_divide(7, 2) == 3.5

# Работает :)
