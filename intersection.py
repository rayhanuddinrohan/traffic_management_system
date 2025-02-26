from road import Road



class Intersection:

    def __init__(self):

        self.roads = []



    def add_road(self, road):

        self.roads.append(road)



    def manage_traffic(self):

       

        print("\nManaging traffic across all roads:")

        for road in self.roads:

            road.manage_traffic()

