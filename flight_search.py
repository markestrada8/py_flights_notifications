import requests
from flight_data import FlightData


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, home_location: str, flight_data_object: FlightData):
        self.flight_search_endpoint = 'https://api.tequila.kiwi.com/v2/search'
        self.locations_search_endpoint = 'https://api.tequila.kiwi.com/locations/query'

        self.flight_home_IATA = home_location
        self.flight_data_object = flight_data_object

    def get_flights(self, data: dict):
        # Takes data manager get_data as an argument
        # Returns dictionary of empty lists for no flights found or single dictionary of first lowest price flight
        alertable_flights = {}
        for item in data['prices']:
            alertable_flights[item['city']] = []

            response = requests.get(
                self.flight_search_endpoint,
                headers=self.flight_data_object.get_flight_search_headers(),
                params=self.flight_data_object.get_flight_search_params(self.flight_home_IATA, item['iataCode']),
            )
            response.raise_for_status()

            flights_info = [{
                'price': item['price'],
                'departure_city': item['cityFrom'],
                'departure_airport': item['flyFrom'],
                'arrival_city': item['cityTo'],
                'arrival_airport': item['flyTo'],
                'local_leave_date': item['route'][0]['local_departure'],
                'local_return_date': item['route'][1]['local_departure']
            } for item in response.json()['data']]

            for flight in flights_info:

                if flight['price'] < item['lowestPrice (gbp)']:
                    alertable_flights[item['city']].append(flight)

        return {k: v[0] if len(v) > 1 else v for k, v in alertable_flights.items()}
