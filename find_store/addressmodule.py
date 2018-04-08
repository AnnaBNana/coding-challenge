GEOCODE_KEY = "AIzaSyDs-UQjbNInhtGOe9w6c0knbfdEAmcEmDs"

class Address():
    def __init__(self, str_address):
        self.str_address = str_address
    def is_valid(self):
        return True
    def get_coords(self):
        pass
    def compare_all(self):
        pass
    def distance_to(self, dest):
        return "43739 Montrose Ave.\nFremont, Ca 94538\n10 mi"
    def find_store(self):
        return "43739 Montrose Ave.\nFremont, Ca 94538\n10 mi"