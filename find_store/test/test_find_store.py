import find_store.__main__ as find_store
from find_store.addressmodule import Address
from subprocess import call
from docopt import docopt
import pytest
import os

docs = find_store.docs.__doc__

fileDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))
csv_path = os.path.join(fileDir, "store-locations.csv")

@pytest.fixture(scope="module")
def address_list():
    addresses = [
        Address({'unit': 'mi', 'value': "'jhd' --unit=km --output=json", 'key': 'address', 'output': 'text'}),
        Address({'value': 'postal_code:95112 --unit=km --output=json', 'output': 'text', 'unit': 'mi', 'key': 'components'}),
    ]
    return addresses

main_test_cases = [
    ("--address='190 Ryland st.'", 0),
    ("--zip=95112", 0),
    ("--zip=95112 --unit=km --output=json", 0),
    ("--address='jhd' --unit=km --output=json", 0),
    ("--address='190 Ryland St.' --zx", 1),
]

# main function is hard to test, here, mimic the command line call and look for expected code
@pytest.mark.parametrize("args, expected", main_test_cases)
def test_main(args, expected):
    assert call("find_store " + args, shell=True) == expected

extract_args_test_cases = [
    (["--address='190 Ryland st.'"], {'key': 'address', 'output': 'text', 'unit': 'mi', 'value': "'190 Ryland st.'"}),
    (["--zip=95112"], {'unit': 'mi', 'output': 'text', 'value': 'postal_code:95112', 'key': 'components'}),
    (["--zip=95112 --unit=km --output=json"], {'value': 'postal_code:95112 --unit=km --output=json', 'output': 'text', 'unit': 'mi', 'key': 'components'}),
    (["--address='jhd' --unit=km --output=json"], {'unit': 'mi', 'value': "'jhd' --unit=km --output=json", 'key': 'address', 'output': 'text'}) 
]

@pytest.mark.parametrize("args, expected", extract_args_test_cases)
def test_extract_args(args, expected):
    args = docopt(docs, argv=args)
    assert find_store.format_args(args) == expected

address_args = [
    ({'value': 'jhd', 'key': 'address'}, True),
    ({'value': 'postal_code:95112', 'key': 'components'}, True)
]

@pytest.mark.parametrize("params, expected", address_args)
def test_address_geocode(address_list, params, expected):
    for address in address_list:
        assert address.geocode(params)['results']

geocode_args = [
    ({'value': 'jhd', 'key': 'address'}, 0.5487839026701014),
    ({'value': 'postal_code:95112', 'key': 'components'}, 1.3631875966444915)
]

@pytest.mark.parametrize("params, expected", geocode_args)
def test_address_geocode(address_list, params, expected):
    for address in address_list:
        address.geocode(params)
        assert address.get_closest_store(csv_path)['distance'] == expected

distance_args = [
    ({'value': 'jhd', 'key': 'address'}, {'Longitude': -73.935242, 'Latitude': 40.730610}, 503.16414056484814),
    ({'value': 'postal_code:95112', 'key': 'components'}, {'Longitude': 2.154007, 'Latitude': 41.390205}, 7200.35833273643)
]

@pytest.mark.parametrize("params, store, expected", distance_args)
def test_distance(address_list, params, store, expected):
    for address in address_list:
        address.geocode(params)
        assert address.calculate_distance(store) == expected