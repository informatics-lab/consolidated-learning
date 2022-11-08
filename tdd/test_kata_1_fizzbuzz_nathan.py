## failing test
import pytest 


def return_number_as_string(number):
    if number%3 == 0 and number%5 == 0:
        return "FizzBuzz"
    if number%3 == 0:
        return "Fizz"
    if number%5 == 0:
        return "Buzz"
    return f'{number}'



@pytest.mark.parametrize(
    "given, expected",
    [
        (4, "4"),
        (3, "Fizz"),
        (5, "Buzz"),
        (15, "FizzBuzz")
    ]
)
def test_func(given, expected):
    result = return_number_as_string(given)
    assert result== expected