# ============================================
# PRG1406 — Advanced Programming
# Group Assignment 1 — Partie 1
# Domaine : Clinique / Santé
# ============================================

print("=" * 50)
print("   SYSTÈME D'ENREGISTREMENT — CLINIQUE")
print("=" * 50)

# --- 1. Nom du patient (str) ---
nom = input("\nEntrez le nom du patient : ").strip()

# --- 2. Prénom (str) ---
prenom = input("Entrez le prénom : ").strip()

# --- 3. Âge (int) --- avec validation
while True:
    try:
        age = int(input("Entrez l'âge du patient : "))
        if age <= 0 or age > 120:
            print("❌ Âge invalide. Réessayez.")
        else:
            break
    except ValueError:
        print("❌ Erreur ! Entrez un nombre entier.")

# --- 4. Poids en kg (float) ---
while True:
    try:
        poids = float(input("Entrez le poids (kg) : "))
        if poids <= 0:
            print("❌ Poids invalide.")
        else:
            break
    except ValueError:
        print("❌ Erreur ! Entrez un nombre. Ex: 65.5")

# --- 5. Taille en mètres (float) ---
while True:
    try:
        taille = float(input("Entrez la taille (m) : "))
        if taille <= 0 or taille > 3:
            print("❌ Taille invalide.")
        else:
            break
    except ValueError:
        print("❌ Erreur ! Entrez un nombre. Ex: 1.75")

# --- 6. Température corporelle (float) ---
while True:
    try:
        temperature = float(input("Température corporelle (°C) : "))
        if temperature < 30 or temperature > 45:
            print("❌ Température hors limites.")
        else:
            break
    except ValueError:
        print("❌ Entrez un nombre. Ex: 37.5")

# --- 7. Groupe sanguin (str) ---
groupes_valides = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]
while True:
    groupe_sanguin = input("Groupe sanguin (ex: A+, O-, AB+) : ").upper().strip()
    if groupe_sanguin in groupes_valides:
        break
    print("❌ Groupe sanguin invalide. Réessayez.")

# --- 8. Numéro de téléphone (str) ---
while True:
    telephone = input("Numéro de téléphone : ").strip()
    if len(telephone) >= 8:
        break
    print("❌ Numéro trop court. Réessayez.")

# --- 9. Nombre de visites (int) ---
while True:
    try:
        nb_visites = int(input("Nombre de visites à la clinique : "))
        if nb_visites < 0:
            print("❌ Nombre invalide.")
        else:
            break
    except ValueError:
        print("❌ Entrez un nombre entier.")

# --- 10. Membre de la clinique (bool) ---
is_membre = input("Est-il membre de la clinique ? (oui/non) : ").lower() == "oui"

# ============================================
# CALCULS ARITHMÉTIQUES
# ============================================

# Calcul 1 — IMC
imc = poids / (taille ** 2)

# Calcul 2 — Frais de consultation
frais_base = 5000.0
reduction = 0.20 if is_membre else 0.0
frais_final = frais_base * (1 - reduction)

# Calcul 3 — Total cumulé des visites
total_depense = nb_visites * frais_base

# ============================================
# ÉCRAN RÉSUMÉ FINAL
# ============================================

print("\n" + "=" * 50)
print("         RÉSUMÉ DU PATIENT")
print("=" * 50)
print(f"  Nom complet   : {prenom} {nom}")
print(f"  Âge           : {age} ans")
print(f"  Téléphone     : {telephone}")
print(f"  Groupe sanguin: {groupe_sanguin}")
print(f"  Poids         : {poids} kg")
print(f"  Taille        : {taille} m")
print(f"  Température   : {temperature} °C")
print(f"  IMC           : {imc:.2f}")
print(f"  Membre        : {'✅ Oui' if is_membre else '❌ Non'}")
print(f"  Visites       : {nb_visites}")
print(f"  Frais today   : {frais_final:.0f} FCFA")
print(f"  Total cumulé  : {total_depense:.0f} FCFA")
print("=" * 50)