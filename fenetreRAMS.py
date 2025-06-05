# fenetreNiveau4.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtGui import QDesktopServices
from PyQt5.QtCore import Qt, QUrl
import os

class FenetreNiveau4(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mission - Niveau 4 : Cryptographie")
        self.setFixedSize(500, 300)

        layout = QVBoxLayout()

        instructions = (
            "🕵️ Étapes de la mission :\n\n"
            "1. Explorez le site suspect hébergé localement.\n"
            "2. Téléchargez le fichier .exe caché sur le site.\n"
            "3. Analysez le malware (strings, Ghidra, Pyinstxtractor).\n"
            "4. Trouvez la méthode de chiffrement utilisée.\n"
            "5. Récupérez la clé de déchiffrement pour aider la banque.\n\n"
            "💡 Objectif : Identifier la clé AES cachée dans le binaire.\n"
        )

        label = QLabel(instructions)
        label.setWordWrap(True)
        label.setAlignment(Qt.AlignLeft)
        layout.addWidget(label)

        bouton_ouvrir_site = QPushButton("🌐 Ouvrir le site compromis")
        bouton_ouvrir_site.setStyleSheet("font-size: 14px; padding: 10px; background-color: #FF5733; color: white;")
        bouton_ouvrir_site.clicked.connect(self.ouvrir_site_malveillant)
        layout.addWidget(bouton_ouvrir_site)

        self.setLayout(layout)

    def ouvrir_site_malveillant(self):
        chemin_absolu = os.path.abspath("index.html")  # Assure le chemin absolu
        url = QUrl.fromLocalFile(chemin_absolu)
        QDesktopServices.openUrl(url)