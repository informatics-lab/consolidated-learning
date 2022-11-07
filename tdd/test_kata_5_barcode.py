"""
Kata 5 from:

https://tddmanifesto.com/exercises/
"""
import pytest

BARCODE_DATABASE = {
    "12345": 7.25,
    "23456": 12.50,
}

ERROR_DATABASE = {
    "" : "Error: empty barcode",
    "99999": "Error: barcode not found"
}


def format_to_currency(total):
    return "$" + "{:.2f}".format(total)


def scan_barcode(input_code):
    """
    """
    if input_code in ERROR_DATABASE.keys():
        return ERROR_DATABASE[input_code]

    value = BARCODE_DATABASE[input_code]

    return format_to_currency(value)


end_to_end_test_inputs = {
    "12345": ("12345", "$7.25"),
    "23456": ("23456", "$12.50"),
    "99999": ("99999", "Error: barcode not found"),
    "Empty barcode": ("", "Error: empty barcode"),
}


@pytest.mark.parametrize(
    "input_code,output",
    end_to_end_test_inputs.values(),
    ids=end_to_end_test_inputs.keys(),
)
def test_known_query(input_code, output):
    """ Test a known query against the database of values.
    """
    assert scan_barcode(input_code) == output


format_test_inputs = {
    "2dp": (7.25, "$7.25"),
    "1dp": (12.5, "$12.50"),
}


@pytest.mark.parametrize(
    "input_number,output", format_test_inputs.values(), ids=format_test_inputs.keys()
)
def test_currency_formatting(input_number, output):
    """ Test that currency values get set properly.
    """
    assert format_to_currency(input_number) == output
