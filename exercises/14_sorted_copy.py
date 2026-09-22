def sorted_copy(numbers: list[int]) -> list[int]:
    return sorted(numbers)


if __name__ == "__main__":
    numbers = [3, 1, 2, 1]
    result = sorted_copy(numbers)
    assert result == [1, 1, 2, 3]
    assert numbers == [3, 1, 2, 1]
    assert result is not numbers
    assert sorted_copy([-1, -3, 0]) == [-3, -1, 0]
    assert sorted_copy([]) == []

    original= [1,3,2,4,9,6,7]
    copy_before = original.copy()
    assert sorted_copy(original) == [1,2,3,4,6,7,9]
    assert original == copy_before
    assert sorted_copy(original) is not original

#Работает :)

