from twilio.rest import Client
import time
import smtplib


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    def __init__(self):
        self.account_sid = ''
        self.auth_token = ''
        self.TEST_NUMBER = ''
        self.MY_NUMBER = ''
        self.sender_email = ""
        self.recipient_email = ""
        self.password = ""

    def send_notification(self, message: str):
        client = Client(self.account_sid, self.auth_token)
        message = client.messages.create(body=message, from_=self.TEST_NUMBER, to=self.MY_NUMBER)
        print(message.status)
        time.sleep(5)

    def format_message(self, data: dict):
        return f"Low price alert! Only £{data['price']} to fly from {data['departure_city']}-{data['departure_airport']} to {data['arrival_city']}-{data['arrival_airport']} from {data['local_leave_date'].split('T')[0]} to {data['local_return_date'].split('T')[0]}."

    def send_alerts_from_data(self, data: dict):
        for key, value in data.items():
            if value:
                self.send_notification(self.format_message(value))

    def send_email(self, message: str):
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()

            connection.login(user=self.sender_email, password=self.password)

            connection.sendmail(
                from_addr=self.sender_email,
                # Can connect this to user input at some point if needed
                to_addrs=self.recipient_email,
                msg=f"Subject:🛩️🌎🤑🚨Flight Deal Alert🛩️🌎🤑🚨!\n\n{message}".encode('utf-8')
            )

    def send_emails_from_data(self, data: dict):
        for key, value in data.items():
            if value:
                self.send_email(self.format_message(value))
