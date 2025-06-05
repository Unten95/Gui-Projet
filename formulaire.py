# formulaire.py
import re
import sqlite3
from PyQt5.QtWidgets import QWidget, QFormLayout, QLineEdit, QPushButton, QMessageBox
from phishing import send_phishing_email, get_company_logo


class FormulaireInscription(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Formulaire d'inscription")
        self.setFixedSize(300, 250)

        self.nom = QLineEdit()
        self.prenom = QLineEdit()
        self.email = QLineEdit()
        self.organisation = QLineEdit()

        layout = QFormLayout()
        layout.addRow("Prénom :", self.prenom)
        layout.addRow("Nom :", self.nom)
        layout.addRow("Email :", self.email)
        layout.addRow("Organisation :", self.organisation)

        bouton_envoyer = QPushButton("S'inscrire")
        bouton_envoyer.clicked.connect(self.soumettre_formulaire)
        layout.addRow(bouton_envoyer)

        self.setLayout(layout)
        self.initialiser_bdd()

    def initialiser_bdd(self):
        self.conn = sqlite3.connect("inscriptions.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS utilisateurs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                prenom TEXT,
                nom TEXT,
                email TEXT UNIQUE,
                organisation TEXT
            )
        """)
        self.conn.commit()

    def email_valide(self, email):
        return re.match(r"[^@]+@[^@]+\.[^@]+", email)

    def email_existe(self, email):
        self.cursor.execute("SELECT 1 FROM utilisateurs WHERE email = ?", (email,))
        return self.cursor.fetchone() is not None

    def soumettre_formulaire(self):
        prenom = self.prenom.text().strip()
        nom = self.nom.text().strip()
        email = self.email.text().strip()
        organisation = self.organisation.text().strip()

        if not all([nom, prenom, email, organisation]):
            QMessageBox.warning(self, "Champs manquants", "Merci de remplir tous les champs.")
            return

        if not self.email_valide(email):
            QMessageBox.warning(self, "Email invalide", "Merci de saisir une adresse mail valide.")
            return

        if self.email_existe(email):
            QMessageBox.warning(self, "Déjà inscrit", "Cette adresse mail est déjà utilisée.")
            return

        self.cursor.execute("""
            INSERT INTO utilisateurs (nom, prenom, email, organisation)
            VALUES (?, ?, ?, ?)
        """, (prenom, nom, email, organisation))
        self.conn.commit()

        full_name = f"{prenom} {nom}"
        logo_url = get_company_logo(organisation)
        send_phishing_email(email, full_name, organisation, logo_url)

        QMessageBox.information(self, "Succès", "Inscription enregistrée.")
        self.close()

    def closeEvent(self, event):
        self.conn.close()
        super().closeEvent(event)
