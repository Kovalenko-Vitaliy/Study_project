def number_sign(number):
    if number>0:
        return "positive"
    if number<0:
        return "negative"
    else:
        return "zero"
    


if __name__ == "__main__":
    assert number_sign(5) == "positive"
    assert number_sign(-8) == "negative"
    assert number_sign(0) == "zero"

    assert number_sign(1) == "positive"

#Работает :)
