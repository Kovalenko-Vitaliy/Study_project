def is_leap_year(year: int) -> bool:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    return False

if __name__ == "__main__":
    assert is_leap_year(2024) is True
    assert is_leap_year(2023) is False
    assert is_leap_year(2000) is True
    assert is_leap_year(1900) is False
    assert is_leap_year(2100) is False
    assert is_leap_year(2400) is True

    assert is_leap_year(1999) is False
    assert is_leap_year(2001) is True
    assert is_leap_year(2002) is False
    assert is_leap_year(2003) is True

#Работает :)
