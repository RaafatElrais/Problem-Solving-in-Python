class Car : 
    def __init__(self,name,fuel_rate,velocity) :
        self.name = name
        self.fuel_rate = fuel_rate
        self.velocity = velocity
    @property
    def velocity(self):
        return self._velocity
    @velocity.setter
    def velocity(self, value):
        if 0 <= value <= 200:
            self._velocity = value
        else:
            print("Velocity must be between 0 and 200.")
            self._velocity = 0
    @property
    def fuel_rate(self) :
        return self._fuel_rate
    @fuel_rate.setter
    def fuel_rate(self,value) :
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            print("fuel Rate must be between 0 and 100.")
            self._fuel_rate = 0

    def run(self, distance, velocity):
        self.velocity = velocity
        # 2. Calculate time
        if velocity == 0:
            print("Velocity cannot be zero. Cannot calculate time.")
            return 
        time = distance / velocity
        print(f"{self.name} is running for {distance} km at {velocity} km/h.")
        print(f"It will take {time:.2f} hours.")
        #3. calculate how much fuel is needed because 1km = 1%fuel
        
        fuel_needed = distance  
        # 4. Check if enough fuel is available
        if self.fuel_rate >= fuel_needed :
            self.fuel_rate -= fuel_needed
            distance_remaining = 0
            print(" Arrived at ur Destination.")
        else :
            distance_traveled = self.fuel_rate
            distance_remaining= distance - distance_traveled
            print(f" Fuel ran out after {distance_traveled} km.")
            print(f" Still need to travel {distance_remaining} km.")
            self.fuel_rate = 0
        self.stop(distance_remaining)

    def stop(self,remaining_distance):
        self.velocity = 0
        if remaining_distance > 0 :
            print(f"u do have {remaining_distance} KM remainig.\n safe journey")
        else :
            print(" You've arrived at ur destination ")

