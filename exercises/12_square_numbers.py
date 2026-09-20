def square_numbers(numbers: list) -> list:
    return [number ** 2 for number in numbers]

if __name__ == "__main__":
    assert square_numbers([1, 2, 3]) == [1, 4, 9]
    assert square_numbers([-3, 0, 2]) == [9, 0, 4]
    assert square_numbers([2, 2]) == [4, 4]
    assert square_numbers([]) == []

    original=[0,4,-7,15,3]
    copy_before=original.copy()
    assert square_numbers(original) == [0,16,49,225,9]
    assert original == copy_before

    original = [0, 1]
    result = square_numbers(original)
    assert result is not original

#Работает :)
