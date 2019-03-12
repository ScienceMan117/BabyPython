class RandomEmployee():
    
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.information = []
    
    def give_raise(self, salary):
        self.salary = salary + 5000
        
