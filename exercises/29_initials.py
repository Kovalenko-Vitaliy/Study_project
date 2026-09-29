def initials(FIO: str) -> str:
    parts = FIO.split()
    result = ""
    for part in parts:
        result += part[0].upper() + "."

    return result

if __name__ == "__main__":
    assert initials("иван петров") == "И.П."
    assert initials("  Анна   Мария  Иванова ") == "А.М.И."
    assert initials("виталий") == "В."
    assert initials("анна-мария иванова") == "А.И."
    assert initials("иван\tпетров\nсергеевич") == "И.П.С."
    assert initials("   ") == ""
    assert initials("") == ""

    assert initials("Коваленко Виталий Игоревич") == "К.В.И."

#Работает :)
