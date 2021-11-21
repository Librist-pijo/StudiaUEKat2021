#zad 1

class Student:
    def __init__(self, name: str, marks: int):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if self.marks > 50:
            return True
        else:
            return False


obj1 = Student(name='Ktoś', marks=0)
obj1.marks = 51
print(obj1.is_passed())
obj1.marks = 49
print(obj1.is_passed())


class Library:
    def __init__(self, city: str, street: str, zip_code: str, open_hours: str, phone: str):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f'Biblioteka w mieście {self.city} na ulicy {self.street}'

class Order:
    def __init__(self,employee,student,books,order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
       return f'Zamówienie dla {self.student} na {self.books} w dniu {self.order_date} spakował {self.employee}'

class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone
    def __str__(self):
        return f'pracownik {self.first_name} {self.last_name}'

class Book:
    def __init__(self,library,publication_date,author_name,author_surname,number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages
    def __str__(self):
        return f'Ksiażka {self.author_surname} z biblioteki w {self.library.city}'


bibl1 = Library(city='Wawa', zip_code='42-13', open_hours='10-20', street='xyzowa', phone='987654321')
bibl2 = Library(city='Wro', zip_code='45-132', open_hours='11-21', street='qwertyowa', phone='123456789')
listaksiazek = []

listaksiazek.append(Book(library=bibl1, publication_date='10-10-1998', author_name='xyz', author_surname='ors', number_of_pages=300))
listaksiazek.append(Book(library=bibl1, publication_date='10-12-1998', author_name='xyz1', author_surname='ors1', number_of_pages=350))
listaksiazek.append(Book(library=bibl2, publication_date='10-10-1993', author_name='xyz2', author_surname='ors2', number_of_pages=360))
listaksiazek.append(Book(library=bibl2, publication_date='10-10-1995', author_name='xyz3', author_surname='ors3', number_of_pages=323))
listaksiazek.append(Book(library=bibl2, publication_date='10-10-1991', author_name='xyz4', author_surname='ors5', number_of_pages=567))

listapracowników = []
listapracowników.append(Employee(street='test',zip_code='test2',phone='123456789',city='wawa',last_name='syz',first_name='jakistam',hire_date='30-10-1998',birth_date='20-10-1975'))
listapracowników.append(Employee(street='test4',zip_code='test3',phone='123456789',city='wro',last_name='syz1',first_name='jakistam2',hire_date='30-10-1998',birth_date='20-10-1975'))
listapracowników.append(Employee(street='test3',zip_code='test1',phone='123456789',city='wawa',last_name='syz2',first_name='jakistam3',hire_date='30-10-1998',birth_date='20-10-1975'))

listastudentow = []
listastudentow.append(Student(name='xyz',marks=34))
listastudentow.append(Student(name='xyz2',marks=343))
listastudentow.append(Student(name='xyz3',marks=15))

listazamowien = []
listazamowien.append(Order(Employee=listapracowników[1], student=listastudentow[2], books=listaksiazek[1], order_date='10-10-2021'))

