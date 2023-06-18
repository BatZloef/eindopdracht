from user import *
from bike import *
from station import *

class Log:
    def __init__(self,naam):
        self.log = []
    def add_log(self,user,action,station,bike):
        log = f"{user.naam} {action} {bike.id} at {station.naam}"
        print(log)
