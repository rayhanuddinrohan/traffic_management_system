from traffic_management_system import TrafficManagementSystem



def main():

   

    system = TrafficManagementSystem()



   

    system.setup_system()



    

    system.start_traffic_light_cycle()



   

    system.manage_traffic()



if __name__ == "__main__":

    main()
