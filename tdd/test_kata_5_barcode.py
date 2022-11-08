"""
Kata 5 from:

https://tddmanifesto.com/exercises/
"""
from collections import defaultdict

import pytest

BARCODE_DATABASE = defaultdict(float, [("12345", 7.25), ("23456", 12.50),])

ERROR_DATABASE = {"": "Error: empty barcode", "99999": "Error: barcode not found"}


def format_to_currency(total):
    return "$" + "{:.2f}".format(total)


def total(input_codes):
    """
    """
    # Check there is not error in the barcodes scanned.
    if set(input_codes) & set(ERROR_DATABASE):
        # Get the first error code
        error_code = list(set(input_codes) & set(ERROR_DATABASE))[0]
        return ERROR_DATABASE[error_code]

    total_value = sum(safe_scan_barcode(input_code) for input_code in input_codes)
    return format_to_currency(total_value)


def scan_barcode(input_code):
    """
    """
    if input_code in ERROR_DATABASE.keys():
        return ERROR_DATABASE[input_code]

    return format_to_currency(safe_scan_barcode(input_code))


def safe_scan_barcode(input_code):
    """
    """
    value = BARCODE_DATABASE[input_code]
    return value


multiple_test_inputs = {
    "multiple": (["12345", "23456"], "$19.75"),
    "barcode_not_found": (["23456", "99999"], "Error: barcode not found"),
    "empty_barcode": (["", "23456"], "Error: empty barcode"),
    "multiple_errors": (["", "99999"], "Error: empty barcode"),
}


@pytest.mark.parametrize(
    "input_codes,output",
    multiple_test_inputs.values(),
    ids=multiple_test_inputs.keys(),
)
def test_total(input_codes, output):
    """ Test total_values.
    """
    assert total(input_codes) == output


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
