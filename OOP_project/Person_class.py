class Person :
    def __init__(self,name,money,mood,health_rate):
        self.name=name
        self.money=money
        self.mood = mood
        self.health_rate = health_rate

    def sleep(self,hours) :
        if hours == 7 :
            self.mood = "happy"
        elif hours > 7 :
            self.mood = "lazy"
        elif  0 < hours <7 :
            self.mood = "tired"
        else :
            print("Invalid sleep time.")
        return self.mood
    
    def eat(self,meals):
        if meals == 3 :
            self.health_rate = 100
        elif meals > 1 and meals <3 :
            self.health_rate = 75
        elif meals == 1 :
            self.health_rate = 50
        else :
            return "more than 3 its gonna be useless for ur health"
        return self.health_rate
    
    def buy(self, items):
        cost = items * 10
        if self.money >= cost:
            self.money -= cost
            return self.money
        else:
            raise ValueError("Not enough money to buy the items")

    # @staticmethod
    # def calculate_health(meals):
    #     if meals == 3 :
    #         return 100
    #     elif meals == 2 :
    #         return 75
    #     elif meals ==1 :
    #         return 50
    #     else :
    #             return "more than 3 its gonna be useless for ur health"
    
# name=(input("Enter ur name please : "))
# hours= int(input("Enter the sleeping hour u have spent : "))
# meals= int(input("Enter the number of ur meals Everyday : "))
# items=int(input("how many iteams did u purchse : "))
# # health = person.calculate_health(meals)

# first_person = person(name=name, money=500, mood="neutral", health_rate= 75)
# first_person.sleep(hours)
# first_person.eat(meals)
# first_person.buy(items)

# print(f"thank you dear {name}")
# print(f"Your income is: {first_person.money} LE")
# print(f"Mood: {first_person.mood}")
# print(f"Health Rate: {first_person.health_rate}")
