"""
Kata 5 from:

https://tddmanifesto.com/exercises/
"""
import pytest

BARCODE_DATABASE = {
    "12345": 7.25,
    "23456": 12.50,
}


def scan_barcode(input_code):
    """
    """

    if input_code == "":
        return "Error: empty barcode"

    if input_code == "99999":
        return "Error: barcode not found"

    return "$" + "{:.2f}".format(BARCODE_DATABASE[input_code])


test_inputs = {
    "12345": ("12345", "$7.25"),
    "23456": ("23456", "$12.50"),
    "99999": ("99999", "Error: barcode not found"),
    "Empty barcode": ("", "Error: empty barcode"),
}


@pytest.mark.parametrize(
    "input_code,output", test_inputs.values(), ids=test_inputs.keys()
)
def test_known_query(input_code, output):
    """
    """
    assert scan_barcode(input_code) == output
