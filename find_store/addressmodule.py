import requests
import json
import math
import csv
import os

GEOCODE_KEY = "#########"

class Address():
    def __init__(self, args):
        self.geocode_json = None
        self.unit = args["unit"]
        self.output = args["output"]
        self.errors = ""

    # gets coordinates from google places, returns json response
    def geocode(self, args):
        key = args['key']
        val = args['value']
        url = "https://maps.googleapis.com/maps/api/geocode/json?{}={}&key={}".format(key, val, GEOCODE_KEY)
        res = requests.get(url)
        self.geocode_json = res.json()
        return self.geocode_json

    def get_closest_store(self, filename):
        """
        returns closest store in miles from csv stores list
        """
        with open(filename) as store_locations:
            stores = csv.DictReader(store_locations)
            d = self.calculate_distance(next(stores))
            closest = {"distance": float(d)}
            for store in stores:
                distance = self.calculate_distance(store)
                distance_string = "{} {}".format(distance, self.unit)
                if distance < closest['distance']:
                    closest = {'store': store, 'distance': distance, 'unit': self.unit}
            return closest

    def extract_coords(self):
        '''
        gets coords from json results of geocode function
        if multiple results, uses first match by default
        '''
        if self.geocode_json['results']:
            return self.geocode_json['results'][0]['geometry']['location']

    def calculate_distance(self, store):
        '''
        Haversine formula 
        as outlined by Chris Veness here: 
        http://www.movable-type.co.uk/scripts/latlong.html
        '''
        coords = self.extract_coords()
        if self.unit == "km":
            R = 6371 # radius of the earth in km
        else:
            R = 3959 # radius of the earth in miles (returns miles by default)
        lon1 = float(store['Longitude'])
        lat1 = float(store['Latitude'])
        lon2 = coords['lng']
        lat2 = coords['lat']
        dlon = math.radians(lon2 - lon1)
        dlat = math.radians(lat2 - lat1)
        a = abs((math.sin(dlat/2))**2 + math.cos(lat1) * math.cos(lat2) * (math.sin(dlon/2))**2)
        c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) ) 
        distance = R * c 
        return distance