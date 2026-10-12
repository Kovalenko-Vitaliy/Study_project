def only_in_first(first:list[int], second:list[int]) -> list[int]:
    return sorted(set(first) - set(second))

if __name__ == "__main__":
    assert only_in_first([3, 1, 3, 2], [2, 4]) == [1, 3]
    assert only_in_first([-2, 0, -2], [0]) == [-2]
    assert only_in_first([1, 2], [2, 1]) == []
    assert only_in_first([], [1]) == []
    assert only_in_first([2, 1, 2], []) == [1, 2]
    first, second = [3, 1], [1]
    assert only_in_first(first, second) == [3]
    assert first == [3, 1] and second == [1]

    assert only_in_first([10, 20, 30, 40, 50, 10], [20, 40]) == [10, 30, 50]

# Работает :)
