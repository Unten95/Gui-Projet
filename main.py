# main.py
import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout,
    QHBoxLayout, QRadioButton
)
from PyQt5.QtCore import Qt
from formulaire import FormulaireInscription

class CyberEscape(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CyberEscape")
        self.setFixedSize(500, 500)

        # === Titre ===
        self.label_titre = QLabel("Cyberescape", self)
        self.label_titre.setAlignment(Qt.AlignCenter)
        self.label_titre.setStyleSheet("font-size: 20px; font-weight: bold;")

        # === Bloc vidéo avec icône œil ===
        self.label_video = QLabel("Vidéo\nd'explications", self)
        self.label_video.setAlignment(Qt.AlignCenter)

        self.bouton_oeil = QPushButton()
        self.bouton_oeil.setFixedSize(40, 40)
        self.bouton_oeil.setStyleSheet("background-color: transparent; border: 1px solid gray; border-radius: 20px;")

        video_layout = QHBoxLayout()
        video_layout.addWidget(self.label_video)
        video_layout.addWidget(self.bouton_oeil)

        # === Niveaux ===
        niveaux = ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4", "Niveau 5"]
        self.layout_niveaux = QVBoxLayout()

        for i, niveau in enumerate(niveaux):
            niveau_layout = QHBoxLayout()

            bouton_niveau = QPushButton(niveau)
            bouton_niveau.setFixedSize(120, 35)
            if i == 0:
                bouton_niveau.setStyleSheet("background-color: #4CAF50; color: white; border-radius: 5px; font-size: 14px;")
                bouton_niveau.clicked.connect(self.ouvrir_formulaire)  # Clique sur Niveau 1
            else:
                bouton_niveau.setStyleSheet("background-color: #f0f0f0; border-radius: 5px; font-size: 14px;")

            niveau_layout.addWidget(bouton_niveau)
            niveau_layout.addWidget(QLabel("3 min 07") if i == 0 else QLabel(""))

            # Radio pour validation
            niveau_layout.addWidget(QRadioButton())

            # Bouton +
            bouton_plus = QPushButton("+")
            bouton_plus.setFixedSize(35, 35)
            bouton_plus.setStyleSheet("background-color: #008CBA; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;")

            # Bouton ▶ play
            bouton_play = QPushButton("▶")
            bouton_play.setFixedSize(35, 35)
            bouton_play.setStyleSheet("background-color: #FF5733; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;")

            niveau_layout.addWidget(bouton_plus)
            niveau_layout.addWidget(bouton_play)

            self.layout_niveaux.addLayout(niveau_layout)

        # === Layout principal ===
        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.label_titre)
        layout_principal.addLayout(video_layout)
        layout_principal.addLayout(self.layout_niveaux)
        self.setLayout(layout_principal)

    def ouvrir_formulaire(self):
        self.formulaire = FormulaireInscription()
        self.formulaire.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    fenetre = CyberEscape()
    fenetre.show()
    sys.exit(app.exec_())
