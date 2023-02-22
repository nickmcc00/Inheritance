import personClass as p

name = 'John'
address = '1234 main street'
phone = '123-456-789'
id = 1234
mailing = True

person1 = p.Person(name, address, phone)

customer1 = p.Customer(name, address, phone, id, mailing)

person1.print_person()

print()
print()
print()

customer1.print_person()


