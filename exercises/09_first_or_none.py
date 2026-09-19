def first_or_none (numbers:list[int])->int|None:
    if numbers:
        return numbers[0]
    return None

if __name__ == "__main__":
    assert first_or_none([10, 20, 30]) == 10
    assert first_or_none([0, 5]) == 0
    assert first_or_none([-7]) == -7
    assert first_or_none([]) is None

    assert first_or_none([0]) ==0

    numbers = [0, 5]
    before = numbers.copy()
    assert first_or_none(numbers) == 0
    assert numbers == before

#Работает :)
