class User() :

    def __init__(self, history, constraints):
        '''
        Constructor
        '''
        self.history = history
        self.constraints = constraints
    
    def set_history(self, history):
        self.history = history

    def set_constraints(self, constraints):
        self.constraints = constraints
    
    def get_history(self):
        return self.history

    def get_constraints(self):
        return self.constraints
        