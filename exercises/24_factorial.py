def factorial(n:int)->int:
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

if __name__ == "__main__":
    assert factorial(0) == 1
    assert factorial(1) == 1
    assert factorial(3) == 6
    assert factorial(5) == 120
    assert factorial(7) == 5040

    assert factorial(10) == 3628800

#Работает :)