def common_numbers(first:list[int], second:list[int]) -> list[int]:
    return sorted(list(set(first) & set(second)))


if __name__ == "__main__":
    assert common_numbers([3, 1, 2, 2], [2, 3, 4]) == [2, 3]
    assert common_numbers([1, 2], [3, 4]) == []
    assert common_numbers([2, 2], [2, 2]) == [2]
    assert common_numbers([], [1]) == []
    assert common_numbers([1], []) == []\

    original_first= [1, 2]
    original_second = [1, 2]
    copy_first = original_first.copy()
    copy_second = original_second.copy()

    result = common_numbers(original_first, original_second)

    assert result == [1, 2]
    assert original_first == copy_first
    assert original_second == copy_second
    assert result is not original_first
    assert result is not original_second

#Работает :)


