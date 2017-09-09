#This will handle the storage of Mac Address and the associated persons
import time
import json
class InformationStorage:


    def __init__(self):
        self.person_list = []
        self.read_file()
        self.leave_times = {}
        self.arrive_times = {}

    def read_file(self):
        with open('information.txt', 'r') as file:
            content = file.readlines()
            for line in content:
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

    def log_leave(self, mac):
        name = self.get_name(mac)
        self.leave_times[name] = time.strftime("%H:%M:%S")
        self.arrive_times[name] = None

    def log_arrive(self, mac):
        name = self.get_name(mac)
        self.arrive_times[name] = time.strftime("%H:%M:%S")
        self.leave_times[name] = None

    def log_goings(self):
        with open("leave_log", "w+") as f:
            json.dump(self.leave_times, f)
        with open("arrive_log", "w+") as f:
            json.dump(self.arrive_times, f)


class Person:

    def __init__(self, name, mac_address):
        self.name = name
        self.mac_address = mac_address