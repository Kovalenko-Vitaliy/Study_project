import itertools


def flatten_once(numbers: list[list[int]]) -> list[int]:
    return [num for sublist in numbers for num in sublist]

if __name__ == "__main__":
    assert flatten_once([[1, 2], [3], [4, 5]]) == [1, 2, 3, 4, 5]
    assert flatten_once([[], [0, -1], []]) == [0, -1]
    assert flatten_once([[2], [2]]) == [2, 2]
    assert flatten_once([[], []]) == []
    assert flatten_once([]) == []
    original = [[1, 2], [3]]
    before = [group.copy() for group in original]
    result = flatten_once(original)
    assert result == [1, 2, 3]
    assert result is not original[0]
    result.append(4)
    assert original == before

    assert flatten_once([[10], [], [20, -30], [10]]) == [10, 20, -30, 10]

# Работает :)
