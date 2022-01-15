class Developer:
    def __init__(self, id: int, name: str, address: str, nip: str):
        self._id = id
        self._name = name
        self._address = address
        self._nip = nip

        @property
        def id(self):
            return self._id

        @id.setter
        def id(self, value):
            self._id = value

        @property
        def name(self):
            return self._name

        @name.setter
        def name(self, value):
            self._name = value

        @property
        def address(self):
            return self._address

        @address.setter
        def address(self, value):
            self._address = value

        @property
        def nip(self):
            return self._nip

        @nip.setter
        def nip(self, value):
            self._nip = value

    def __str__(self):
        return f"id: {self._id}, name: {self._name}," \
               f" adress: {self._address}, nip: {self._nip}"
