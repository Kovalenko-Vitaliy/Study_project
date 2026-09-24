def count_items(items: list[str]) -> dict[str, int]:
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

if __name__ == "__main__":
    assert count_items(["кот", "пёс", "кот"]) == {"кот": 2, "пёс": 1}
    assert count_items(["a", "a", "a"]) == {"a": 3}
    assert count_items(["Кот", "кот"]) == {"Кот": 1, "кот": 1}
    assert count_items(["", ""]) == {"": 2}
    assert count_items([]) == {}

    original = ["рыбка", "рыбка", "птичка", "рыбка"]
    copy_before = original.copy()
    result = count_items(original)
    assert result == {"рыбка" : 3, "птичка" :1}
    assert original == copy_before

#Работает :)
