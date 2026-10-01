def mask_phone(phone: str) -> str:
    if len(phone) <= 4:
        return phone
    return "*" * (len(phone) - 4) + phone[-4:]

if __name__ == "__main__":
    assert mask_phone("79991234567") == "*******4567"
    assert mask_phone("12345") == "*2345"
    assert mask_phone("0012") == "0012"
    assert mask_phone("123") == "123"
    assert mask_phone("") == ""

    assert mask_phone("70987654321") == "*******4321"

#Работает :)
