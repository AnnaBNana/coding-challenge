import pytest

from ..addressmodule import Address

new_address = Address("190 Ryland St. #4213 San Jose, Ca 94538")
bad_address = Address("yeryu")


@pytest.mark.parametrize("geocode_obj, expected", [
    (Address("190 Ryland St. #4213 San Jose, Ca 94538"), True),
    (Address("yeryu"), False)
])

def test_geocode(geocode_obj, expected):
    assert (len(geocode_obj.geocode()['results']) > 0) == expected
