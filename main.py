# ============================================
# PRG1406 — Advanced Programming
# Group Assignment 1 — COMPLETE PROGRAM
# Domain : Clinic / Health
# ============================================
# Part 1 — Foundations         : Maïmata Diallo
# Part 2 — Inheritance         : (team member)
# Part 3 — Magic Methods       : (team member)
# Part 4 — Decorators          : (team member)
# ============================================


# ============================================
# PART 3 — Magic Methods (__str__)
# PART 4 — Decorators (@staticmethod)
# ============================================

class Person:
    """PART 2 — Parent class"""
    def __init__(self, last_name, first_name, age, phone):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.phone = phone


class Patient(Person):
    """PART 2 — Child class that inherits from Person
    PART 3 — Magic Method __str__
    PART 4 — Decorators @staticmethod
    """
    def __init__(self, last_name, first_name, age, phone,
                 weight, height, blood_type, is_member, patient_number):
        # PART 2 — Call parent constructor
        super().__init__(last_name, first_name, age, phone)
        # Child's own attributes
        self.weight = weight
        self.height = height
        self.blood_type = blood_type
        self.is_member = is_member
        self.patient_number = patient_number
        self.bmi = self.calculate_bmi(weight, height)

    # PART 4 — @staticmethod decorator
    # Reason: calculate_bmi() does not depend on self or cls.
    # It is a pure medical calculation reusable anywhere.
    @staticmethod
    def calculate_bmi(weight, height):
        """Calculates BMI from weight and height"""
        return weight / (height ** 2)

    @staticmethod
    def bmi_category(bmi):
        """Returns BMI category"""
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal weight"
        elif bmi < 30.0:
            return "Overweight"
        else:
            return "Obesity"

    # PART 3 — Magic Method __str__
    # Controls what is displayed when print(patient) is called
    def __str__(self):
        status = "Clinic member" if self.is_member else "Non-member"
        return (
            f"\n{'='*55}\n"
            f"  PATIENT FILE — {self.first_name.upper()} {self.last_name.upper()}\n"
            f"{'='*55}\n"
            f"  Patient Number  : {self.patient_number}\n"
            f"  Age             : {self.age} years old\n"
            f"  Phone           : {self.phone}\n"
            f"  Weight          : {self.weight} kg\n"
            f"  Height          : {self.height} m\n"
            f"  BMI             : {self.bmi:.2f} kg/m2\n"
            f"  BMI Category    : {self.bmi_category(self.bmi)}\n"
            f"  Blood Type      : {self.blood_type}\n"
            f"  Clinic Status   : {status}\n"
            f"{'='*55}\n"
        )


# ============================================
# PART 1 — Foundations (inputs + validation)
# ============================================

print("=" * 55)
print("    PATIENT REGISTRATION SYSTEM — CLINIC")
print("=" * 55)

# --- 1. Last name (str) ---
last_name = input("\nEnter patient last name: ").strip()

# --- 2. First name (str) ---
first_name = input("Enter patient first name: ").strip()

# --- 3. Age (int) --- with validation
while True:
    try:
        age = int(input("Enter patient age: "))
        if age <= 0 or age > 120:
            print("Invalid age. Please try again.")
        else:
            break
    except ValueError:
        print("Error! Please enter a whole number.")

# --- 4. Weight in kg (float) ---
while True:
    try:
        weight = float(input("Enter weight (kg): "))
        if weight <= 0:
            print("Invalid weight. Please try again.")
        else:
            break
    except ValueError:
        print("Error! Please enter a number. Ex: 65.5")

# --- 5. Height in meters (float) ---
while True:
    try:
        height = float(input("Enter height (m): "))
        if height <= 0 or height > 3:
            print("Invalid height. Please try again.")
        else:
            break
    except ValueError:
        print("Error! Please enter a number. Ex: 1.75")

# --- 6. Body temperature (float) ---
while True:
    try:
        temperature = float(input("Body temperature (C): "))
        if temperature < 30 or temperature > 45:
            print("Temperature out of range. Please try again.")
        else:
            break
    except ValueError:
        print("Error! Please enter a number. Ex: 37.5")

# --- 7. Blood type (str) ---
valid_blood_types = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
while True:
    blood_type = input("Blood type (ex: A+, O-, AB+): ").upper().strip()
    if blood_type in valid_blood_types:
        break
    print("Invalid blood type. Please try again.")

# --- 8. Phone number (str) ---
while True:
    phone = input("Phone number: ").strip()
    if len(phone) >= 8:
        break
    print("Number too short. Please try again.")

# --- 9. Number of visits (int) ---
while True:
    try:
        nb_visits = int(input("Number of clinic visits: "))
        if nb_visits < 0:
            print("Invalid number. Please try again.")
        else:
            break
    except ValueError:
        print("Error! Please enter a whole number.")

# --- 10. Clinic member (bool) ---
is_member = input("Is the patient a clinic member? (yes/no): ").lower() == "yes"

# --- Patient number (auto) ---
patient_number = 1001

# ============================================
# ARITHMETIC CALCULATIONS — PART 1
# ============================================

# Calculation 1 — BMI (also used by @staticmethod)
bmi = Patient.calculate_bmi(weight, height)

# Calculation 2 — Consultation fee with member discount
base_fee = 5000.0
discount = 0.20 if is_member else 0.0
final_fee = base_fee * (1 - discount)

# Calculation 3 — Total cumulative visits cost
total_spent = nb_visits * base_fee

# ============================================
# CREATE PATIENT OBJECT (uses all 4 parts)
# ============================================

patient = Patient(
    last_name, first_name, age, phone,
    weight, height, blood_type, is_member, patient_number
)

# ============================================
# FINAL SUMMARY SCREEN
# ============================================

# Uses __str__ magic method (Part 3)
print(patient)

# Additional financial summary (Part 1)
print(f"  Temperature     : {temperature} C")
print(f"  Visits          : {nb_visits}")
print(f"  Fee today       : {final_fee:.0f} FCFA")
print(f"  Total spent     : {total_spent:.0f} FCFA")
print("=" * 55)