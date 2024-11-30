import pytest

from find_budget import find_website


@pytest.mark.parametrize(
    "city, state, expected",
    [
        ("Williston", "Vermont", "https://www.town.williston.vt.us/"),
        ("South Burlington", "Vermont", "https://www.southburlingtonvt.gov/"),
        ("Richmond", "Vermont", "https://www.richmondvt.gov/"),
        ("Colchester", "Vermont", "https://colchestervt.gov/"),
        ("Barre", "Vermont", "https://www.barrecity.org/") # This one fails
    ],
)
def test_find_website(city, state, expected):
    assert find_website(city, state) == expected
