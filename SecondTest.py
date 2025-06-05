from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QFrame
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtCore import QTimer, QTime
from fenetreMDP import FenetreMotDePasse
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QLineEdit
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtGui import QPalette
from fenetreOSINT import FenetreOsint
from fenetreRAMS import FenetreNiveau4
from fenetreSpoofing import FenetreSpoofing



from formulaire import FormulaireInscription

from AstuceWindow import FenetreInfo
from VideoWindow import FenetreVideo


class CyberEscape(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Cyberescape")
        self.setFixedSize(500, 500)

        self.labels_temps = {}
        self.temps_debut_niveaux = {}
        self.boutons_niveaux = {}

        self.textes_niveaux = {
            "Niveau 1": ("Bienvenue dans le premier niveau !", "Vous apprendrez à détecter des mails frauduleux."),
            "Niveau 2": ("Ce niveau teste votre mémoire.", "Vous devrez retenir un mot de passe complexe."),
            "Niveau 3": ("Un défi réseau vous attend.", "Configurez un pare-feu pour bloquer les attaques."),
            "Niveau 4": ("🧩 Mission : Bienvenue dans la Cryptographie !" , "🔐 Un employé d'une grande banque a téléchargé par erreur un fichier exécutable à partir d’un site de streaming. Ce fichier contenait un ransomware qui a chiffré tous les documents confidentiels de l’entreprise. \n💻 Votre mission est cruciale : retracer les étapes de l'attaque pour comprendre comment les données ont été chiffrées, et tenter de retrouver la clé de déchiffrement."),
            "Niveau 5": ("Le défi final approche !", "Protégez un système complet contre une attaque.")
        }

        self.mots_de_passe_niveaux = {
            "Niveau 1": "cyber01",
            "Niveau 2": "cyber02",
            "Niveau 3": "cyber03",
            "Niveau 4": "cyber04",
            "Niveau 5": "cyber05"
        }

        # Créer un QLabel pour afficher l'image du logo
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(
            "D:\\Gui-Projet\\CyberEscape2.png")  # Remplacez par le chemin réel de votre logo
        # Redimensionne l'image
        self.logo_pixmap = self.logo_pixmap.scaled(200, 200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.logo_label.setPixmap(self.logo_pixmap)
        self.logo_label.setAlignment(Qt.AlignCenter)
        # Chronomètre 1h
        self.secondes_restantes = 3600  # 1h = 3600 secondes
        self.label_chrono = QLabel("01:00:00")
        self.label_chrono.setAlignment(Qt.AlignCenter)
        self.label_chrono.setStyleSheet("font-size: 18px; color: red; font-weight: bold;")
        # Player vidéo
        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        # Label vidéo
        self.label_video = QLabel("Vidéo\nd'explications", self)
        self.label_video.setAlignment(Qt.AlignCenter)
        video_layout = QHBoxLayout()
        video_layout.addWidget(self.label_video)
        # Liste des niveaux
        niveaux = ["Niveau 1", "Niveau 2", "Niveau 3", "Niveau 4", "Niveau 5"]
        self.layout_niveaux = QVBoxLayout()
        # Chronometre
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.mettre_a_jour_chronometre)
        self.timer.start(1000)  # toutes les 1 seconde

        for i, niveau in enumerate(niveaux):
            niveau_layout = QHBoxLayout()

            bouton_niveau = QPushButton(niveau)
            bouton_niveau.setFixedSize(120, 35)
            if i == 0:
                bouton_niveau.setStyleSheet("background-color: #FFCC33; border-radius: 5px; font-size: 14px;")
                bouton_niveau.clicked.connect(self.ouvrir_formulaire)  # Clique sur Niveau 1

            elif i == 1:
                bouton_niveau.setStyleSheet("background-color: #FFCC33; border-radius: 5px; font-size: 14px;")
                bouton_niveau.clicked.connect(self.ouvrir_fenetre_osint)
            elif i == 2:
                bouton_niveau.setStyleSheet("background-color: #FFCC33; border-radius: 5px; font-size: 14px;")
                bouton_niveau.clicked.connect(self.ouvrir_fenetre_spoofing)
            elif i == 3:  # Niveau 4
                bouton_niveau.setStyleSheet("background-color: #FFCC33; border-radius: 5px; font-size: 14px;")
                bouton_niveau.clicked.connect(self.ouvrir_fenetre_niveau4)
            else:
                bouton_niveau.setStyleSheet("background-color: #FFCC33; border-radius: 5px; font-size: 14px;")
                bouton_niveau.clicked.connect(lambda _, n=niveau: self.ouvrir_info_niveau(n))

            label_temps = QLabel(f"Temps :")
            self.labels_temps[niveau] = label_temps
            self.boutons_niveaux[niveau] = bouton_niveau

            radio_bouton = QRadioButton()
            radio_bouton.toggled.connect(
                lambda checked, n=niveau, r=radio_bouton: self.verifier_mot_de_passe(n, r) if checked else None)

            bouton_plus = QPushButton("+")
            bouton_plus.setFixedSize(35, 35)
            bouton_plus.setStyleSheet(
                "background-color: #008CBA; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;")
            bouton_plus.pressed.connect(lambda btn=bouton_plus: btn.setStyleSheet(
                "background-color: #005f7f; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;"))
            bouton_plus.released.connect(lambda btn=bouton_plus: btn.setStyleSheet(
                "background-color: #008CBA; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;"))

            bouton_play = QPushButton("▶")
            bouton_play.setFixedSize(35, 35)
            bouton_play.setStyleSheet(
                "background-color: #FF5733; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;")
            bouton_play.pressed.connect(lambda btn=bouton_play: btn.setStyleSheet(
                "background-color: #b23c21; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;"))
            bouton_play.released.connect(lambda btn=bouton_play: btn.setStyleSheet(
                "background-color: #FF5733; border-radius: 17px; color: white; font-weight: bold; font-size: 16px;"))

            if i == 0:
                bouton_play.clicked.connect(lambda: self.lancer_video("D:/Gui-Projet/ILOVE.mp4"))

            bouton_plus.clicked.connect(lambda checked=False, n=niveau: self.ouvrir_info_niveau(n))

            niveau_layout.addWidget(bouton_niveau)
            niveau_layout.addWidget(label_temps)
            niveau_layout.addWidget(radio_bouton)
            niveau_layout.addWidget(bouton_plus)
            niveau_layout.addWidget(bouton_play)

            self.layout_niveaux.addLayout(niveau_layout)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.logo_label)  # Ajoute le logo au layout
        layout_principal.addLayout(video_layout)
        layout_principal.addLayout(self.layout_niveaux)
        layout_principal.addWidget(self.label_chrono)
        self.setLayout(layout_principal)

    def lancer_video(self, chemin_video):
        self.fenetre_video = FenetreVideo(chemin_video)
        self.fenetre_video.show()

    def ouvrir_info_niveau(self, niveau):
        texte_intro, texte_plus = self.textes_niveaux.get(niveau, ("Texte indisponible", ""))
        self.fenetre_info = FenetreInfo(texte_intro, texte_plus)
        self.fenetre_info.show()

        if niveau not in self.temps_debut_niveaux:
            self.temps_debut_niveaux[niveau] = QTime.currentTime()

    def mettre_a_jour_chronometre(self):
        if self.secondes_restantes > 0:
            self.secondes_restantes -= 1
            heures = self.secondes_restantes // 3600
            minutes = (self.secondes_restantes % 3600) // 60
            secondes = self.secondes_restantes % 60
            self.label_chrono.setText(f"{heures:02d}:{minutes:02d}:{secondes:02d}")
        else:
            self.timer.stop()
            self.label_chrono.setText("Temps écoulé !")
            self.label_chrono.setStyleSheet("font-size: 18px; color: gray; font-weight: bold;")

    def ouvrir_mot_de_passe(self):
        self.fenetre_mdp = FenetreMotDePasse()
        self.fenetre_mdp.show()

    def verifier_mot_de_passe(self, niveau, bouton_radio):
        mot_de_passe_correct = self.mots_de_passe_niveaux.get(niveau)
        mot_saisi, ok = QInputDialog.getText(self, f"Mot de passe - {niveau}", "Entrez le mot de passe :",
                                             echo=QLineEdit.Password)

        if ok:
            if mot_saisi == mot_de_passe_correct:
                bouton_radio.setChecked(True)
                # Calcule le temps passé dans le niveau
                temps_debut = self.temps_debut_niveaux.get(niveau, QTime.currentTime())
                temps_actuel = QTime.currentTime()
                secondes_passees = temps_debut.secsTo(temps_actuel)

                heures = secondes_passees // 3600
                minutes = (secondes_passees % 3600) // 60
                secondes = secondes_passees % 60
                texte_temps = f"✔ Fini en {heures:02d}:{minutes:02d}:{secondes:02d}"

                # Met à jour la couleur du bouton de niveau en vert
                bouton_niveau = self.boutons_niveaux.get(niveau)
                if bouton_niveau:
                    bouton_niveau.setStyleSheet("""
                        background-color: #4CAF50;
                        color: white;
                        border-radius: 5px;
                        font-size: 14px;
                        font-weight: bold;
                    """)

                self.mettre_a_jour_label_temps(niveau, texte_temps)
                bouton_radio.setStyleSheet("""
                    background-color: #4CAF50;  /* Vert lorsque correct */
                    color: white;  /* Texte en blanc */
                    border: 2px solid #388E3C;  /* Bordure verte foncée */
                    font-weight: bold;  /* Texte en gras */
                """)

                # Griser le bouton après validation (mais lui laisser un aspect joli)
                bouton_radio.setStyleSheet("""
                    background-color: #B2FF59;  /* Vert pâle pour l'état terminé */
                    color: gray;  /* Texte gris */
                    border: 2px solid #66BB6A;  /* Bordure verte plus claire */
                    font-weight: bold;
                """)
                bouton_radio.setEnabled(False)  # Empêche de cliquer à nouveau

            else:
                QMessageBox.warning(self, "Erreur", "Mot de passe incorrect.")
                bouton_radio.setChecked(False)

    def ouvrir_formulaire(self):
        self.formulaire = FormulaireInscription()
        self.formulaire.show()

    def ouvrir_fenetre_niveau4(self):
        self.fenetre_niv4 = FenetreNiveau4()
        self.fenetre_niv4.show()

    def mettre_a_jour_label_temps(self, niveau, nouveau_texte):
        if niveau in self.labels_temps:
            self.labels_temps[niveau].setText(nouveau_texte)

    def ouvrir_fenetre_osint(self):
        self.fenetre_osint = FenetreOsint(self.lancer_niveau_2_apres_osint)
        self.fenetre_osint.show()

    def ouvrir_fenetre_spoofing(self):
        self.fenetre_spoof = FenetreSpoofing()
        self.fenetre_spoof.show()

    def lancer_niveau_2_apres_osint(self, identifiant):
        QMessageBox.information(self, "Dictionnaire généré", f"Un pseudo a été enregistré : {identifiant}")

        # Génération d’un dictionnaire simple pour simulation
        variantes = [
            identifiant,
            identifiant + "123",
            identifiant + "2024",
            identifiant.upper(),
            identifiant[::-1],
            "@" + identifiant,
            identifiant + "!"
        ]

        # Sauvegarde dans un fichier texte
        with open("dictionnaire_instagram.txt", "w") as f:
            for mot in variantes:
                f.write(mot + "\n")

        # Ensuite, on lance les infos du niveau 2
        self.ouvrir_info_niveau("Niveau 2")


# Lancer l'application
app = QApplication([])
fenetre = CyberEscape()
fenetre.show()
app.exec_()