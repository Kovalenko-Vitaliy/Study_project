def running_totals(numbers: list[int]) -> list[int]:
    totals: list[int] = []
    total=0

    for number in numbers:
        total+=number
        totals.append(total)

    return totals

if __name__ == "__main__":
    assert running_totals([1, 2, 3]) == [1, 3, 6]
    assert running_totals([3, -5, 2]) == [3, -2, 0]
    assert running_totals([0, 0]) == [0, 0]
    assert running_totals([]) == []
    original = [5]
    result = running_totals(original)
    assert result == [5]
    assert result is not original
    result.append(9)
    assert original == [5]

    assert running_totals([10, -3, -2, 5]) == [10, 7, 5, 10]

# Работает :)
