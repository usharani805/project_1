# Singleton Pattern

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            print("Database connection created")
        return cls._instance

    def connect(self):
        print("Connected to database")


# Factory Pattern

class EmailNotification:
    def send(self, message):
        print(f"Email: {message}")


class SMSNotification:
    def send(self, message):
        print(f"SMS: {message}")


class NotificationFactory:
    @staticmethod
    def create_notification(notification_type):
        if notification_type == "email":
            return EmailNotification()
        elif notification_type == "sms":
            return SMSNotification()
        else:
            raise ValueError("Invalid notification type")


# Main Program

# Testing Singleton
db1 = Database()
db1.connect()

db2 = Database()
db2.connect()

print("Same database object:", db1 is db2)


# Testing Factory
email = NotificationFactory.create_notification("email")
email.send("Welcome to Python!")

sms = NotificationFactory.create_notification("sms")
sms.send("Your OTP is 1234")