#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from datetime import datetime, timedelta

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
notification_manager = NotificationManager()

flight_search = FlightSearch()

if sheet_data[0]['iataCode'] == '':
    
    for row in sheet_data:
        row['iataCode'] = flight_search.get_destination_code(row['city'])
    print(f"sheet_data:\n {sheet_data}")

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for dest in sheet_data:
    latest_price = flight_search.search_flight_price(
        origin="LON",
        dest=dest["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    
    if latest_price.price < dest["lowestPrice"]:
        notification_manager.send_sms(
            message=f"Low price alert! Only £{latest_price.price} to fly from London-{dest['iataCode']} from {tomorrow.strftime('%d/%m/%Y')} to {six_month_from_today.strftime('%d/%m/%Y')}."
        )