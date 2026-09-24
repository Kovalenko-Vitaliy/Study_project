def get_username(user:dict[str, Any]) -> str:
    return user.get("name","Гость")

if __name__ == "__main__":
    assert get_username({"name": "Виталий"}) == "Виталий"
    assert get_username({"age": 20}) == "Гость"
    assert get_username({}) == "Гость"
    assert get_username({"name": ""}) == ""

    original = {"role":"admin","name":""}
    copy_before = original.copy()

    result = get_username(original)

    assert result == ""
    assert original == copy_before
    assert "name" in original

#Работает :)
