def read_nonempty_lines(path:str) -> list[str]:

    result = []

    with open(path, encoding="utf-8") as file:
        for line in file:
            stripped = line.strip()
            if stripped:
                result.append(stripped)

    return result

if __name__ == "__main__":
    from pathlib import Path
    from tempfile import TemporaryDirectory

    with TemporaryDirectory() as folder:
        path = Path(folder) / "input.txt"
        text = "  Привет  \n\n мир \n  \nПривет\n"
        path.write_text(text, encoding="utf-8")
        assert read_nonempty_lines(str(path)) == ["Привет", "мир", "Привет"]
        assert path.read_text(encoding="utf-8") == text
        path.write_text(" a  b \n last", encoding="utf-8")
        assert read_nonempty_lines(str(path)) == ["a  b", "last"]
        path.write_text("  \n\t\n", encoding="utf-8")
        assert read_nonempty_lines(str(path)) == []
        path.write_text("", encoding="utf-8")
        assert read_nonempty_lines(str(path)) == []

        own_path = Path(folder)
        own_text = "  Один  \n\nДва   \n  Два  \nТри  три  три"
        path.write_text(own_text, encoding="utf-8")

        assert read_nonempty_lines(str(path)) == [
            "Один",
            "Два",
            "Два",
            "Три  три  три",
        ]

        assert path.read_text(encoding="utf-8") == own_text

#Работает:)
