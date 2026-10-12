def have_same_items(first: list[int], second: list[int]) -> bool:
    return set(first) == set(second)



if __name__ == "__main__":
    assert have_same_items([1, 1, 2], [2, 1]) is True
    assert have_same_items([1, 2], [1, 2, 3]) is False
    assert have_same_items([0, -1], [-1, 0, 0]) is True
    assert have_same_items([], []) is True
    assert have_same_items([], [0]) is False
    first, second = [2, 1, 2], [1, 2]
    assert have_same_items(first, second) is True
    assert first == [2, 1, 2] and second == [1, 2]

    assert have_same_items([7, 7, 7, -3], [-3, 7, -3]) is True

# Работает :)
