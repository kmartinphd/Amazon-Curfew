#This will handle the storage of Mac Address and the associated persons

class InformationStorage:


    def __init__(self):
        self.person_list = []
        self.read_file()

    def read_file(self):
        file = open('information.txt', 'r')
        content = file.readlines()
        for line in content:
            print('program is reading a line')
            tuple_of_info = line.split(',')
            name = tuple_of_info[0].strip()
            mac_address = tuple_of_info[1].strip()
            person = Person(name=name, mac_address=mac_address)
            self.person_list.append(person)

    def get_mac_addresses(self):
        addresses = []
        for person in self.person_list:
            address = person.mac_address
            addresses.append(address)
        return addresses

    def get_name(self, mac_address):
        for person in self.person_list:
            if person.mac_address == mac_address:
                return person.name
        return 'person_not_found'


class Person:

    def __init__(self, name, mac_address):
        self.name = name
        self.mac_address = mac_address