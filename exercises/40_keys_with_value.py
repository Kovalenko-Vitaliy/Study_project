def keys_with_value(dictionary: dict[str, int], target: int):
    result = []

    for key, value in dictionary.items():
        if value == target:
            result.append(key)

    return result

if __name__ == "__main__":
    assert keys_with_value({"a": 1, "b": 2, "c": 1}, 1) == ["a", "c"]
    assert keys_with_value({"z": 0, "a": 0}, 0) == ["z", "a"]
    assert keys_with_value({"x": -1}, -1) == ["x"]
    assert keys_with_value({"a": 1}, 3) == []
    assert keys_with_value({}, 0) == []
    original = {"x": 2, "y": 1}
    assert keys_with_value(original, 2) == ["x"]
    assert original == {"x": 2, "y": 1}

    assert keys_with_value({"a": 1, "b": 2}, 2) == ["b"]

#Работает :)
