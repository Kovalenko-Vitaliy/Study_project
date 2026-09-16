def count_words(text:str):
    return len(text.split())

if __name__ == "__main__":
    assert count_words("Привет мир") == 2
    assert count_words("  один   два  ") == 2
    assert count_words("один\tдва\nтри") == 3
    assert count_words("Привет, мир!") == 2
    assert count_words("   ") == 0
    assert count_words("") == 0

    assert count_words("Свой! Тестовый! Пример!") == 3

#Работает :)
