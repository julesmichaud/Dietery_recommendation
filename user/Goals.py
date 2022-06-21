from constraint import Constraint


class Goals(Constraint) :

    def __init__(self, departure, running, arrival):
        '''
        Constructor
        '''
        self.departure = departure
        self.running = running
        self.arrival = arrival
    
    def set_departure(self, departure):
        self.departure = departure
    
    def set_running(self, running):
        self.running = running
    
    def set_arrival(self, arrival):
        self.arrival = arrival
    
    def get_departure(self):
        return self.departure

    def get_running(self):
        return self.running
    
    def get_arrival(self):
        return self.arrival