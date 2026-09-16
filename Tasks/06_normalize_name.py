def normalize_name(name):
    return name.strip().lower()


if __name__ == "__main__":
    assert normalize_name("  ВИТАЛИЙ  ") == "виталий"
    assert normalize_name("Анна Мария") == "анна мария"
    assert normalize_name("  Анна  Мария  ") == "анна  мария"
    assert normalize_name("   ") == ""
    assert normalize_name("") == ""

    assert normalize_name("   ИМя ")=="имя"

#Работает :)
