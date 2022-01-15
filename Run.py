import Zamowienie as zmw
import Dom as d
import Mieszkanie as m
import Developer as dev
import datetime
import decimal

def main():
    z = zmw.Zamowienie(id=1, developer=dev.Developer(id=1, address='testaddrs',
                                             name='testname', nip='testnip'),
                   mieszkanie=m.Mieszkanie(id=1, price=2000.20,
                                         address='testaddrsmieksz', m2=50),
                   dom=d.Dom(id=1, price=20000.30,
                           address='testaddrsdom', m2=150),
                   order_date=datetime.date.today())
    print(z)
