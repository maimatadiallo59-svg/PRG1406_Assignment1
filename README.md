# PRG1406 — Advanced Programming
## Group Assignment 1 — Clinic Management System

## What the program does
This program simulates a patient registration system for a clinic.
It collects patient information, validates all inputs, performs
health calculations, and displays a complete summary.

## Files
- `partie1.py` — Part 1 (foundations)
- `part 2.py` — Part 2 (inheritance)
- `partie3.py` — Part 3 (magic methods)
- `partie4.py` — Part 4 (decorators)
- `main.py` — Complete program combining all 4 parts

## Part 1 — Foundations
- 10 inputs with correct type casting (str, int, float, bool)
- Input validation using while loop and try/except
- Calculates BMI, consultation fees, and total expenses
- Displays a formatted summary screen using f-strings

## Part 2 — Inheritance
- Parent class: Person
- Child class: Patient inherits from Person
- Uses super().__init__() to call parent constructor
- Patient adds new attributes: weight, height, blood_type, is_member

## Part 3 — Magic Methods
- Implements __str__() to control print(patient) output

## Part 4 — Decorators
- Implements @staticmethod for BMI calculation
- calculate_bmi() is a pure function reusable without an instance

## How to run
python main.py

## Group Members
- Diallo Maimata — Part 1 & Part 2
- Ouedraogo Alimata — Part 3 (Magic Methods)
- Dakuyo Prisca Annexe — Part 4 (Decorators)
- Dah Nibouor
- Kantagba Efraim