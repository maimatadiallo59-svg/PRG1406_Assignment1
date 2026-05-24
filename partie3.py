class Patient:
    def __init__(self, nom, prenom, age, poids, taille, groupe_sanguin, telephone, est_membre, numero_patient):
        """Constructeur — initialise tous les attributs du patient"""
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.poids = poids          # float en kg
        self.taille = taille        # float en mètres
        self.groupe_sanguin = groupe_sanguin
        self.telephone = telephone
        self.est_membre = est_membre  # bool
        self.numero_patient = numero_patient
        self.imc = poids / (taille ** 2)  # calcul automatique

    def interpreter_imc(self):
        """Interprète la valeur de l'IMC"""
        if self.imc < 18.5:
            return "Insuffisance pondérale"
        elif self.imc < 25:
            return "Poids normal"
        elif self.imc < 30:
            return "Surpoids"
        else:
            return "Obésité"

    def __str__(self):
        """Magic Method __str__
        Contrôle ce qui s'affiche quand on fait print(patient)
        """
        statut = "Membre de la clinique" if self.est_membre else "Non-membre"
        return (
            f"\n{'='*55}\n"
            f"FICHE PATIENT — {self.prenom.upper()} {self.nom.upper()}\n"
            f"{'='*55}\n"
            f"Numéro Patient     : {self.numero_patient}\n"
            f"Âge                : {self.age} ans\n"
            f"Téléphone          : {self.telephone}\n"
            f"Poids              : {self.poids} kg\n"
            f"Taille             : {self.taille} m\n"
            f"IMC                : {self.imc:.2f} kg/m²\n"
            f"Interprétation     : {self.interpreter_imc()}\n"
            f"Statut Clinique    : {statut}\n"
            f"{'='*55}\n"
        )


# Test en dehors de la classe
p = Patient("Mensah", "Kofi", 25, 70.5, 1.75, "A+", "0701020304", True, 1)
print(p)