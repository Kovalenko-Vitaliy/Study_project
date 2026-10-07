def find_index(items: list[str], target: str) -> int | None:
    for index, item in enumerate(items):
        if item == target:
            return index
    return None


if __name__ == "__main__":
    assert find_index(["a", "b", "a"], "a") == 0
    assert find_index(["a", "b", "a"], "b") == 1
    assert find_index(["A", "a"], "a") == 1
    assert find_index(["", "x"], "") == 0
    assert find_index(["a"], "missing") is None
    assert find_index([], "a") is None
    original = [" a ", "a"]
    assert find_index(original, "a") == 1
    assert original == [" a ", "a"]

    assert find_index(["Assert", "Find index", "Is None"], "Is None") == 2

# Работает:)
