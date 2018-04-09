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

"""