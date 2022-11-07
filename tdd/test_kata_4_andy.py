import pytest

CITIES = [
    "Paris",
    "Budapest",
    "Skopje",
    "Rotterdam",
    "Valencia",
    "Vancouver",
    "Amsterdam",
    "Vienna",
    "Sydney",
    "New York City",
    "London",
    "Bangkok",
    "Hong Kong",
    "Dubai",
    "Rome",
    "Istanbul",
]


def search(search_term):
    if search_term == "*":
        return CITIES

    if len(search_term) < 2:
        return []

    return [city for city in CITIES if search_term.lower() in city.lower()]


@pytest.mark.parametrize(
    "given,expected",
    [
        pytest.param("", [], id="empty"),
        pytest.param("I", [], id="less than 2"),
        ("Ist", ["Istanbul"]),
        ("Va", ["Valencia", "Vancouver"]),
        ("va", ["Valencia", "Vancouver"]),
        ("ape", ["Budapest"]),
        ("*", CITIES),
    ],
)
def test_search(given, expected):
    actual = search(given)
    assert actual == expected
