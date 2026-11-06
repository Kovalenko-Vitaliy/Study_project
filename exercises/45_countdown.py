def countdown(n: int):
    for i in range(n, -1, -1):
        yield i


if __name__ == "__main__":
    from types import GeneratorType

    assert isinstance(countdown(2), GeneratorType)
    assert list(countdown(3)) == [3, 2, 1, 0]
    assert list(countdown(0)) == [0]
    iterator = countdown(2)
    assert next(iterator) == 2
    assert next(iterator) == 1
    assert list(iterator) == [0]
    assert list(iterator) == []
    assert list(countdown(2)) == [2, 1, 0]

    assert list(countdown(5)) == [5, 4, 3, 2, 1, 0]

# Работает :)
