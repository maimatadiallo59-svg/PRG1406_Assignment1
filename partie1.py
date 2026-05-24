# ============================================
# PRG1406 — Advanced Programming
# Group Assignment 1 — Part 1
# Domain : Clinic / Health
# ============================================

print("=" * 50)
print("   PATIENT REGISTRATION SYSTEM — CLINIC")
print("=" * 50)

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

# ============================================
# ARITHMETIC CALCULATIONS
# ============================================

# Calculation 1 — BMI
bmi = weight / (height ** 2)

# Calculation 2 — Consultation fee
base_fee = 5000.0
discount = 0.20 if is_member else 0.0
final_fee = base_fee * (1 - discount)

# Calculation 3 — Total cumulative visits cost
total_spent = nb_visits * base_fee

# ============================================
# FINAL SUMMARY SCREEN
# ============================================

print("\n" + "=" * 50)
print("           PATIENT SUMMARY")
print("=" * 50)
print(f"  Full name     : {first_name} {last_name}")
print(f"  Age           : {age} years")
print(f"  Phone         : {phone}")
print(f"  Blood type    : {blood_type}")
print(f"  Weight        : {weight} kg")
print(f"  Height        : {height} m")
print(f"  Temperature   : {temperature} C")
print(f"  BMI           : {bmi:.2f}")
print(f"  Member        : {'Yes' if is_member else 'No'}")
print(f"  Visits        : {nb_visits}")
print(f"  Fee today     : {final_fee:.0f} FCFA")
print(f"  Total spent   : {total_spent:.0f} FCFA")
print("=" * 50)