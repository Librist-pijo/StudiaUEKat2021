import decimal
class Dom:
    def __init__(self, id: int, price: decimal, address: str, m2: int):
        self._id = id
        self._price = price
        self._address = address
        self._m2 = m2

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            self._id = value

        @property
        def rooms(self):
            return self.rooms

        @rooms.setter
        def rooms(self, value):
            self._rooms = value

        @property
        def address(self):
            return self._address

        @address.setter
        def address(self, value):
            self._address = value

        @property
        def m2(self):
            return self._m2

        @m2.setter
        def number(self, value):
            self._m2 = value

    def __str__(self):
        return f"id: {self._id}, price: {self._price}," \
               f" adress: {self._address}, m2: {self._m2}"
