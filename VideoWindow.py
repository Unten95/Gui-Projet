from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSlider, QLabel, QSizePolicy
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtCore import QUrl, Qt, QTimer

class FenetreVideo(QWidget):
    def __init__(self, chemin_video):
        super().__init__()
        self.setWindowTitle("Lecture vidéo")
        self.setGeometry(100, 100, 700, 500)

        # Widget vidéo
        self.video_widget = QVideoWidget()
        self.video_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        self.player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.player.setVideoOutput(self.video_widget)

        # Bouton Play/Pause
        self.bouton_play_pause = QPushButton("⏸")
        self.bouton_play_pause.setFixedSize(40, 40)
        self.bouton_play_pause.clicked.connect(self.toggle_play_pause)

        # Slider de progression
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setRange(0, 0)
        self.slider.sliderMoved.connect(self.set_position)

        # Label de temps
        self.label_temps = QLabel("00:00 / 00:00")
        self.label_temps.setFixedWidth(100)

        # Layout des contrôles
        self.controle_layout = QHBoxLayout()
        self.controle_layout.addWidget(self.bouton_play_pause)
        self.controle_layout.addWidget(self.slider)
        self.controle_layout.addWidget(self.label_temps)

        # Regrouper les contrôles dans un widget pour pouvoir le masquer
        self.controle_widget = QWidget()
        self.controle_widget.setLayout(self.controle_layout)

        # Layout principal
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.video_widget)
        self.layout_principal.addWidget(self.controle_widget)
        self.setLayout(self.layout_principal)

        # Charger la vidéo
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(chemin_video)))
        self.player.play()

        # Connexions
        self.player.positionChanged.connect(self.update_position)
        self.player.durationChanged.connect(self.update_duration)
        self.player.stateChanged.connect(self.sync_bouton_play)

        # Timer pour auto-cacher les contrôles
        self.timer = QTimer()
        self.timer.setInterval(3000)  # 3000 ms = 3 secondes d'inactivité
        self.timer.timeout.connect(self.hide_controles)
        self.timer.start()

        # Pour garder en mémoire la durée totale de la vidéo
        self.duree = 0

    def hide_controles(self):
        self.controle_widget.hide()

    def show_controles(self):
        self.controle_widget.show()
        # Redémarrage du timer d'auto-hide
        self.timer.start()

    def enterEvent(self, event):
        # Lorsque la souris entre dans la fenêtre, montrer les contrôles
        self.show_controles()
        super().enterEvent(event)

    def mouseMoveEvent(self, event):
        # Dès qu'il y a un mouvement de souris, montrer les contrôles et redémarrer le timer
        self.show_controles()
        super().mouseMoveEvent(event)

    def closeEvent(self, event):
        self.player.stop()
        self.player.deleteLater()
        event.accept()

    def toggle_play_pause(self):
        if self.player.state() == QMediaPlayer.PlayingState:
            self.player.pause()
        else:
            self.player.play()

    def sync_bouton_play(self, state):
        self.bouton_play_pause.setText("⏸" if state == QMediaPlayer.PlayingState else "▶")

    def update_position(self, position):
        self.slider.setValue(position)
        self.label_temps.setText(f"{self.formater_temps(position)} / {self.formater_temps(self.duree)}")

    def update_duration(self, duration):
        self.slider.setRange(0, duration)
        self.duree = duration

    def set_position(self, position):
        self.player.setPosition(position)

    def formater_temps(self, ms):
        secondes = int(ms / 1000)
        minutes = secondes // 60
        secondes = secondes % 60
        return f"{minutes:02d}:{secondes:02d}"
