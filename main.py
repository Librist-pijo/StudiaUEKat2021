# Zad a.
def fn_names(namelist):
    for name in namelist:
        print(name)


names = ['Ala', 'Tomek', 'Rafał', 'Piotr', 'Monika']
fn_names(names)


# Zad b.
# i.
def for_multiply(numberlist):
    for i in range(len(numberlist)):
        numbers[i] = numberlist[i] * 2
    return numberlist


numbers = [1, 2, 3, 4, 5]
for_multiply(numbers)


# ii.
def multiply(numberlist):
    numberlist = [n * 2 for n in numberlist]
    return numberlist


numbers = [1, 2, 3, 4, 5]
for_multiply(numbers)

# zad c.
numbers = list(range(11))
for number in numbers:
    if number % 2 == 0 and number != 0:
        print(number)

"""
Zapisałem sobie jako alternatywa,
lista składowana która od razu ma liczby parzyste
numbers = [number for number in range(11) if number % 2 == 0 and number != 0]
print(numbers)
"""

# zad d.
numbers = list(range(10))
print(numbers[::2])
