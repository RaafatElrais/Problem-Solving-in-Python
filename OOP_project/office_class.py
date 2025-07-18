class Office :
    
    employee_num = 0 

    def __init__(self,name) :
        self.name=name
        self.employees = []

    def get_all_employees(self):
        return self.employees
    
    def get_employee(self,emp_id):
        for emp in self.employees :
            if emp.id == emp_id :
                return emp
        return None
    
    def hire(self,employee):
        self.employees.append(employee)
        Office.employee_num += 1

        return self.employees
    
    # with id only will be more relistic in systems we dont need the full object to remove with employee instead of id
    def fire(self,emp_id) :
        for emp in self.employees :
            if emp.id == emp_id :
                self.employees.remove(emp)
                Office.employee_num -= 1

                return f"Fired {emp.name}"
        else :
            print("Empolyee Not Found")
        return self.employees

    def deduct(self,emp_id,amount) :
        for emp in self.employees :
            if emp.id==emp_id :
                emp.salary -= amount 
                print(f"{emp.name}'s salary has been deducted by {amount}.")
                return
        else:
            print("Employee not found.")

    def reward(self,emp_id,amount) :
        for emp in self.employees :
            if emp.id==emp_id :
                emp.salary += amount 
                print(f"{emp.name}'s salary has been increased by {amount}.")
                return
        else:
            print("Employee not found.")
    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        """
        Calculates whether the employee is late based on target hour, 
        movement time, distance to work, and car velocity.
        """
        travel_time = distance / velocity  # in hours
        arrival_time = move_hour + travel_time

        # Employee is late if they arrive after the target hour
        return arrival_time > target_hour
        
    def check_lateness(self, emp_id, move_hour):
        emp = self.get_employee(emp_id)
        if emp:
            distance = emp.distance_to_work
            velocity = emp.car.velocity
            target_hour = 9  # Assume target arrival time is 9:00 AM

            is_late = Office.calculate_lateness(target_hour, move_hour, distance, velocity)

            if is_late:
                self.deduct(emp_id, 10)
                print(f"{emp.name} is late! 10 L.E deducted.")
            else:
                self.reward(emp_id, 10)
                print(f"{emp.name} arrived on time. 10 L.E reward added.")
        else:
            print("Employee not found.")

    @classmethod
    def change_emps_num(cls, num):
        cls.employee_num = num