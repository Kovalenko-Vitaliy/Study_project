def longest_word(text:str) -> str:
    words = text.split()

    if not words:
        return None

    return max(words, key=len)


if __name__ == "__main__":
    assert longest_word("кот собака мышь") == "собака"
    assert longest_word("one two six") == "one"
    assert longest_word(" hi!  ok ") == "hi!"
    assert longest_word("a\tlong\nbb") == "long"
    assert longest_word("   ") is None
    assert longest_word("") is None

    assert longest_word("дом квартира   дача") == "квартира"

#Работает :)
