import requests
from flight_data import FlightData

ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "zcD5vI-mvbUur7olY-Mj5LIvtHy2UStG"
headers = {
    "apikey": API_KEY,
}

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    pass

    def get_destination_code(self, city_name):
        para = {
            "term": city_name,
            "location_types": "city"
        }
        response = requests.get(f"{ENDPOINT}/locations/query", params=para, headers=headers)
        return response.json()["locations"][0]["code"]
        # return response.json()
        
    def search_flight_price(self, origin, dest, from_time, to_time):
        para = {
            "fly_from": origin,
            "fly_to": dest,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "max_stopovers": 0,
            "one_for_city": 1,
            "curr": "GBP",
        }
        
        response = requests.get(
            f"{ENDPOINT}/v2/search", 
            params=para, 
            headers=headers)
        
        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {dest}.")
            return None
        
        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date = data["route"][0]["local_departure"].split("T")[0],
            return_date = data["route"][1]["local_departure"].split("T")[0],
        )
        
        print(f"{flight_data.destination_city}: £{flight_data.price}")
        return flight_data
        