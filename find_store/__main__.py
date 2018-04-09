import sys
import json
import os

from docopt import docopt

from .addressmodule import Address

def docs():
    """
    Find Store
    find_store will locate the nearest store (as the crow flies) from
    store-locations.csv, print the matching store address, as well as
    the distance to that store.

    Usage:
    find_store --address=<address>
    find_store --address=<address> [--units=(mi|km)] [--output=(text|json)]
    find_store --zip=<zip>
    find_store --zip=<zip> [--units=(mi|km)] [--output=(text|json)]

    Options:
    --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
    --address=<address>  Find nearest store to this address. If there are multiple best-matches, return the first.
    --units=(mi|km)      Display units in miles or kilometers [default: mi]
    --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

    Example
    find_store --address="1770 Union St, San Francisco, CA 94123"
    find_store --zip=94115 --units=km
    """

def main():
    ''' 
    Invoked when package find_store is invoked. 
    see setup.py for config
    '''
    fileDir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    csv_path = os.path.join(fileDir, "store-locations.csv")
    # creates a dictionary of args
    args = docopt(docs.__doc__)
    attrs = format_args(args)
    # creates address object and gets coords
    address = Address(attrs)
    address.geocode(attrs)
    # shows error if no results
    if not address.geocode_json['results']:
        return address.geocode_json['status']
    # finds store closest to the address or zip entered
    closest_store = address.get_closest_store(csv_path)
    # display closest store data
    display(closest_store, address.output)

def display(closest_store, style):
    # decide display style
    if style == "json":
        json_output(closest_store)
    else:
        text_output(closest_store)

def text_output(closest_store):
    """
    prints human readable address and distance to console
    """
    print(closest_store['store']['\ufeffStore Name'])
    print(closest_store['store']['Store Location'])
    print("{}, {} {}".format(
        closest_store['store']['City'], 
        closest_store['store']['State'],
        closest_store['store']['Zip Code']
        )
    )
    print("Distance: {} {}".format(round(closest_store['distance'], 1), closest_store['unit']))

def json_output(closest_store):
    """
    print computer readable address and distance to console
    """
    store_dict = {
        "Name": closest_store['store']['\ufeffStore Name'],
        "Location": closest_store['store']['Store Location'],
        "City": closest_store['store']['City'],
        "State": closest_store['store']['State'],
        "Zip Code": closest_store['store']['Zip Code'],
        "Distance": "{} {}".format(round(closest_store['distance'], 1), closest_store['unit'])
    }
    # convert dict to string
    store_string = json.dumps(store_dict)
    print(store_string)

def format_args(args):
    """
    extracts arguments passed in from command line 
    converts to data needed for query, calculation, and display
    """
    cli_args = {}
    if args['--address']:
        cli_args["key"] = "address"
        cli_args["value"] = args['--address']
    elif args['--zip']:
        cli_args["key"] = "components"
        cli_args["value"] = "postal_code:" + args['--zip']
    if args['--units'] == "km":
        cli_args["unit"] = "km"
    else:
        cli_args["unit"] = "mi"
    if args['--output'] == "json":
        cli_args["output"] = "json"
    else:
        cli_args["output"] = "text"
    return cli_args

if __name__ == '__main__':
    main()