def absolute_difference(a:int, b:int) -> int:
    return abs(a-b)

if __name__ == "__main__":
    assert absolute_difference(3, 8) == 5
    assert absolute_difference(8, 3) == 5
    assert absolute_difference(-3, 4) == 7
    assert absolute_difference(-7, -2) == 5
    assert absolute_difference(5, 5) == 0
    assert absolute_difference(0, 0) == 0

    assert absolute_difference(-7, 7) == 14

#Работает :)
