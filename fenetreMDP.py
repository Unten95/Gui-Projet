from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QLineEdit, QPushButton

class FenetreMotDePasse(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Authentification")
        self.setFixedSize(300, 150)

        self.label = QLabel("Entrez le mot de passe :")
        self.input = QLineEdit()
        self.input.setEchoMode(QLineEdit.Password)

        self.bouton_valider = QPushButton("Valider")
        self.bouton_valider.clicked.connect(self.verifier_mot_de_passe)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.bouton_valider)
        self.setLayout(layout)

    def verifier_mot_de_passe(self):
        mot_de_passe = self.input.text()
        if mot_de_passe == "cyber123":  # Exemple de mot de passe
            self.label.setText("Accès autorisé ✅")
        else:
            self.label.setText("Mot de passe incorrect ❌")
