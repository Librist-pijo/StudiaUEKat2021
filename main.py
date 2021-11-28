class Produkt:
    def __init__(self, price: float, name: str, quantity: int, country_of_made: str, company: str):
        self._price = price
        self._name = name
        self._quantity = quantity
        self._country_of_made = country_of_made
        self._company = company

    @property
    def price(self):
        return self._price

    @property
    def name(self):
        return self._name

    @property
    def quantity(self):
        return self._quantity

    @property
    def country_of_made(self):
        return self._country_of_made

    @property
    def company(self):
        return self._company

    def __str__(self):
        return f"Product - price: {self.price}, name: {self.name}, quantity: {self.quantity}," \
               f" country_of_made: {self.country_of_made}, company: {self.company}"

    @price.setter
    def price(self, value):
        self._price = value

    @name.setter
    def name(self, value):
        self._name = value

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @country_of_made.setter
    def country_of_made(self, value):
        self._country_of_made = value

    @company.setter
    def company(self, value):
        self._company = value


class Magazyn:
    def __init__(self, city: str, zip_code: str, driver: str, logistics: str, boss: str):
        self.city = city
        self.zip_code = zip_code
        self.driver = driver
        self.logistics = logistics
        self.boss = boss

    @property
    def city(self):
        return self.city

    @property
    def zip_code(self):
        return self.zip_code

    @property
    def driver(self):
        return self.driver

    @property
    def logistics(self):
        return self.logistics

    @property
    def boss(self):
        return self.boss

    def __str__(self):
        return f"Magazyn - city: {self.city}, zip_code: {self.zip_code}, driver: {self.driver}," \
               f" logistics: {self.logistics}, boss: {self.boss}"


class Klient:
    def __init__(self, city: str, address: str, zip_code: str):
        self.city = city
        self.address = address
        self.zip_code = zip_code

    @property
    def city(self):
        return self.city

    @property
    def address(self):
        return self.address

    @property
    def zip_code(self):
        return self.zip_code

    def __str__(self):
        return f"Klient - city: {self.city}, zip_code: {self.zip_code}, address: {self.address}"

    @city.setter
    def city(self, value):
        self._city = value

    @address.setter
    def address(self, value):
        self._address = value

    @zip_code.setter
    def zip_code(self, value):
        self._zip_code = value


class KlientDetaliczny(Klient):
    def __init__(self, name: str, surname: str, city: str, address: str, zip_code: str):
        super().__init__(city, address, zip_code)
        self.name = name
        self.surname = surname

    @property
    def name(self):
        return self.name

    @property
    def surname(self):
        return self.surname

    def __str__(self):
        return f"KlientDetaliczny - city: {self.city}, surname: {self.surname}"

    @name.setter
    def name(self, value):
        self._name = value

    @surname.setter
    def surname(self, value):
        self._surname = value


class KlientBiznesowy(Klient):
    def __init__(self, company: str, nip: str, city: str, address: str, zip_code: str):
        super().__init__(city, address, zip_code)
        self.nip = nip
        self.company = company

    @property
    def company(self):
        return self.company

    @property
    def nip(self):
        return self.nip

    def __str__(self):
        return f"KlientBiznesowy - nip: {self.nip}, company: {self.company}"


class Zamowienia():
    def __init__(self, client: Klient, quantity: int, product: list, order_date: str, sent_date: str):
        self._client = client
        self._quantity = quantity,
        self._product = product
        self._order_date = order_date
        self._sent_date = sent_date

    @property
    def client(self) -> str:
        return self._client

    @client.setter
    def client(self, value):
        self._client = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        self._quantity = value

    @property
    def product(self) -> list:
        return self._product

    @product.setter
    def product(self, value: list):
        self._product = value

    @property
    def order_date(self) -> str:
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        self.order_date = value

    @property
    def sent_date(self) -> str:
        return self._sent_date

    @sent_date.setter
    def sent_date(self, value):
        self._sent_date = value

    def total_price(self, value: float) -> float:
        for i, v in enumerate(self._product):
            value = value + v
        return round(value, 2)

    def client_address(self):
        return self._client.address

    def __str__(self):
        return f"client: {self._client}, quantity: {self._quantity}, product: {self._product}," \
               f" order_date: {self.order_date}, sent_date: {self.sent_date}"


z = Zamowienia
z.quantity = 1
z.order_date = "10-10-2220"
z.sent_date = "11-10-2220"
z.client = KlientDetaliczny(name="TestName", surname="TestSurname",
                            city="TestCity", address="TestAddress", zip_code="TestZip_Code")
z.product = [
    Produkt(price=23.6, name="JakaśNazwa1", quantity=2, company="JakaśFirma1", country_of_made="JakiśKrajPrd1"),
    Produkt(price=30.6, name="JakaśNazwa2", quantity=2, company="JakaśFirma2", country_of_made="JakiśKrajPrd2")]

print(z)