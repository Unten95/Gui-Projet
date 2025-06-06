from PyQt5.QtWidgets import (
    QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QMessageBox, QGraphicsOpacityEffect
)
from PyQt5.QtCore import Qt, QTimer, QPropertyAnimation
from PyQt5.QtMultimedia import QSound

class FenetreOsint(QWidget):
    def __init__(self, callback_suivant):
        super().__init__()
        self.setWindowTitle("Analyse OSINT - Instagram")
        self.setFixedSize(320, 180)
        self.callback_suivant = callback_suivant

        # Widgets
        self.label = QLabel("🕵️‍♀️ Pour accéder au niveau 2,\nrenseignez votre identifiant Instagram :")
        self.label.setAlignment(Qt.AlignCenter)

        self.input = QLineEdit()
        self.input.setPlaceholderText("ex: john_doe_123")

        self.bouton_valider = QPushButton("🔍 Lancer l'analyse")
        self.bouton_valider.clicked.connect(self.valider_identifiant)

        self.label_animation = QLabel("🧠 Analyse en cours...", self)
        self.label_animation.setAlignment(Qt.AlignCenter)
        self.label_animation.setStyleSheet("font-size: 14px; color: green; font-weight: bold;")
        self.label_animation.setVisible(False)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.input)
        layout.addWidget(self.bouton_valider)
        layout.addWidget(self.label_animation)
        self.setLayout(layout)

    def valider_identifiant(self):
        identifiant = self.input.text().strip()
        if identifiant:
            self.lancer_animation_opacite()
            QTimer.singleShot(1600, lambda: self.finir_validation(identifiant))
        else:
            QMessageBox.warning(self, "Erreur", "❗ Veuillez saisir un identifiant.")

    def lancer_animation_opacite(self):
        self.label_animation.setVisible(True)
        effet = QGraphicsOpacityEffect(self.label_animation)
        self.label_animation.setGraphicsEffect(effet)

        self.animation = QPropertyAnimation(effet, b"opacity")
        self.animation.setDuration(1500)
        self.animation.setStartValue(0)
        self.animation.setEndValue(1)
        self.animation.start()

    def finir_validation(self, identifiant):
        self.jouer_son_validation()
        QMessageBox.information(
            self,
            "Analyse terminée",
            f"🕵️‍♂️ Pseudo enregistré : {identifiant}"
        )
        self.callback_suivant(identifiant)
        self.close()

    def jouer_son_validation(self):
        try:
            QSound.play("sons/hacking_bip.wav")  # Assurez-vous que le fichier existe ici
        except Exception as e:
            print("Erreur de lecture audio :", e)
