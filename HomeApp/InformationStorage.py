import time
import json
class InformationStorage:
    '''
    This Information Storage class is used to create information storage objects which interact with the json and 
    txt files that store the information. It abstracts the reading and writing of the information as well as providing
    helpful methods to surmize the information.
    '''


    def __init__(self):
        self.person_list = []
        self.read_file()
        self.leave_times = {} #maps names to leave times
        self.arrive_times = {} #maps names to arrival times

    def read_file(self):
        '''
        This reads the information txt file which holds the user information and associated mac addresses and loads
        them into the InformationStorage object
        :return: does not return anything
        '''
        with open('information.txt', 'r') as file:
            content = file.readlines()
            for line in content:
                tuple_of_info = line.split(',')
                name = tuple_of_info[0].strip()
                mac_address = tuple_of_info[1].strip()
                person = Person(name=name, mac_address=mac_address)
                self.person_list.append(person)

    def get_mac_addresses(self):
        '''
        :return: a list of all mac addresses associated with registered people
        '''
        addresses = []
        for person in self.person_list:
            address = person.mac_address
            addresses.append(address)
        return addresses

    def get_name(self, mac_address):
        '''
        :param mac_address: the particular mac address detected
        :return: the name of the person whos is associated with the mac address
        '''
        for person in self.person_list:
            if person.mac_address == mac_address:
                return person.name
        return 'person_not_found'

    def get_names_list(self):
        '''
        :return: the names of all registered persons
        '''
        names = []
        for p in self.person_list:
            names.append(p.get_name())
        return names

    def log_leave(self, mac):
        '''
        :param mac: the mac address that has left
        :return: logs the mac address (does not return anything)
        '''
        name = self.get_name(mac)
        self.leave_times[name] = time.strftime("%H:%M:%S")
        self.arrive_times[name] = None

    def log_arrive(self, mac):
        '''
        :param mac: the mac address that has arrived
        :return: logs the mac address (does not return anything)
        '''
        name = self.get_name(mac)
        self.arrive_times[name] = time.strftime("%H:%M:%S")
        self.leave_times[name] = None

    def log_goings(self):
        '''
        :return: writes the current logs to the json files
        '''
        with open("leave_log", "w+") as f:
            json.dump(self.leave_times, f)
        with open("arrive_log", "w+") as f:
            json.dump(self.arrive_times, f)


class Person:
    #A class representation of a person. A person has a name and a mac address

    def __init__(self, name, mac_address):
        self.name = name
        self.mac_address = mac_address

    def get_name(self):
        return self.name