# Object
#  -> Specific intance of a class

# Class
# -> General definition

class Message:
    content: str
    timestamp: str


class iPhone:
    def __init__(self, name, version, phone_number, color , model): #constructor
        self.name = name
        self.version = version
        self.phone_number = phone_number
        self.color = color
        self.model = model

    def send_message(self, to, content):
        msg = Message(content, timestamp=Date())
        to.receive(msg)
    
    def recieve(self, msg):
        print(self.name, "has received", msg.timestamp, "-", msg.content)

    def drop(self,filename):
        print("Dropping %s" % filename)
        pass



    def set_name(self,new_name):
        if len(new_name)<3:
            print("Name must be longer than 3 character")
        else:
            self.name = new_name
            print(f"Now {self.name} is {new_name}")


# Create an instance of iPhone class
ians_iphone = iPhone(name = "Ian's Iphone",version = "18", phone_number = "123456", color = "blue", model = "16 promax")
print(ians_iphone.name)
ians_iphone.set_name("MEME")
ians_iphone.drop("notes.pdf")

rishis_iphone = iPhone(name="Rishi's Iphone", version = "16", phone_number = "654321", color = "pink", model = "12 promax")