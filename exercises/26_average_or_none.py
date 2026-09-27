def average_or_none(numbers: list) -> float|None:
    return sum(numbers) / len(numbers) if numbers else None

if __name__ == "__main__":
    from math import isclose

    assert average_or_none([2, 4, 6]) == 4.0
    assert isinstance(average_or_none([2, 4, 6]), float)
    assert average_or_none([-4, 2]) == -1.0
    assert average_or_none([0]) == 0.0
    assert average_or_none([]) is None
    assert isclose(average_or_none([1, 0, 0]), 1 / 3)
    original = [2, 5]
    assert average_or_none(original) == 3.5
    assert original == [2, 5]

    assert average_or_none([3, 7, 11]) == 7

#Работает :)
