def digit_sum(number: int) -> int:
    return sum(int(digit) for digit in str(abs(number)))

if __name__ == "__main__":
    assert digit_sum(123) == 6
    assert digit_sum(-405) == 9
    assert digit_sum(1000) == 1
    assert digit_sum(9) == 9
    assert digit_sum(0) == 0

    assert digit_sum(-9999) == 36

#Работает :)
