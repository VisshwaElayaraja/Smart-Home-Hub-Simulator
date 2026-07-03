
import time as t
import random as r

# ===========================================================================

# Class & Function Definitions:

class SmartDevice:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.is_on = False
        self.idle_ticks = 0
        
    def Turn_on(self):
        self.is_on = True
        
    def Turn_off(self):
        self.is_on = False
        
    def increase_idle_ticks(self):
        self.idle_ticks += 1


class AirConditioner(SmartDevice):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.temperature = 24 # Default temperature in Celsius
        self.units = "C"
        self.minimum_temperatur = 16
        self.maximum_temperature = 30

    def increase_temperature(self):
        if self.temperature == self.maximum_temperature: print("Temperature is at maximum.")
        else:self.temperature += 1
    
    def decrease_temperature(self):
        if self.temperature == self.minimum_temperature: print("Temperature is at minimum.")
        else:self.temperature -= 1


class Television(SmartDevice):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.channel = 0 # Default home screen channel.
        self.volume = 15
        self.maximum_volume = 100
        self.minimum_volume = 0

    def increase_volume(self):
        if self.volume == self.maximum_volume: print("Volume is at maximum.")
        else:self.volume += 1
    
    def decrease_volume(self):
        if self.volume == self.minimum_volume: print("Volume is at minimum.")
        else:self.volume -= 1
    
    def change_channel(self, channel_number: int):
        if (channel_number > 0) and (len(str(channel_number)) <= 3):
            self.channel = channel_number
        else: print("Unvailable channel.")


# ===========================================================================

class SimulatorEngine():
    
    # Objects & Variables:
    
    pass



# MAIN
if __name__ == "__main__":
    
    print("=== STARTING CONTROL HUM SIMULATOR ===")        
    
