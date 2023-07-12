from twilio.rest import Client
import time


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = ''
        self.auth_token = ''
        self.TEST_NUMBER = ''
        self.MY_NUMBER = ''

    def send_notification(self, message):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages \
            .create(
            body=message,
            from_=self.TEST_NUMBER,
            to=self.MY_NUMBER
        )
        print(message.status)
        time.sleep(5)

    def format_message(self, data):
        return f"Low price alert! Only £{data['price']} to fly from {data['departure_city']}-{data['departure_airport']} to {data['arrival_city']}-{data['arrival_airport']} from {data['local_leave_date'].split('T')[0]} to {data['local_return_date'].split('T')[0]}."

    def send_alerts_from_data(self, data):
        for key, value in data.items():
            if value:
                self.send_notification(self.format_message(value))
