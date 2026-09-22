def unique_numbers(numbers: list[int]) -> list[int]:
    return sorted(set(numbers))

if __name__ == "__main__":
    assert unique_numbers([3, 1, 3, 2, 1]) == [1, 2, 3]
    assert unique_numbers([5, 5, 5]) == [5]
    assert unique_numbers([0, -1, 0]) == [-1, 0]
    assert unique_numbers([]) == []

    original = [7, -2, 7, 0, -2]
    copy_before = original.copy()
    original_2=unique_numbers(original)
    assert original_2 == [-2, 0, 7]
    assert original == copy_before
    assert original_2 is not original

#Работает :)