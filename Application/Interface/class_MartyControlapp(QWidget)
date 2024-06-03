import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from martypy import Marty, MartyConfigException
import threading

class MartyControlApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.marty_robot = None

    def initUI(self):
        self.setWindowTitle('Marty Control Interface')
        self.setGeometry(100, 100, 800, 600)

        main_layout = QHBoxLayout()
        self.setLayout(main_layout)

        left_layout = QVBoxLayout()
        main_layout.addLayout(left_layout)

        right_layout = QVBoxLayout()
        main_layout.addLayout(right_layout)

        # Connection Box
        connection_box = QGroupBox("Connection")
        connection_layout = QVBoxLayout()
        self.ip_label = QLabel('Adresse IP de Marty:', self)
        connection_layout.addWidget(self.ip_label)

        self.ip_input = QLineEdit(self)
        connection_layout.addWidget(self.ip_input)
        

        self.connect_btn = QPushButton('Connecter à Marty', self)
        self.connect_btn.clicked.connect(self.connect_to_marty)
        connection_layout.addWidget(self.connect_btn)

        self.status_label = QLabel('', self)
        connection_layout.addWidget(self.status_label)
        
        self.battery_btn = QPushButton('Obtenir niveau de batterie', self)
        self.battery_btn.clicked.connect(self.get_battery)
        self.battery_btn.setEnabled(False)
        connection_layout.addWidget(self.battery_btn)
        
        self.battery_label = QLabel('Niveau de batterie: ', self)
        connection_layout.addWidget(self.battery_label)

        connection_box.setLayout(connection_layout)
        left_layout.addWidget(connection_box)

        # Movement Controls
        movement_box = QGroupBox("Movement Controls")
        movement_layout = QVBoxLayout()

        self.forward_btn = QPushButton(self)
        self.forward_btn.setIcon(QIcon(r'C:/Users/hatim/OneDrive/Bureau/Projet robotique/up_blue_arrow'))
        self.forward_btn.setIconSize(QSize(50, 50))
        self.forward_btn.clicked.connect(self.move_forward)
        self.forward_btn.setEnabled(False)
        movement_layout.addWidget(self.forward_btn)

        horizontal_layout = QHBoxLayout()
        self.turn_left_btn = QPushButton(self)
        self.turn_left_btn.setIcon(QIcon(r'C:/Users/hatim/OneDrive/Bureau/Projet robotique/left_blue_arrow'))
        self.turn_left_btn.setIconSize(QSize(50, 50))
        self.turn_left_btn.clicked.connect(self.turn_left)
        self.turn_left_btn.setEnabled(False)
        horizontal_layout.addWidget(self.turn_left_btn)

        self.turn_right_btn = QPushButton(self)
        self.turn_right_btn.setIcon(QIcon(r'C:/Users/hatim/OneDrive/Bureau/Projet robotique/right_blue_arrow'))
        self.turn_right_btn.setIconSize(QSize(50, 50))
        self.turn_right_btn.clicked.connect(self.turn_right)
        self.turn_right_btn.setEnabled(False)
        horizontal_layout.addWidget(self.turn_right_btn)

        movement_layout.addLayout(horizontal_layout)

        self.backward_btn = QPushButton(self)
        self.backward_btn.setIcon(QIcon(r'C:/Users/hatim/OneDrive/Bureau/Projet robotique/down_blue_arrow'))
        self.backward_btn.setIconSize(QSize(50, 50))
        self.backward_btn.clicked.connect(self.move_backward)
        self.backward_btn.setEnabled(False)
        movement_layout.addWidget(self.backward_btn)

        movement_box.setLayout(movement_layout)
        left_layout.addWidget(movement_box)

        # Additional Controls
        controls_box = QGroupBox("Additional Controls")
        controls_layout = QVBoxLayout()

        self.walk_btn = QPushButton('Marcher 5 pas', self)
        self.walk_btn.clicked.connect(self.walk)
        self.walk_btn.setEnabled(False)
        controls_layout.addWidget(self.walk_btn)

        self.dance_btn = QPushButton('Danse', self)
        self.dance_btn.clicked.connect(self.dance)
        self.dance_btn.setEnabled(False)
        controls_layout.addWidget(self.dance_btn)
        
        self.celeb_btn = QPushButton('celebration', self)
        self.celeb_btn.clicked.connect(self.dance)
        self.celeb_btn.setEnabled(False)
        controls_layout.addWidget(self.celeb_btn)


        self.stand_btn = QPushButton('Se tenir droit', self)
        self.stand_btn.clicked.connect(self.stand_straight)
        self.stand_btn.setEnabled(False)
        controls_layout.addWidget(self.stand_btn)

        self.sound_btn = QPushButton('Jouer son ID 1', self)
        self.sound_btn.clicked.connect(self.play_sound)
        self.sound_btn.setEnabled(False)
        controls_layout.addWidget(self.sound_btn)

        self.distance_btn = QPushButton('Obtenir distance', self)
        self.distance_btn.clicked.connect(self.get_distance)
        self.distance_btn.setEnabled(False)
        controls_layout.addWidget(self.distance_btn)

        self.accelerometer_btn = QPushButton('Obtenir accéléromètre', self)
        self.accelerometer_btn.clicked.connect(self.get_accelerometer)
        self.accelerometer_btn.setEnabled(False)
        controls_layout.addWidget(self.accelerometer_btn)

        self.stop_btn = QPushButton('Arrêter', self)
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setEnabled(False)
        controls_layout.addWidget(self.stop_btn)

        self.high_five_btn = QPushButton('High Five', self)
        self.high_five_btn.clicked.connect(self.high_five)
        self.high_five_btn.setEnabled(False)
        controls_layout.addWidget(self.high_five_btn)
        
        self.turn_right_btn1 = QPushButton('Roation à droite', self)
        self.turn_right_btn1.clicked.connect(self.turn_right1)
        self.turn_right_btn1.setEnabled(False)
        controls_layout.addWidget(self.turn_right_btn1)
        
        self.turn_left_btn1 = QPushButton('Rotation à gauche', self)
        self.turn_left_btn1.clicked.connect(self.turn_left1)
        self.turn_left_btn1.setEnabled(False)
        controls_layout.addWidget(self.turn_left_btn1)
        
        #champ de saisie pour entrer la position des yeux.
        #tu dois saisir soit :'angry', 'excited', 'normal', 'wide', or 'wiggle' sinon tu saisis un angle
        self.eyes_label = QLabel('Position des yeux: ', self)
        controls_layout.addWidget(self.eyes_label)

        self.eyes_input = QLineEdit(self)
        controls_layout.addWidget(self.eyes_input)
        
        self.eyes_btn = QPushButton('Bouger les yeux', self)
        self.eyes_btn.clicked.connect(self.move_eyes)
        self.eyes_btn.setEnabled(False)
        controls_layout.addWidget(self.eyes_btn)

        
        controls_box.setLayout(controls_layout)
        right_layout.addWidget(controls_box)

    def connect_to_marty(self):
        ip = self.ip_input.text()
        try:
            self.marty_robot = MartyRobot(ip)
            self.status_label.setText(f'Connecté à Marty à {ip}')
            self.enable_buttons(True)
        except MartyConfigException as e:
            self.status_label.setText(f'Erreur: {e}')
            self.enable_buttons(False)









    def enable_buttons(self, enabled):
        self.walk_btn.setEnabled(enabled)
        self.dance_btn.setEnabled(enabled)
        self.celeb_btn.setEnabled(enabled)
        self.stand_btn.setEnabled(enabled)
        self.sound_btn.setEnabled(enabled)
        self.distance_btn.setEnabled(enabled)
        self.accelerometer_btn.setEnabled(enabled)
        self.stop_btn.setEnabled(enabled)
        self.high_five_btn.setEnabled(enabled)
        self.forward_btn.setEnabled(enabled)
        self.turn_left_btn.setEnabled(enabled)
        self.turn_right_btn.setEnabled(enabled)
        self.backward_btn.setEnabled(enabled)
        self.turn_right_btn1.setEnabled(enabled)
        self.turn_left_btn1.setEnabled(enabled)
        self.battery_btn.setEnabled(enabled)
        self.eyes_btn.setEnabled(enabled)
