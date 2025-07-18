from Person_class import Person

class Employee(Person) :
    def __init__(self,name,money,mood,health_rate,Id,car,salary,distance_to_work) :
        super().__init__(name,money,mood,health_rate)
        self.id= Id
        self.car = car
        self.salary = salary
        self.distance_to_work = distance_to_work

    def work(self,hours):
        if hours == 8 :
            self.mood = "happy"
        elif hours > 8 :
            self.mood = "tired"
        else :
            self.mood = "lazy"
        return self.mood 
    
    def drive(self, distance, velocity):
        return self.car.run(distance, velocity)
    
    def refuel(self,gas_amount=100):
        new_fuel = self.car.fuel_rate + gas_amount
        if new_fuel > 100 :
            self.car.fuel_rate = 100
        else :
            self.car.fuel_rate = new_fuel

    def send_mail(self) :
        print(f"Sending mail from Employee {self.name}... Done.")

    def __str__(self):
        return f"Employee: {self.name} | ID: {self.id} | Salary: {self.salary} L.E | Mood: {self.mood}"

# working_hours= int(input("How many time have u been spending at ur work : ")) # Employee
