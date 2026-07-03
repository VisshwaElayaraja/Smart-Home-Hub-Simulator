
import time as t
import random as r


#Class & Function Definitions:

class SmartDevice:
    def __init__(self, name):
        self.name = name
        self.is_on = False
        self.idle_ticks = 0
        
    def Turn_on(self):
        self.is_on = True
        
    def Turn_off(self):
        self.is_on = False
        
    def increase_idle_ticks(self):
        self.idle_ticks += 1


class AirConditioner(SmartDevice):
    def __init__(self, name):
        super().__init__(name)
        self.temperature = None

    def increase_temperure():
        pass


class SIMULATOR_ENGINE():
    
    # Objects & Variables:
    
    pass



# MAIN
if __name__ == "__main__":
    
    print("=== STARTING CONTROL HUM SIMULATOR ===")        
        

