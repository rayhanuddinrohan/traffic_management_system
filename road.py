from traffic_light import TrafficLight
from vehicle import Vehicle

class Road:
    def __init__(self, name, traffic_light=None):
        self.name = name
        self.traffic_light = traffic_light if traffic_light else TrafficLight("Red")
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def manage_traffic(self):
      
        print(f"\nManaging traffic on {self.name}:")
        for vehicle in self.vehicles:
            if self.traffic_light.color == "Green":
                vehicle.move()
            else:
                vehicle.stop()

    def __str__(self):
        return f"Road: {self.name} with Traffic Light {self.traffic_light}"
