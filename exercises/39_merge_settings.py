def merge_settings(base:dict[str,int], overrides:dict[str,int]) -> dict[str,int]:
    merged=base.copy()
    merged.update(overrides)
    return merged

if __name__ == "__main__":
    assert merge_settings({"port": 8000}, {"port": 9000, "timeout": 5}) == {"port": 9000, "timeout": 5}
    assert merge_settings({"retries": 3}, {"retries": 0}) == {"retries": 0}
    assert merge_settings({}, {}) == {}
    base, overrides = {"a": 1}, {"b": 2}
    result = merge_settings(base, overrides)
    assert result == {"a": 1, "b": 2}
    assert result is not base and result is not overrides
    result["a"] = 99
    assert base == {"a": 1} and overrides == {"b": 2}

    assert merge_settings({"issue": 39, "return": 39},{"return":0}) == {"issue": 39, "return": 0}

# Работает :)
