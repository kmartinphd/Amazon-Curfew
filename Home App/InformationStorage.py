#This will handle the storage of Mac Address and the associated persons

class InformationStorage:


    def __init__(self):
        self.person_list = []

    def read_file(self):
        file = open('information.text', 'r')

        #file.read()


class Person:

    def __init__(self, name, mac_addresses):
        self.name = name
        self.mac_addresses = mac_addresses