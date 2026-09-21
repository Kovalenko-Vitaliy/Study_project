def largest_or_none(numbers:list) -> int:
    if not numbers:
        return None
    return max(numbers)

if __name__ == "__main__":
    assert largest_or_none([3, 9, 2]) == 9
    assert largest_or_none([-5, -2, -10]) == -2
    assert largest_or_none([0]) == 0
    assert largest_or_none([4, 4]) == 4
    assert largest_or_none([]) is None

    original = [7,5,9,5,12,17,64,3,-21]
    copy_before=original.copy()
    assert largest_or_none(original) == 64
    assert copy_before == original

#Работает :)
