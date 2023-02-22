class Person:

    def __init__(self, name, address, phone):
        self.__name = name 
        self.__address = address
        self.__phone = phone

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_phone(self):
        return self.__phone


    def print_person(self):
        print('name:', self.__name)
        print('addr:', self.__address)
        print('phone:', self.__phone)

class Customer(Person):

    def __init__(self, name, address, phone, id, mailing):
        Person.__init__(self, name, address, phone)
        
        self.__id = id
        self.__mailing = mailing

    def print_person(self):
        print("#method 1")
        
        Person.print_person(self)
        print('id:', self.__id)
        if self.__mailing:
            print('on mailing list: Yes')
        else:
            print('on mailing list: No')

        print()


        print("#method 2")
        
        print(f"name: {Person.get_name(self)}")
        print(f"address: {Person.get_address(self)}")
        print(f"phone: {Person.get_phone(self)}")
        print('id:', self.__id)
        if self.__mailing:
            print('on mailing list: Yes')
        else:
            print('on mailing list: No')