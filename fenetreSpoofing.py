from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextBrowser, QPushButton

class FenetreSpoofing(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Mission - DNS Spoofing (Niveau 3)")
        self.setFixedSize(700, 500)

        layout = QVBoxLayout()

        instructions = """
<h2>[INTRA TECH - Département RH]</h2>
<p>Bienvenue à votre première mission au sein du service RH. Vous êtes chargé d'effectuer une vérification de routine sur le portail interne RH de l’entreprise.</p>

<p><b>Accédez au portail :</b> <a href="http://rh.intra.local">http://rh.intra.local</a></p>

<h3>📝 Tâches à accomplir :</h3>
<ol>
<li>Connectez-vous au portail RH avec vos identifiants.</li>
<li>Veuillez trouver les informations nécessaires sur Politique RH 2025 (confidentiel) en exécutant les commandes suivantes :
cd ~/Downloads
./flag.run</li>
<li>Utilisez le script réseau pour observer les connexions effectuées.</li>
<li>Relevez toute anomalie suspecte (adresse IP étrange, comportement du site, erreurs...).</li>
<li>Rédigez un rapport dans le fichier prévu à cet effet.</li>
</ol>

<h3>:file_folder: Outils disponibles :</h3>
<ul>
<li><b>Script :</b> <code>analyse_dns.py</code> (permet d'observer les résolutions DNS)</li>
<li><b>Répertoire de logs :</b> <code>~/logs_https/</code> (se remplit automatiquement)</li>
<li><b>En cas d’anomalie dans l’adresse IP du site, ajoutez cette ligne dans le fichier /etc/hosts :
adresse_ip_légitime rh.intra.local</li>
</ul>

<h3>⚠️ Important :</h3>
<ul>
<li>Si le site affiche un comportement inhabituel (erreurs, lenteur, visuel modifié…), pensez à relancer le script d’analyse.</li>
<li>Aucune alerte ne sera donnée automatiquement : vous êtes seul responsable de votre vigilance.</li>
</ul>

<hr>
<p><i>Bonne chance, et n’oubliez pas : la cybersécurité commence par l’observation.</i></p>
"""

        texte = QTextBrowser()
        texte.setOpenExternalLinks(True)
        texte.setHtml(instructions)

        bouton_fermer = QPushButton("Fermer")
        bouton_fermer.clicked.connect(self.close)

        layout.addWidget(texte)
        layout.addWidget(bouton_fermer)

        self.setLayout(layout)