from Person_class import Person
from emp_class import Employee
from car_class import Car
from office_class import Office

# --- Create Car instance ---
samy_car = Car("Fiat 128", 100, 80)  # fuel_rate=100%, velocity=80 km/h

# --- Create Employee instance ---
samy = Employee(
    name="Samy",
    money=500,
    mood="neutral",
    health_rate=80,
    Id=1,
    car=samy_car,
    salary=3000,
    distance_to_work=20
)

# --- Create Office instance ---
iti_office = Office("ITI Smart Village")
iti_office.hire(samy)

# --- Simulate moving at 8:00 AM ---
move_hour = 8
iti_office.check_lateness(emp_id=1, move_hour=move_hour)

# --- Simulate driving ---
samy.drive(distance=20, velocity=samy.car.velocity)

# --- Show all employees ---
print("\nAll employees in the office:")
for emp in iti_office.get_all_employees():
    print(emp)

# --- Simulate reward and deduction ---
iti_office.reward(1, 100)
iti_office.deduct(1, 50)

# --- Refuel car ---
samy.refuel(30)
print(f"\nFuel after refueling: {samy.car.fuel_rate}%")

# --- Sleep & Eat test ---
samy.sleep(7)
print(f"Mood after sleep: {samy.mood}")

samy.eat(3)
print(f"Health rate after eating: {samy.health_rate}")
