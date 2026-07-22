
import time
import random
import Devices

# ===========================================================================

class EnvironmentSensorSystem():

    power_source = "Main"
    critical_hazard = None

    @classmethod
    def generate_central_sensor_readings(cls):
        cls.power_source = random.choice(["Main", "Main", "Main", "Battery"])

        if random.randint(1, 20) == 1: cls.critical_hazard = "Fire"
        else: cls.critical_hazard = None


    def generate_room_sensor_readings(self):
        if random.randint(1, 20) == 1: self.smoke_detected = True
        else: self.smoke_detected = False

        self.ambient_temperature = random.randint(0, 50)

        self.motion_detected = random.choice([True, False, False])


# ===========================================================================


class SimulatorEngine():
    
    def __init__(self):
        self.room_devices = {
            "Master Bedroom": [Devices.AirConditioner("AC", 2), Devices.Television("TV", 2), Devices.SmartFan("Fan", 2)], 
            "Guest Bedroom" : [Devices.AirConditioner("AC", 3), Devices.SmartFan("Fan", 3)],
            "Living Room"   : [Devices.AirConditioner("AC", 1), Devices.Television("TV", 1), Devices.SmartFan("Fan", 1)], 
            "Kitchen"       : [Devices.AirConditioner("AC", 1)],
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

            EnvironmentSensorSystem.generate_central_sensor_readings()
            for room in self.room_devices.keys():
                self.room_sensor_systems[room].generate_room_sensor_readings()

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
            sleep_time = float(input("Enter sleep time for every iteration:   "))
            break
        except Exception as Error:
            print(Error)

    def Main():
        Engine.start_engine(sleep_time)

    print("\n=== STARTING CONTROL HUB SIMULATOR ===")
    print(f"[   NOTE: EVERY {sleep_time} SECONDS IS COUNTED AS 1 SECOND IN THIS SIMULATOR   ]")     # Configurable sleep time for user preference and flexibility.
    Main()

# ===========================================================================
