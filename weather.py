import requests

class City:
    def __init__(self, name, lat, lon, units="metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):

        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=b717c33dd19b2a6df5ee3a4d031c8d63")
            print(response.json())
        except Exception as e:
            print("there is no access to the internet at this time")

        self.response_json = response.json()
        self.temp =self.response_json["main"]["temp"]
        self.temp_min =self.response_json["main"]["temp_min"]
        self.temp_max =self.response_json["main"]["temp_max"]

    def temp_print(self):
        unit_symbol = "C"
        if self.units == "imperial":
            unit_symbol = "F"
        print(f"In Montreal it is currently {self.temp}° {unit_symbol}")
        print(f"Today's high: {self.temp_max}° {unit_symbol}")
        print(f"Today's low: {self.temp_min}° {unit_symbol}")



# my_city = City("Douala", 4.0511, 9.7679 )
# my_city.temp_print()
new_city = City("Montreal", 45.5019, -73.5674, units="imperial")
new_city.temp_print()