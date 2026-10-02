def pairwise_sums(first: list[int], second: list[int]) -> list[int]:
    result = []
    for a, b in zip(first, second):
        result.append(a + b)
    return result


if __name__ == "__main__":
    assert pairwise_sums([1, 2, 3], [10, 20, 30]) == [11, 22, 33]
    assert pairwise_sums([1, 2, 3], [10]) == [11]
    assert pairwise_sums([1], [10, 20]) == [11]
    assert pairwise_sums([], [1]) == []
    assert pairwise_sums([1], []) == []
    first, second = [-2, 0], [2, 5]
    result = pairwise_sums(first, second)
    assert result == [0, 5]
    assert result is not first and result is not second
    assert first == [-2, 0] and second == [2, 5]

    assert pairwise_sums([100, -50, 7], [1, 2, 3, 4, 5]) == [101, -48, 10]

# Работает :)
