from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import FlightData
from notification_manager import NotificationManager

# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.

data_manager = DataManager()
flight_data = FlightData(data_manager.get_location_codes())
flight_search = FlightSearch('LON', flight_data)
notification_manager = NotificationManager()

flights_information = flight_search.get_flights(data_manager.get_data())

notification_manager.send_alerts_from_data(flights_information)