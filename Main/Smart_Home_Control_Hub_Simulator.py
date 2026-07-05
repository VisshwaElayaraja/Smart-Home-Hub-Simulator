
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

    def handle_power_outage(self):
        pass
    
    def handle_obstacles(self, sensor_pack):
        # Enforces all device sub-classes to override this method.
        raise NotImplementedError(f"Error: {self.__class__.__name__} missing 'handle_obstacles' method.")


class AirConditioner(SmartDevice):

    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.temperature = 24 # Default temperature in Celsius
        self.units = "C"
        self.minimum_temperature = 16
        self.maximum_temperature = 30
        self.battery_saver = True

    def increase_temperature(self):
        if self.temperature == self.maximum_temperature: print("Temperature is at maximum.")
        else:self.temperature += 1
    
    def decrease_temperature(self):
        if self.temperature == self.minimum_temperature: print("Temperature is at minimum.")
        else:self.temperature -= 1

    def switch_battery_saver(self):
        self.battery_saver = not self.battery_saver


    def handle_obstacles(self, sensor_pack):
        if (sensor_pack.global_hazard == "Fire") or (sensor_pack.smoke_detected):
            self.Turn_off()
            log = "[AC TURNED OFF]: Due to undesirable surrounding conditions.."
            print(log)

        if sensor_pack.ambient_temperature > 36:
            self.Turn_on()
            self.temperature = self.minimum_temperature
            log = "[AC TURNED ON]: Due to high ambient temperature."
            print(log)


class Television(SmartDevice):

    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.channel = 0 # Default home screen channel.
        self.volume = 15
        self.maximum_volume = 100
        self.minimum_volume = 0

    def increase_volume(self):
        if self.volume >= self.maximum_volume: self.volume = self.maximum_volume
        else:self.volume += 1
    
    def decrease_volume(self):
        if self.volume <= self.minimum_volume: self.volume = self.minimum_volume
        else: self.volume -= 1
    
    def change_channel(self, channel_number: int):
        if 0 <= channel_number <= 999:
            self.channel = channel_number
        else: print("Channel unvailable.")
    
    def handle_obstacles(self, sensor_pack):
        if (sensor_pack.global_hazard == "Fire"):
            self.Turn_off()
            log = "[TV TURNED OFF]: Due to undesirable surrounding conditions."
            print(log)
        


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
    
    def handle_obstacles(self):
        pass


# ===========================================================================


class EnvironmentalSensorSystem():

    def __init__(self):

        self.power_source = r.choice(["Main", "Main", "Main", "Battery"])

        if r.randint(1, 25) == 1: self.smoke_detected = True
        else: self.smoke_detected = False

        self.ambient_temperature = r.randint(0, 50)

        self.motion_detected = r.choice([True, False, False])

        if r.randint(1, 25) == 1: self.global_hazard = "Fire"
        else: self.global_hazard = None


# ===========================================================================


class SimulatorEngine():
    
    def __init__(self):

        self.room_devices = {
            "Living Room"   : [AirConditioner("AC", 1), Television("TV", 1), SmartFan("Fan", 1)], 
            "Master Bedroom": [AirConditioner("AC", 2), Television("TV", 2), SmartFan("Fan", 2)], 
            "Guest Bedroom" : [AirConditioner("AC", 3), SmartFan("Fan", 3)],
            "Kitchen"       : [AirConditioner("AC", 1)],
        }
        self.room_sensors = {
            "Living Room":    EnvironmentalSensorSystem(),
            "Master Bedroom": EnvironmentalSensorSystem(),
            "Guest Bedroom" : EnvironmentalSensorSystem(),
            "Kitchen"       : EnvironmentalSensorSystem(),
        }

    def check_for_hazards(self):
        for key in self.room_sensors:
            
            if self.room_sensors[key].power_source == "Battery":
                pass


# ===========================================================================


# MAIN
if __name__ == "__main__":
    
    print("=== STARTING CONTROL HUB SIMULATOR ===")        
    
