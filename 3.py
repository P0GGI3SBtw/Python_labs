class Person(object):
    counter = 0

    def __init__(self):
        Person.counter += 1

    def print_gender(self):
        print('Person gender is unknown')


class Female(Person):
    def __init__(self):
        super().__init__()

    def print_gender(self):
        print('Person gender is female')


class Male(Person):
    def __init__(self):
        super().__init__()

    def print_gender(self):
        print('Person gender is male')


person1 = Male()
person1.print_gender()

person2 = Female()
person2.print_gender()

person3 = Person()
person3.print_gender()

print('Number of object form class: ', Person.counter)
