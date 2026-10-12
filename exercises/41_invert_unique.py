def invert_unique(data:dict[str,int]) -> dict[int,str]:
    return {value:key for key, value in data.items()}

if __name__ == "__main__":
    assert invert_unique({"a": 1, "b": 2}) == {1: "a", 2: "b"}
    assert invert_unique({"zero": 0, "minus": -3}) == {0: "zero", -3: "minus"}
    assert invert_unique({"": 7}) == {7: ""}
    assert invert_unique({}) == {}
    original = {"x": 4}
    result = invert_unique(original)
    assert result == {4: "x"}
    assert result is not original
    assert original == {"x": 4}

    assert invert_unique({"issue": 41, "next":42}) == {41: "issue", 42: "next"}

# Работает :)