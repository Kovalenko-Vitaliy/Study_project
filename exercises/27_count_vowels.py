def count_vowels(text:str)->int:
    vowels = {'a', 'e', 'i', 'o', 'u'}

    count = 0
    for char in text.lower():
        if char in vowels:
            count += 1

    return count

if __name__ == "__main__":
    assert count_vowels("Hello") == 2
    assert count_vowels("AEIOU") == 5
    assert count_vowels("banana") == 3
    assert count_vowels("sky") == 0
    assert count_vowels("АУ 123!") == 0
    assert count_vowels("") == 0

    assert count_vowels("aAeEiIoOuU ПРИвет 123321") == 10

#Работает :)
