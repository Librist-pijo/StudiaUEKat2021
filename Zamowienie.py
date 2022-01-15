import Dom
import Mieszkanie
import Developer
import datetime
import decimal

class Zamowienie:
    def __init__(self, id, developer: Developer,
                 mieszkanie: Mieszkanie, dom: Dom, order_date: datetime):
        self._id = id
        self._developer = developer
        self._dom = dom
        self._mieszkanie = mieszkanie
        self._order_date = order_date

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @property
    def developer(self):
        return self._developer

    @developer.setter
    def developer(self, value):
        self._developer = value

    @property
    def dom(self):
        return self._dom

    @dom.setter
    def dom(self, value):
        self._dom = value

    @property
    def mieszkanie(self):
        return self._mieszkanie

    @mieszkanie.setter
    def mieszkanie(self, value):
        self._mieszkanie = value

    @property
    def order_date(self):
        return self._order_date

    @order_date.setter
    def order_date(self, value):
        self._order_date = value

    def TotalPrice(self):
        return self._dom._price + self._mieszkanie._price

    def Totalm2(self):
        return self._dom._m2 + self.mieszkanie._m2

    def __str__(self):
        return f"""
    id: {self._id}
    dom: {self._dom}
    mieszkanie: {self._mieszkanie}
    order_date: {self._order_date}
    developer: {self._developer}
    total price: {self.TotalPrice()}
    total m2: {self.Totalm2()}
    """