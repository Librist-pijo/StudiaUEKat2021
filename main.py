# Zad a.
def fn_names(names):
    for name in names:
        print(name)


names = ['Ala', 'Tomek', 'Rafał', 'Piotr', 'Monika']
fn_names(names)


# Zad b.
# i.
def for_multiply(numbers):
    for i in range(len(numbers)):
        numbers[i] = numbers[i] * 2
    return print(numbers)


numbers = [1, 2, 3, 4, 5]
for_multiply(numbers)


# ii.
def multiply(numbers):
    numbers = [number * 2 for number in numbers]
    return print(numbers)


numbers = [1, 2, 3, 4, 5]
for_multiply(numbers)


# zad c.
numbers = list(range(11))
for number in numbers:
    if number % 2 == 0 and number != 0:
        print(number)

"""
Zapisałem sobie jako alternatywa, lista składowana która od razu ma liczby parzyste
numbers = [number for number in range(11) if number % 2 == 0 and number != 0]
print(numbers)
"""

# zad d.
numbers = list(range(11))
print(numbers[::2])
