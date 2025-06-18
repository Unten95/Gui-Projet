from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QRadioButton, QFrame
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QDialog,QScrollArea
from PyQt5.QtCore import Qt, QUrl, QTimer, QTime
from fenetreMDP import FenetreMotDePasse
from PyQt5.QtWidgets import QInputDialog, QMessageBox, QLineEdit, QCheckBox
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
            "Niveau 1": (
            "🔍 Objectif :Apprenez à identifier un mail frauduleux, même lorsqu’il semble provenir d’une source de confiance.",
            "\n💡Astuce :Inspectez l'expéditeur, le contenu du lien, et posez-vous les bonnes questions : Est-ce que ce mail est attendu ? Y a-t-il des fautes ? Le lien mène-t-il à un site officiel ?"),
            "Niveau 2": ("🧠 Mission OSINT – Profil public en danger",
                         "\nBienvenue dans la seconde mission, agent.\n🎯Objectif : vous montrer à quel point les informations que vous partagez peuvent être utilisées dans des attaques ciblées.\n🔒 Serez-vous capable de deviner si votre propre mot de passe y figure ? Si oui : il est temps de le changer. Si non : bravo, vous avez résisté à une attaque OSINT ciblée. \nMais souvenez-vous :Ce que vous partagez en ligne peut être utilisé contre vous…"),
            "Niveau 3": ("🕵️Bienvenue chez INTRA TECH – Département RH.",
                         "Vous êtes chargé d’une vérification interne sur le portail RH.\nConnectez-vous, récupérez les documents, lancez les scripts. Mais soyez attentif : un document téléchargé depuis le mauvais site pourrait ouvrir une brèche.À vous d’observer : comportements anormaux, connexions suspectes, lenteurs inhabituelles.Aucun signal d’alerte. Tout repose sur votre vigilance.Bonne chance, agent."),
            "Niveau 4": ("🧩 Mission : Bienvenue dans la Cryptographie !",
                         "🔐 Un employé d'une grande banque a téléchargé par erreur un fichier exécutable à partir d’un site de streaming. Ce fichier contenait un ransomware qui a chiffré tous les documents confidentiels de l’entreprise. \n💻 Votre mission est cruciale : retracer les étapes de l'attaque pour comprendre comment les données ont été chiffrées, et tenter de retrouver la clé de déchiffrement."),
            "Niveau 5": ("🎁 Défi Bonus – La Clé Mystère !",
                         "\nFélicitations ! Pour avoir atteint ce niveau, vous recevez une clé USB cadeau 🎉\nMais attention… dans le monde de la cybersécurité, tout cadeau cache peut-être un piège.\nSerez-vous capable de réagir à temps ? Ou serez-vous victime de votre propre curiosité ? 😅"),
        }

        self.mots_de_passe_niveaux = {
            "Niveau 1": "cyberizan@gmail.com",
            "Niveau 2": "cyber02",
            "Niveau 3": "FLAG{dns_spoofing_success_resolved_to_attacker_ip}",
            "Niveau 4": "ThisIsMySecretAESKey1234567890!!",
            "Niveau 5": "CYber1234"
        }

        self.mots_de_passe_niveaux_incorrect = {
            "Niveau 1": "cyber01",
            "Niveau 2": "cyber02",
            "Niveau 3": "cyber03",
            "Niveau 4": "cyber04",
            "Niveau 5": "cyber05"
        }

        self.contremesures_niveaux = {
            "Niveau 1": """~~ Phishing : <br> 
            - Vérifiez que l’expéditeur du mail est bien celui attendu et que le message semble légitime. <br> 
            - Ne cliquez jamais sur un lien ou une pièce jointe sans être sûr de sa provenance. <br> 
            <a href="https://www.cybermalveillance.gouv.fr/tous-nos-contenus/fiches-reflexes/hameconnage-phishing">➜ En savoir plus sur le phishing</a>""",

            "Niveau 2": """~~ OSINT : <br> 
            - Mettez vos comptes (ex. Instagram) en privé. <br> 
            - Évitez de publier des informations personnelles, sensibles ou compromettantes. <br> 
            ~~ Brute Force : <br> 
            - N’utilisez pas de données personnelles dans vos mots de passe. <br> 
            - Créez des mots de passe robustes : majuscules, minuscules, chiffres et caractères spéciaux. <br> 
            <a href="https://www.cybermalveillance.gouv.fr/tous-nos-contenus/actualites/conseils-mot-de-passe">➜ Conseils pour des mots de passe sécurisés</a>""",

            "Niveau 3": """~~ DNS Spoofing : <br> 
            - Évitez les connexions à des Wi-Fi publics non sécurisés. <br> 
            - Vérifiez toujours l’apparence et l’URL des pages web que vous visitez. <br> 
            ~~ Reverse Shell : <br> 
            - Ne lancez jamais de scripts ou de fichiers d’origine inconnue ou douteuse. <br> 
            <a href="https://www.cert.ssi.gouv.fr/">➜ Bonnes pratiques générales (ANSSI)</a>""",

            "Niveau 4": """~~ Clickjacking : <br> 
            - Faites attention à ce sur quoi vous cliquez, même sur des sites connus. <br> 
            - Méfiez-vous des téléchargements qui se lancent automatiquement après un clic. <br> 
            ~~ Ransomware : <br> 
            - Ne lancez pas d’exécutables non vérifiés, surtout avec des droits administrateur. <br> 
            - Surveillez le comportement suspect d’un programme au moment de son lancement. <br> 
            <a href="https://www.cybermalveillance.gouv.fr/tous-nos-contenus/fiches-reflexes/ransomware-rancongiciel">➜ Se protéger contre les ransomware</a>""",

            "Niveau 5": """~~ HackyPi : <br> 
            - Ne branchez jamais une clé USB ou un appareil inconnu à votre ordinateur. <br> 
            - Désactivez les ports USB ou limitez leur usage si possible. <br> 
            <a href="https://www.cybermalveillance.gouv.fr/">➜ Plus de conseils sur la sécurité informatique</a>"""


        }

        # Créer un QLabel pour afficher l'image du logo
        self.logo_label = QLabel(self)
        self.logo_pixmap = QPixmap(
            "C:\\Users\\Goku9\\.vscode\\Gui-Projet\\CyberEscape2.png")  # Remplacez par le chemin réel de votre logo
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
        # Bouton vert pour lancer la vidéo d'explication
        bouton_video = QPushButton("▶")
        bouton_video.setFixedSize(35, 35)
        bouton_video.setStyleSheet("""
            background-color: #4CAF50;  /* Vert */
            color: white;
            font-weight: bold;
            font-size: 16px;
            border-radius: 17px;
        """)
        bouton_video.pressed.connect(lambda: bouton_video.setStyleSheet("""
            background-color: #388E3C;  /* Vert foncé pressé */
            color: white;
            font-weight: bold;
            font-size: 16px;
            border-radius: 17px;
        """))
        bouton_video.released.connect(lambda: bouton_video.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
            font-size: 16px;

            border-radius: 17px;
        """))
        bouton_video.clicked.connect(
            lambda: self.lancer_video("D:\\Gui-Projet\\ILOVE.mp4"))  # remplace par ton chemin
        bouton_video.setToolTip("Vidéo d'explication")
        video_layout = QHBoxLayout()
        video_layout.addWidget(bouton_video)

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

            label_temps = QLabel(f"Temps :")
            self.labels_temps[niveau] = label_temps
            self.boutons_niveaux[niveau] = bouton_niveau
            # creation des checkbox
            checkbox_valide = QCheckBox()
            checkbox_valide.setText("")  # Laisse vide si tu ne veux pas de texte à côté

            # Connecte la vérification au clic (état coché)
            checkbox_valide.stateChanged.connect(
                lambda state, n=niveau, cb=checkbox_valide: self.verifier_mot_de_passe(n,
                                                                                       cb) if state == Qt.Checked else None)

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
                bouton_play.clicked.connect(lambda: self.lancer_video("D:\\Gui-Projet\\ILOVE.mp4"))

            bouton_plus.clicked.connect(lambda checked=False, n=niveau: self.ouvrir_info_niveau(n))

            niveau_layout.addWidget(bouton_niveau)
            niveau_layout.addWidget(label_temps)
            niveau_layout.addWidget(checkbox_valide)
            niveau_layout.addWidget(bouton_plus)
            niveau_layout.addWidget(bouton_play)

            self.layout_niveaux.addLayout(niveau_layout)

        layout_principal = QVBoxLayout()
        layout_principal.addWidget(self.logo_label)  # Ajoute le logo au layout
        layout_principal.addLayout(video_layout)
        layout_principal.addLayout(self.layout_niveaux)
        layout_principal.addWidget(self.label_chrono)
        self.setLayout(layout_principal)

        # Bouton pour afficher les statistiques finales
        bouton_stats = QPushButton("Voir mes stats")
        bouton_stats.setStyleSheet("""
            background-color: #9C27B0;  /* Violet */
            color: white;
            font-weight: bold;
            font-size: 14px;
            border-radius: 8px;
            padding: 8px;
        """)
        bouton_stats.clicked.connect(self.afficher_stats)

        layout_principal.addWidget(bouton_stats)


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
        mot_de_passe_interdit = self.mots_de_passe_niveaux_incorrect.get(
            niveau)  # Dictionnaire des mauvais mots de passe

        mot_saisi, ok = QInputDialog.getText(
            self,
            f"Mot de passe - {niveau}",
            "Entrez le mot de passe :",
            echo=QLineEdit.Password
        )

        if not ok or not mot_saisi:
            return  # L'utilisateur a annulé ou n'a rien saisi

        if mot_saisi == mot_de_passe_correct:
            bouton_radio.setChecked(True)

            # Calcule le temps passé dans le niveau
            temps_debut = self.temps_debut_niveaux.get(niveau)
            if temps_debut:
                temps_actuel = QTime.currentTime()
                secondes_passees = temps_debut.secsTo(temps_actuel)

                heures = secondes_passees // 3600
                minutes = (secondes_passees % 3600) // 60
                secondes = secondes_passees % 60
                texte_temps = f"✔ Fini en {heures:02d}:{minutes:02d}:{secondes:02d}"
                self.mettre_a_jour_label_temps(niveau, texte_temps)

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

            bouton_radio.setStyleSheet("""
                background-color: #B2FF59;  /* Vert pâle */
                color: gray;
                border: 2px solid #66BB6A;
                font-weight: bold;
            """)
            bouton_radio.setEnabled(False)

        elif mot_saisi == mot_de_passe_interdit:
            # Mot de passe connu mais incorrect → style rouge
            bouton_radio.setChecked(True)  # Le bouton peut rester activé mais stylisé en rouge
            self.mettre_a_jour_label_temps(niveau, "✖ Mauvais Flag utilisé")

            bouton_radio.setStyleSheet("""
                background-color: #FF8A80;  /* Rouge clair */
                color: black;
                border: 2px solid #D32F2F;
                font-weight: bold;
            """)
            bouton_radio.setEnabled(False)

            bouton_niveau = self.boutons_niveaux.get(niveau)
            if bouton_niveau:
                bouton_niveau.setStyleSheet("""
                    background-color: #D32F2F;
                    color: white;
                    border-radius: 5px;
                    font-size: 14px;
                    font-weight: bold;
                """)

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

   
    def afficher_stats(self):
        niveaux_valides = 0
        recap = ""

        for niveau in self.boutons_niveaux.keys():
            label_texte = self.labels_temps[niveau].text()
            if "✔" in label_texte:
                niveaux_valides += 1
            recap += f"{niveau} : {label_texte}<br>"

        score_final = f"<br>🏆 Score final : <b>{niveaux_valides} / {len(self.boutons_niveaux)}</b> niveaux validés.<br>"
        contremesures = "<br><b>🛡️ Contremesures recommandées :</b><br>"

        for niveau in self.boutons_niveaux.keys():
            label_texte = self.labels_temps[niveau].text()
            if "✖" in label_texte:
                contremesures += f'<br><span style="color:red; font-weight:bold;">🔸 {niveau} :<br>{self.contremesures_niveaux.get(niveau, "Pas de contremesures définies.")}</span><br>'
            elif "✔" not in label_texte:
                contremesures += f'<br>🔸 {niveau} :<br>{self.contremesures_niveaux.get(niveau, "Pas de contremesures définies.")}<br>'

        contenu_html = recap + score_final + contremesures

        # Création d'une QDialog avec QScrollArea
        dialog = QDialog(self)
        dialog.setWindowTitle("Statistiques finales")
        layout = QVBoxLayout(dialog)

        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)

        contenu_widget = QLabel()
        contenu_widget.setTextFormat(Qt.TextFormat.RichText)
        contenu_widget.setText(contenu_html)
        contenu_widget.setWordWrap(True)

        scroll_area.setWidget(contenu_widget)

        bouton_fermer = QPushButton("Fermer")
        bouton_fermer.clicked.connect(dialog.close)

        layout.addWidget(scroll_area)
        layout.addWidget(bouton_fermer)

        dialog.resize(500, 400)  # Dimensions de la fenêtre avec scroll
        dialog.exec_()


# Lancer l'application
app = QApplication([])
fenetre = CyberEscape()
fenetre.show()
app.exec_()