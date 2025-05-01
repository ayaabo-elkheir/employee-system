class person:

    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate



    def sleep(self, hours):
        if hours == 7:

            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"

        else:
            self.mood = "lazy"

    def eat(self, meals):
        if meals == 3:
            self.healthrate = 100
        elif meals == 2:

            self.healthrate = 75
        elif meals == 1:

            self.healthrate = 50

    def buy(self, items):
        self.money -= 10*items


class employee(person):
    def __init__(self, name, money, mood, healthrate, id, car, email, salary, distancetowork):
        super().__init__(name, money, mood, healthrate)
        self.id = id
        self.car = car

        self.email = email
        self.salary = salary

        self.distancetowork = distancetowork

    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours > 8:

            self.mood = "tired"
        else:
            self.mood = "lazy"

    def drive(self, distance):

        self.car.run(self.car.velocity, distance)

    def refuel(self, gasamount=100):

        self.car.fuelrate = min(self.car.fuelrate + gasamount, 100)

    def send_mail(self, to, subject, body, receiver_name):

        with open("email.txt", "w") as f:

            f.write(f"to: {to}\nsubject: {subject}\nbody: {body}\nreceiver: {receiver_name}")


class car:
    def __init__(self, name, fuelrate, velocity):
        self.name = name
        self.fuelrate = max(0, min(fuelrate, 100))

        self.velocity = max(0, min(velocity, 200))

    def run(self, velocity, distance):

        self.velocity = max(0, min(velocity, 200))

        while distance > 0 and self.fuelrate > 0:
            distance -= 10

            self.fuelrate -= 10
        self.stop(distance)

    def stop(self, remaining_distance):

        self.velocity = 0

        if remaining_distance > 0:

            print(f"you stopped with {remaining_distance} km left due to no fuel.")
        else:

            print("you have arrived at your destination.")


class office:
    employeesnum = 0

    def __init__(self, name):
        self.name = name

        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empid):

        for emp in self.employees:

            if emp.id == empid:
                return emp
            
        return None

    def hire(self, employee):

        self.employees.append(employee)

        office.employeesnum += 1

    def fire(self, empid):

        self.employees = [emp for emp in self.employees if emp.id != empid]

        office.employeesnum -= 1

    def deduct(self, empid, deduction):

        emp = self.get_employee(empid)
        if emp:
            emp.salary -= deduction

    def reward(self, empid, reward):

        emp = self.get_employee(empid)
        if emp:
            emp.salary += reward

    def check_lateness(self, empid, movehour):

        emp = self.get_employee(empid)
        if emp:

            is_late = office.calculate_lateness(9, movehour, emp.distancetowork, emp.car.velocity)
            if is_late:
                self.deduct(empid, 10)
            else:
                self.reward(empid, 10)

    @staticmethod
    def calculate_lateness(targethour, movehour, distance, velocity):

        arrival_time = movehour + (distance / velocity)
        
        return arrival_time > targethour

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesnum = num
