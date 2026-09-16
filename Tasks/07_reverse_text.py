def reverse_text(text:str)->str:
    return text[::-1]


if __name__ == "__main__":
    assert reverse_text("python") == "nohtyp"
    assert reverse_text("кот") == "ток"
    assert reverse_text("a b") == "b a"
    assert reverse_text("a") == "a"
    assert reverse_text("") == ""

    assert reverse_text("primer") == "remirp"

#Работает :)
