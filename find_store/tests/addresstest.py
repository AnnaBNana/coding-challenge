import pytest
from ..addressmodule import Address

new_address = Address("190 Ryland St. #4213 San Jose, Ca 94538")
bad_address = Address("usytdfy 878")

# def test_find_store():
#     assert new_address.find_store() == "43739 Montrose Ave.\nFremont, Ca 94538\n10.3 mi"

def test_is_valid():
    assert new_address.is_valid() == True
    assert bad_address.is_valid() == False
