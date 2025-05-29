from PyQt5.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout

class FenetreInfo(QWidget):
    def __init__(self, texte_intro, texte_plus):
        super().__init__()
        self.setWindowTitle("Informations supplémentaires")
        self.resize(400, 200)

        layout = QVBoxLayout()

        self.texte_initial = QLabel(texte_intro)
        self.texte_initial.setWordWrap(True)

        self.bouton_voir_plus = QPushButton("Voir plus")
        self.bouton_voir_plus.clicked.connect(self.afficher_plus)

        self.texte_plus = QLabel(texte_plus)
        self.texte_plus.setWordWrap(True)
        self.texte_plus.hide()

        layout.addWidget(self.texte_initial)
        layout.addWidget(self.bouton_voir_plus)
        layout.addWidget(self.texte_plus)

        self.setLayout(layout)

    def afficher_plus(self):
        self.texte_plus.show()
        self.bouton_voir_plus.hide()
