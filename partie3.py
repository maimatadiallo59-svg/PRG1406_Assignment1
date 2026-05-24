class Patient:
    def __init__(self, last_name, first_name, age, weight, height, blood_type, phone, is_member, patient_number):
        """Constructor — initializes all patient attributes"""
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.weight = weight
        self.height = height
        self.blood_type = blood_type
        self.phone = phone
        self.is_member = is_member
        self.patient_number = patient_number
        self.bmi = weight / (height ** 2)

    def interpret_bmi(self):
        """Interprets the BMI value"""
        if self.bmi < 18.5:
            return "Underweight"
        elif self.bmi < 25:
            return "Normal weight"
        elif self.bmi < 30:
            return "Overweight"
        else:
            return "Obesity"

    def __str__(self):
        """Magic Method __str__
        Controls what is displayed when print(patient) is called
        """
        status = "Clinic member" if self.is_member else "Non-member"
        return (
            f"\n{'='*55}\n"
            f"PATIENT FILE — {self.first_name.upper()} {self.last_name.upper()}\n"
            f"{'='*55}\n"
            f"Patient Number     : {self.patient_number}\n"
            f"Age                : {self.age} years old\n"
            f"Phone              : {self.phone}\n"
            f"Weight             : {self.weight} kg\n"
            f"Height             : {self.height} m\n"
            f"BMI                : {self.bmi:.2f} kg/m²\n"
            f"Interpretation     : {self.interpret_bmi()}\n"
            f"Clinic Status      : {status}\n"
            f"{'='*55}\n"
        )


# Test
p = Patient("Mensah", "Kofi", 25, 70.5, 1.75, "A+", "0701020304", True, 1)
print(p)