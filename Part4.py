# PART 4 — Decorators
# Decorator chosen: @staticmethod
# Reason: calculate_bmi() does not depend on self or cls.
# It is a pure medical calculation that can be reused anywhere.

class Patient:

    def __init__(self, last_name, first_name, weight, height, is_member):
        self.last_name = last_name
        self.first_name = first_name
        self.weight = weight
        self.height = height
        self.is_member = is_member

    @staticmethod
    def calculate_bmi(weight, height):
        return weight / (height ** 2)

    @staticmethod
    def bmi_category(bmi):
        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25.0:
            return "Normal weight"
        elif bmi < 30.0:
            return "Overweight"
        else:
            return "Obesity"
