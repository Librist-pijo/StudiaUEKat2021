# zad 1
def return_string(name: str, surname: str) -> str:
    # Use a breakpoint in the code line below to debug your script.
    return f'Cześć {name} {surname}'  # Press Ctrl+F8 to toggle the breakpoint.


name = 'Piotr'
surname = 'Xyz'

wynik = return_string(name, surname)
print(wynik)


# Zad 2
def multiply(a: int, b: int) -> int:
    return a * b


# zad 3
def jest_parzysta(a: int) -> bool:
    if a % 2 == 0:
        return True


a = 3
if jest_parzysta(a):
    print('Liczba parzysta')
else:
    print('liczba nieparzysta')
a = 4
if jest_parzysta(a):
    print('Liczba parzysta')
else:
    print('liczba nieparzysta')

#zad 4
def suma_wieksza_lub_rowna_niz(a: int, b: int, c: int) -> bool:
    if a+b >= c:
        return True


#zad 5
def jest_na_liscie(listaliczb: list, b : int ):
    return listaliczb.__contains__(b)


#zad 6
def list_append_and_pow(pierwszalista: list, drugalista: list) -> list:
    pierwszalista.extend(drugalista)
    pierwszalista = list(dict.fromkeys(pierwszalista))
    return [number**3 for number in pierwszalista]

#zad 7
import requests
class Brawery:
    response = requests.get("https://api.openbrewerydb.org/breweries")
obiekt = Brawery
print(obiekt.response.json())

