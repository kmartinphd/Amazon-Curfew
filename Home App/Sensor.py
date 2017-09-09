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
        info_source = InformationStorage.InformationStorage()
        temp = info_source.get_mac_addresses()
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
                    b= BluetoothRSSI(addr=m)
                    rssi = b.get_rssi()
                    self.dict_lock.release()
                    self.mac_dict[m] = rssi
                    self.dict_lock.release()
            except (KeyboardInterrupt, SystemExit):
                message = "Exception raised in Sensor run loop, method update_dict: either Keyboard Interrupt or System exit"
                print message
                self.dict_lock.release()
                break

            while True:
                try:
                    time.sleep(sys.maxint)
                except KeyboardInterrupt, SystemExit:
                    print "exit program"
                    break

    def run(self):
        try:
            thread.start_new_thread(self.update_dicts, ())
        except:
            message = "Failed to launch all threads in Sensor run method"
            message += "Stack Trace:/n" + traceback.format_exc()