
import time
import random

# ===========================================================================

# Class & Function Definitions:

class SmartDevice:

    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id
        self.is_on = False
        self.idle_ticks = 0
        self.maximum_idle_time = 20

    def Log_Activity(self, log):
        print(log)

    def turn_on(self):
        self.is_on = True
        
    def turn_off(self):
        self.is_on = False

    def has_idle_timed_out(self):
        if self.idle_ticks == self.maximum_idle_time:
            self.turn_off()
            self.idle_ticks = 0
        
    def automated_motion_detection(self, sensor_pack):
        if sensor_pack.motion_detected and (not self.is_on):
            self.turn_on()
            self.Log_Activity(f"[{self.name.upper()} TURNED ON]: Due to room occupancy.")
        else:
            self.idle_ticks += 1

    def handle_power_outage(self, sensor_pack):
        # Default Rule: If the power source is switched to 'Battery', turn_off all appliances.
        if sensor_pack.power_source != "Main" and (self.is_on):
            self.turn_off()
    
    def handle_obstacles_and_requirements(self, sensor_pack):
        # Enforces all device sub-classes to override this method.
        raise NotImplementedError(f"Error: {self.__class__.__name__} missing 'handle_obstacles_and_requirements' method.")


class AirConditioner(SmartDevice):

    def __init__(self, name: str, id: int):
        super().__init__(name, id)
        self.temperature = 24 # Default temperature in Celsius.
        self.units = "C"
        self.minimum_temperature = 16
        self.maximum_temperature = 30
        self.battery_saver_is_on = False

    def increase_temperature(self):
        if self.temperature == self.maximum_temperature: print("Temperature is at maximum.")
        else:self.temperature += 1
    
    def decrease_temperature(self):
        if self.temperature == self.minimum_temperature: print("Temperature is at minimum.")
        else:self.temperature -= 1

    def switch_battery_saver(self):
        self.battery_saver_is_on = not self.battery_saver_is_on
        if self.battery_saver_is_on: self.minimum_temperature = 24
        else: self.minimum_temperature = 16

    def handle_power_outage(self, sensor_pack):
        if sensor_pack.power_source != "Main" and (not self.battery_saver_is_on):
            self.switch_battery_saver()
            self.Log_Activity("[AC BATTERY SAVER ON]: Due to power outage.")
        elif sensor_pack.power_source == "Main" and (self.battery_saver_is_on):
            self.switch_battery_saver()
            self.Log_Activity("[AC BATTERY SAVER OFF]: Due to power restoration.")

    def handle_obstacles_and_requirements(self, sensor_pack):
        self.automated_motion_detection(sensor_pack)
        self.handle_power_outage(sensor_pack)

        if (sensor_pack.global_hazard == "Fire" or sensor_pack.smoke_detected) and (self.is_on):
            self.turn_off()
            self.Log_Activity("[AC TURNED OFF]: Due to undesirable surrounding conditions.")

        if sensor_pack.ambient_temperature > 36  and (not self.is_on):
            self.turn_on()
            self.temperature = self.minimum_temperature
            self.Log_Activity("[AC TURNED ON]: Due to high ambient temperature.")

        self.has_idle_timed_out()


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
    
    def handle_obstacles_and_requirements(self, sensor_pack):
        self.automated_motion_detection(sensor_pack)
        self.handle_power_outage(sensor_pack)

        if (sensor_pack.global_hazard == "Fire") and (self.is_on):
            self.turn_off()
            self.Log_Activity("[TV TURNED OFF]: Due to undesirable surrounding conditions.")

        self.has_idle_timed_out()


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

    def handle_power_outage(self, sensor_pack):
        if sensor_pack.power_source != "Main":
            self.speed = 1
            self.maximum_speed = 2
        elif sensor_pack.power_source == "Main" and (self.maximum_speed != 6):
            self.speed = 3
            self.maximum_speed = 6
    
    def handle_obstacles_and_requirements(self, sensor_pack):
        self.automated_motion_detection(sensor_pack)
        self.handle_power_outage(sensor_pack)

        if (sensor_pack.global_hazard == "Fire" or sensor_pack.smoke_detected) and (not self.is_on):
            self.turn_on()
            self.speed = self.maximum_speed
            self.Log_Activity("[Fan Set to Max Speed]: To eliminate undesirable surrounding conditions.")

        self.has_idle_timed_out()


# ===========================================================================


class EnvironmentSensorSystem():

    power_source = random.choice(["Main", "Main", "Main", "Battery"])

    def generate_sensor_readings(self):

        if random.randint(1, 20) == 1: self.smoke_detected = True
        else: self.smoke_detected = False

        self.ambient_temperature = random.randint(0, 50)

        self.motion_detected = random.choice([True, False, False])

        if random.randint(1, 20) == 1: self.global_hazard = "Fire"
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

        self.room_sensor_systems = {
            "Living Room":    EnvironmentSensorSystem(),
            "Master Bedroom": EnvironmentSensorSystem(),
            "Guest Bedroom" : EnvironmentSensorSystem(),
            "Kitchen"       : EnvironmentSensorSystem(),
        }

    def manage_obstacles_and_requirements(self):
        for no, (room, device_list) in enumerate(self.room_devices.items(), 1):
            if room in self.room_sensor_systems:
                current_system = self.room_sensor_systems[room]
                print(f"{no}) Devices of {room.upper()}:")
                for device in device_list:
                    device.handle_obstacles_and_requirements(current_system)
                print()

    def start_engine(self, sleep_time):
        run_time = 0
        while True:
            
            print(f"\n*****===== RUN TIME : {run_time} =====*****")  

            for room in self.room_devices.keys():
                self.room_sensor_systems[room].generate_sensor_readings()

            self.manage_obstacles_and_requirements()

            run_time += 1
            time.sleep(sleep_time)
            # cmd = input("Press 'Enter' (or) 'Return' to continue: ")

# ===========================================================================


# MAIN
if __name__ == "__main__":
    
    Engine = SimulatorEngine()

    while True:
        try:
            sleep_time = int(input("Enter sleep time for every iteration:   "))
            break
        except Exception as Error:
            print(Error)

    def Main():
        Engine.start_engine(sleep_time)

    print("\n=== STARTING CONTROL HUB SIMULATOR ===")
    print(f"[   NOTE: EVERY {sleep_time} SECONDS IS COUNTED AS 1 SECOND IN THIS SIMULATOR   ]")     # Configurable sleep time for user preference and flexibility.
    Main()
