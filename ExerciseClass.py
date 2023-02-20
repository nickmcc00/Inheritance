class Person:

    def __init__(self, name, address, phone):
        self.__name = name 
        self.__address = address
        self.__phone = phone

    def print_person(self, name, address, phone):
        print(self.__name, self.__address, self.__phone)


class Customer(Person):

    def __init__(self, name, address, phone, id, mailing):
        Person.__init__(self, name, address, phone)
        
        self.__id = id
        self.__mailing = True




