def append_to_copy(numbers: list[int], value: int) -> list[int]:
    return numbers + [value]

if __name__ == "__main__":
    numbers = [1, 2]
    result = append_to_copy(numbers, 3)
    assert result == [1, 2, 3]
    assert numbers == [1, 2]
    assert result is not numbers
    result.append(4)
    assert numbers == [1, 2]
    assert append_to_copy([], 7) == [7]
    assert append_to_copy([2], 2) == [2, 2]

    original = [-1, 0, -3]
    copy_before = original.copy()
    appended = append_to_copy(original, 2)
    assert appended == [-1, 0, -3, 2]
    assert original == copy_before
    assert appended is not original

#Работает :)