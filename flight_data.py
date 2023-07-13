from datetime import datetime as dt, timedelta
import requests


class FlightData:
    # This class is responsible for structuring the flight data.
    def __init__(self, location_codes: dict):
        self.location_codes = location_codes
        self.flight_search_api_key = ''

    def tomorrow(self):
        return str((dt.now() + timedelta(days=1)).strftime('%d/%m/%Y'))

    def six_months_date(self):
        return str((dt.now() + timedelta(days=183)).strftime('%d/%m/%Y'))

    def get_location_code(self, location: str):
        parameters = {'term': location}
        response = requests.get(self.locations_search_endpoint, headers=self.header, params=parameters)
        return response.json()['locations'][0]['code']

    def get_flight_search_headers(self):
        return {
            'apikey': self.flight_search_api_key,
            'Content-Type': 'application/json'
        }

    def get_flight_search_params(self, origin: str, destination: str):
        return {
            'fly_from': origin,
            'fly_to': destination,
            'date_from': self.tomorrow(),
            'date_to': self.six_months_date(),
            'curr': 'GBP',
            'max_stopovers': '0',
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28
        }
