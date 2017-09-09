import os
import json
from threading import Lock
from bt_proximity import BluetoothRSSI
import time
import thread
import traceback
import sys
import InformationStorage

class Sensor:
    def __init__(self):
        self.info_source = InformationStorage.InformationStorage()
        temp = self.info_source.get_mac_addresses()
        self.dict_lock = Lock() #lock for the mac_dict variable
        self.mac_dict = {}
        for m in temp:
            self.mac_dict[m] = None #dictionary mapping the bluetooth addresses to signal strength

    def get_mac_dict(self):
        return self.mac_dict

    def update_dicts(self):
        """
        update the mac_dict with the latest set of bluetooth address
        strengths
        :return: None
        """
        while True:
            try:
                for m in self.mac_dict.keys():
                    time.sleep(1)
                    b = BluetoothRSSI(addr=m)
                    rssi = b.get_rssi()
                    temp =self.mac_dict[m]
                    self.dict_lock.acquire()
                    self.mac_dict[m] = rssi
                    self.dict_lock.release()
                    if self.mac_dict[m] != temp:
                        if self.mac_dict[m] is None:
                            self.log_leave(m)
                        else:
                            self.log_arrive(m)
                    self.info_source.log_goings()
            except (KeyboardInterrupt):
                message = "Exception raised in Sensor run loop, method update_dict: either Keyboard Interrupt or System exit"
                print message
                #self.dict_lock.release()
                break
            print self.mac_dict
            print "#" *30

    def run(self):
        try:
            thread.start_new_thread(self.update_dicts, ())
        except:
            message = "Failed to launch all threads in Sensor run method"
            message += "Stack Trace:/n" + traceback.format_exc()

        while True:
            try:
                time.sleep(sys.maxint)
            except KeyboardInterrupt:
                print "exit program"
                break

    def map_mac(self, mac):
        name = self.info_source.get_name(mac)
        if name != "person_not_found":
            return name
        else:
            return None

    def log_leave(self, mac):
        self.info_source.log_leave(mac)

    def log_arrive(self, mac):
        self.info_source.log_arrive(mac)
