def remove_value(numbers:list[int], value:int) -> list[int]:
    return [number for number in numbers if number != value]

if __name__ == "__main__":
    assert remove_value([1, 2, 1, 3], 1) == [2, 3]
    assert remove_value([0, -1, 0], 0) == [-1]
    assert remove_value([2, 2], 2) == []
    assert remove_value([], 1) == []
    original = [3, 1, 3]
    result = remove_value(original, 9)
    assert result == [3, 1, 3]
    assert result is not original
    result.append(10)
    assert original == [3, 1, 3]

    assert remove_value([-5, 3, -5, 0, -5], -5) == [3, 0]

#Работает :)
