# Import required modules
import requests

# Variables
sheety_username = "caf14cc59105725febff04f5bba84d53"
sheety_projectName = "stevenFlightDeals"
sheety_sheetName = "prices"
sheety_header = {
    "Authorization": "Basic c3RldmVuOiRzcDF1WiYzTlRheGUkeSo="
}

sheety_endpoint = f"https://api.sheety.co/{sheety_username}/{sheety_projectName}/{sheety_sheetName}"

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        # 1. Use the Sheety API to GET all the data in that sheet and print it out.
        sheety_response = requests.get(sheety_endpoint, headers=sheety_header)
        data = sheety_response.json()
        self.destination_data = data["prices"]
        return self.destination_data        
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheety_response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=sheety_header
            )
            print(sheety_response.text)