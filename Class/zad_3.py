import decimal

print("Zad 3")


class Property:
    def __init__(self, area: str, rooms: int, price: decimal, address: str):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address

    def __str__(self):
        return f"""
               Property:
                   area: {self.area}
                   rooms: {self.rooms}
                   price: {self.price}
                   address: {self.address}
               """


class House(Property):
    def __init__(self, plot: int, area: str,
                 rooms: int, price: decimal, address: str):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"""
               House(Property):
                   area: {self.area}
                   rooms: {self.rooms}
                   price: {self.price}
                   address: {self.address}
                   plot: {self.plot}
               """


class Flat(Property):
    def __init__(self, floor: int, area: str,
                 rooms: int, price: decimal, address: str):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"""
               Flat(Property):
                    area: {self.area}
                   rooms: {self.rooms}
                   price: {self.price}
                   address: {self.address}
                   floor: {self.floor}
               """


dom = House(area="xyz", price=3456.20, address="costam", rooms=10, plot=4)
mieszkanie = Flat(floor=3, area="xyz2",
                  rooms=3, price=123.10, address="costam2")
print(dom)
print(mieszkanie)
