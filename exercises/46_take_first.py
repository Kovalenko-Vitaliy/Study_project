from itertools import islice

def take_first (iterable, count: int) -> list[int]:
    return list(islice(iterable, count))


if __name__ == "__main__":
    from itertools import count

    assert take_first([1, 2, 3], 2) == [1, 2]
    assert take_first([1], 5) == [1]
    assert take_first([], 3) == []
    assert take_first((x * 2 for x in range(4)), 3) == [0, 2, 4]
    iterator = iter([10, 20, 30, 40])
    assert next(iterator) == 10
    assert take_first(iterator, 2) == [20, 30]
    assert next(iterator) == 40
    untouched = iter([7, 8])
    assert take_first(untouched, 0) == []
    assert next(untouched) == 7
    assert take_first(count(5), 3) == [5, 6, 7]
    original = [1, 2]
    result = take_first(original, 9)
    assert result == [1, 2] and result is not original
    assert original == [1, 2]


    gen=(x * 10 for x in range(5))
    assert take_first(gen, 2) ==[0, 10]
    assert take_first(gen, 1) == [20]

# Работает :)
