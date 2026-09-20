def only_positive(numbers: list) -> list:
    return [i for i in numbers if i > 0]

if __name__ == "__main__":
    assert only_positive([-2, 0, 3, 1, -5, 3]) == [3, 1, 3]
    assert only_positive([0, -1]) == []
    assert only_positive([2, 4]) == [2, 4]
    assert only_positive([]) == []

    original = [-2, 0, 3, 1, -5, 3]
    copy_before = original.copy()
    assert only_positive(original) == [3, 1, 3]
    assert original == copy_before

    original = [2, 4]
    result = only_positive(original)
    assert result is not original

# Работает :)
