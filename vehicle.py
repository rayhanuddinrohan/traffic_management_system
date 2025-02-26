class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type
        self.state = "Stopped"

    def move(self):
        self.state = "Moving"
        print(f"{self.vehicle_type} is now {self.state}.")

    def stop(self):
        self.state = "Stopped"
        print(f"{self.vehicle_type} is now {self.state}.")

    def __str__(self):
        return f"{self.vehicle_type} ({self.state})"
