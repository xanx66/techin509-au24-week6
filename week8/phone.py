class Phone:
    def __init__(self,name):
       self.name = name
    def call(self,to):
       print("Dialing", to, "...")


class iPhone(Phone):
  def airdrop(self, to, file):
     print ("Sending", file, "to", to, "...")


class Android(Phone):
    def ok_google(self):
       print("Ok Google")

phone = iPhone("ME")
phone.call("1234")
phone.airdrop("YOU", "2.pdf")

phone2 = Android("YOU")
phone2.call("12345678")
phone2.ok_google()