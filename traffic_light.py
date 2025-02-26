import time

class TrafficLight:
    def __init__(self, color="Red"):
        self.color = color

    def change(self):
       
        if self.color == "Red":
            self.color = "Green"
        elif self.color == "Green":
            self.color = "Yellow"
        elif self.color == "Yellow":
            self.color = "Red"

    def __str__(self):
        return f"Traffic Light is {self.color}"

    def run_cycle(self):
       
        while True:
            print(self)
            time.sleep(1) 
            self.change()
