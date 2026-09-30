def is_palindrome(text:str) -> bool:
    normalized = text.lower()
    return normalized == normalized[::-1]

if __name__ == "__main__":
    assert is_palindrome("Abba") is True
    assert is_palindrome("Топот") is True
    assert is_palindrome("python") is False
    assert is_palindrome("a a") is True
    assert is_palindrome(" abba") is False
    assert is_palindrome("x") is True
    assert is_palindrome("") is True

    assert is_palindrome("Flash") is False
    assert is_palindrome("dog") is False
    assert is_palindrome("cat123321tac") is True

    assert is_palindrome("ΣοΣ") is False
    assert is_palindrome("İaİ") is False

#Работает :)
