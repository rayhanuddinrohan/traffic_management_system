from intersection import Intersection
from road import Road
from traffic_light import TrafficLight
from vehicle import Vehicle
import threading

class TrafficManagementSystem:
    def __init__(self):
        self.intersection = Intersection()

    def setup_system(self):
       
        
        traffic_light_1 = TrafficLight("Red")
        traffic_light_2 = TrafficLight("Red")
        traffic_light_3 = TrafficLight("Red")
        traffic_light_4 = TrafficLight("Red")

      
        road_1 = Road("Road 1", traffic_light_1)
        road_2 = Road("Road 2", traffic_light_2)
        road_3 = Road("Road 3", traffic_light_3)
        road_4 = Road("Road 4", traffic_light_4)

      
        road_1.add_vehicle(Vehicle("Car"))
        road_2.add_vehicle(Vehicle("Bus"))
        road_3.add_vehicle(Vehicle("Truck"))
        road_4.add_vehicle(Vehicle("Motorcycle"))

  
        self.intersection.add_road(road_1)
        self.intersection.add_road(road_2)
        self.intersection.add_road(road_3)
        self.intersection.add_road(road_4)

    def start_traffic_light_cycle(self):
      
        def light_cycle():
            while True:
                for road in self.intersection.roads:
                    road.traffic_light.run_cycle()

        light_thread = threading.Thread(target=light_cycle)
        light_thread.daemon = True
        light_thread.start()

    def manage_traffic(self):
        
        while True:
            self.intersection.manage_traffic()
