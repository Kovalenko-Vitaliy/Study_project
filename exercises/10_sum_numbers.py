def sum_numbers(numbers: list) -> int:
    return sum(numbers)

if __name__ == "__main__":
    assert sum_numbers([1, 2, 3]) == 6
    assert sum_numbers([-2, 5, -3]) == 0
    assert sum_numbers([-3, -4]) == -7
    assert sum_numbers([7]) == 7
    assert sum_numbers([]) == 0

    assert sum_numbers([10,-10,5]) == 5

    numbers = [2, -1, 4]
    before = numbers.copy()
    assert sum_numbers(numbers) == 5
    assert numbers == before

#Работает :)
