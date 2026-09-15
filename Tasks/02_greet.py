def greet (name:str=""):
    if name!="":
        return f"Привет, {name}!"
    else:
        return f"Привет!"
if __name__ == "__main__":
    assert greet("Виталий") == "Привет, Виталий!"
    assert greet("Анна") == "Привет, Анна!"
    assert greet("") == "Привет!"

#Работает :)
