def is_even(number: int):
    if number==0:
        return True
    return number % 2 == 0

if __name__ == "__main__":
    assert is_even(4) is True
    assert is_even(7) is False
    assert is_even(0) is True
    assert is_even(-2) is True
    assert is_even(-3) is False

#Работает :)
