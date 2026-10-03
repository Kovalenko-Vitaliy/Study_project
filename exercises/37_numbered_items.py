def numbered_items(items: list[str]) -> list[tuple[int, str]]:
    return [(number, item) for number, item in enumerate(items,start=1)]

if __name__ == "__main__":
    assert numbered_items(["кот", "пёс"]) == [(1, "кот"), (2, "пёс")]
    assert numbered_items(["x", "x"]) == [(1, "x"), (2, "x")]
    assert numbered_items([""]) == [(1, "")]
    assert numbered_items([]) == []
    original = ["a", "b"]
    result = numbered_items(original)
    assert result == [(1, "a"), (2, "b")]
    assert isinstance(result[0], tuple)
    assert original == ["a", "b"]

    assert numbered_items(["", "дом", "", "дом"])==[(1, ""), (2, "дом"), (3, ""), (4, "дом")]

# Работает :)
