# ============================================
# PRG1406 — Advanced Programming
# Group Assignment 1 — Part 2
# Domain : Clinic / Health
# Part 2 — Inheritance
# ============================================

# PARENT CLASS
class Person:
    def __init__(self, last_name, first_name, age, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.phone = phone

    def introduce(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, Phone: {self.phone}"


# CHILD CLASS — Patient IS a Person
class Patient(Person):
    def __init__(self, last_name, first_name, age, phone,
                 weight, height, blood_type, is_member):
        # Call parent constructor
        super().__init__(last_name, first_name, age, phone)
        # New attributes specific to Patient
        self.weight = weight
        self.height = height
        self.blood_type = blood_type
        self.is_member = is_member

    def get_status(self):
        status = "Clinic member" if self.is_member else "Non-member"
        return f"Blood type: {self.blood_type} | Status: {status}"


# Test
p = Patient("Diallo", "Awa", 33, "66244723", 56.0, 1.6, "O-", True)
print(p.introduce())
print(p.get_status())