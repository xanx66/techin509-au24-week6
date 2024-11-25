import datetime

class Message:
    def __init__(self, content, timestamp):
        self.content = content
        self.timestamp = timestamp


class iPhone:
    def __init__(self, name, version, phone_number, color, model):  # constructor
        self.name = name
        self.version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model
        self.messages = []  # List to store received messages

    def send_message(self, to, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        msg = Message(content, timestamp)
        to.receive(msg)

    def receive(self, msg):
        self.messages.append(msg)
        print(f"{self.name} has received a message at {msg.timestamp}: {msg.content}")

    def check_messages(self):
        print(f"Messages for {self.name}:")
        for msg in self.messages:
            print(f" - {msg.timestamp}: {msg.content}")

    def set_name(self, new_name):
        if len(new_name) < 3:
            print("Name must be longer than 3 characters")
        else:
            self.name = new_name
            print(f"The phone's name has been updated to {self.name}")


# Create instances of the iPhone class
phone1 = iPhone(name="iPhone1", version="15", phone_number="123456789", color="black", model="14")
phone2 = iPhone(name="iPhone2", version="15", phone_number="987654321", color="white", model="16 Pro")

# Change names of the phones
phone1.set_name("Annika's iPhone")
phone2.set_name("Fiona's iPhone")

# Send an iMessage from phone1 to phone2
phone1.send_message(phone2, "Hello from Annika!")

# Check messages on phone2
phone2.check_messages()
