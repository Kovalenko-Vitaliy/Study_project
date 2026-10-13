def group_words_by_length(words: list[str]) -> dict[int, list[str]]:
    groups: dict[int, list[str]] = {}

    for word in words:
        length = len(word)

        if length not in groups:
            groups[length] = []
        groups[length].append(word)

    return groups

if __name__ == "__main__":
    assert group_words_by_length(["кот", "я", "дом", "мы"]) == {3: ["кот", "дом"], 1: ["я"], 2: ["мы"]}
    assert group_words_by_length(["", "a", ""]) == {0: ["", ""], 1: ["a"]}
    assert group_words_by_length(["aa", "aa"]) == {2: ["aa", "aa"]}
    assert group_words_by_length([]) == {}
    original = ["a", "bb"]
    result = group_words_by_length(original)
    second = group_words_by_length(original)
    result[1].append("z")
    assert second == {1: ["a"], 2: ["bb"]}
    assert original == ["a", "bb"]

    assert group_words_by_length(["issue", "42", "has", "been", "solved"]) == {
        5: ["issue"],
        2: ["42"],
        3: ["has"],
        4: ["been"],
        6: ["solved"]
    }

# Работает :)

