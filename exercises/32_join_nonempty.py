def join_nonempty(text:list[str]) -> str:
    return ", ".join(word for words in text if (word := words.strip()))

if __name__ == "__main__":
    assert join_nonempty([" Москва ", "", " Казань "]) == "Москва, Казань"
    assert join_nonempty(["a", "a"]) == "a, a"
    assert join_nonempty([" a  b ", " c "]) == "a  b, c"
    assert join_nonempty([" ", "\t"]) == ""
    assert join_nonempty([]) == ""
    original = [" x ", "", "y"]
    assert join_nonempty(original) == "x, y"
    assert original == [" x ", "", "y"]

    assert join_nonempty(["    Виталий решает задачу      ","   №32"]) == "Виталий решает задачу, №32"

#Работает :)
