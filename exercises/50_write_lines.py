def write_lines(path:str, lines: list[str]) -> None:

    with open(path, "w", encoding="utf-8") as file:
        for line in lines:
            file.write(line + "\n")

    return None


if __name__ == "__main__":
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as folder:
        path = Path(folder) / "output.txt"
        original = ["Привет", "мир"]
        assert write_lines(str(path), original) is None
        assert path.read_text(encoding="utf-8") == "Привет\nмир\n"
        assert original == ["Привет", "мир"]
        write_lines(str(path), [" a ", "", "b"])
        assert path.read_text(encoding="utf-8") == " a \n\nb\n"
        write_lines(str(path), [])
        assert path.read_text(encoding="utf-8") == ""
        fresh = Path(folder) / "empty.txt"
        write_lines(str(fresh), [])
        assert fresh.is_file() and fresh.read_text(encoding="utf-8") == ""

        own_lines = ["Один", "Два"]
        assert write_lines(str(path), own_lines) is None
        assert path.read_text(encoding="utf-8") == "Один\nДва\n"
        assert own_lines == ["Один", "Два"]

#Работает :)
