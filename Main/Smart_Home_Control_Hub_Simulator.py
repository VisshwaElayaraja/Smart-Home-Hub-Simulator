
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
        self.minimum_temperature = 16
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
        if 0 <= channel_number <= 999:
            self.channel = channel_number
        else: print("Channel unvailable.")


class SmartFan(SmartDevice):
    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.speed = 3
        self.maximum_speed = 6
        self.minimum_speed = 0
    
    def auto_power_by_speed(self):
        if self.speed == self.minimum_speed: self.is_on = False
        else: self.is_on = True

    def increase_speed(self):
        if self.speed == self.maximum_speed: print("Speed is at maximum")
        else: self.speed += 1
        self.auto_power_by_speed()

    def decrease_speed(self):
        if self.speed == self.minimum_speed: print("Speed is at minimum")
        else: self.speed -= 1
        self.auto_power_by_speed()

# ===========================================================================

class SimulatorEngine():
    
    # Objects & Variables:
    
    pass



# MAIN
if __name__ == "__main__":
    
    print("=== STARTING CONTROL HUB SIMULATOR ===")        
    
