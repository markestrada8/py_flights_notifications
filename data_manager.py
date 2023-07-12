import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.endpoint = ''
        self.sheet_data = requests.get(self.endpoint).json()

    def get_data(self):
        return self.sheet_data

    def insert_data(self, id: int, data: dict):
        # data = {<column>: <value>}
        requests.put(f"{self.endpoint}/{id}", json={'price': data})

    def get_location_codes(self):
        return {item['city']: item['iataCode'] for item in self.get_data()['prices']}
