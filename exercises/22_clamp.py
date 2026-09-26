def clamp(number:int, lower:int, upper:int)->int:
    if number > upper:
        return upper
    if number < lower:
        return lower
    return number


if __name__ == "__main__":
    assert clamp(5, 1, 10) == 5
    assert clamp(-3, 1, 10) == 1
    assert clamp(15, 1, 10) == 10
    assert clamp(1, 1, 10) == 1
    assert clamp(10, 1, 10) == 10
    assert clamp(-4, -8, -2) == -4
    assert clamp(100, 7, 7) == 7

#Работает :)
