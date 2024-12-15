class Manufacturer:
    def __init__(self, identity, location):
        self.identity = identity
        self.location = location

    def describe(self):
        print("Danh tinh-identity:", self.identity)
        print("Dia diem-location:", self.location)

class Device:
    def __init__(self, name, price, identity, location):
        self.name = name
        self.price = price
        # Create an instance of Manufacturer
        self.manufacturer = Manufacturer(identity, location)

    def describe(self):
        print("Ten-name:", self.name)
        print("Gia-price:", self.price)
        # Access the manufacturer details
        self.manufacturer.describe()

# Create a Device instance
a = Device("vantrung", 9.9, 12, "vietnam")

# Call the describe method
a.describe()
