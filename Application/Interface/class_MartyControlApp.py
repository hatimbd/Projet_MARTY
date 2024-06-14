## Classe chargé de la création de l'interface graphique
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QLineEdit, QGridLayout
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from martypy import MartyConfigException
import threading
from class_MartyRobot import MartyRobot

class MartyControlApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()
        self.marty_robot1 = None
        self.marty_robot2 = None
        self.detection_running = False
        
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
        
        # Marty 1
        self.ip_label1 = QLabel('Adresse IP de Marty 1:', self)
        connection_layout.addWidget(self.ip_label1)

        self.ip_input1 = QLineEdit(self)
        connection_layout.addWidget(self.ip_input1)
        
         # Marty 2
        self.ip_label2 = QLabel('Adresse IP de Marty 2:', self)
        connection_layout.addWidget(self.ip_label2)

        self.ip_input2 = QLineEdit(self)
        connection_layout.addWidget(self.ip_input2)
        
        self.connect_btn = QPushButton('Connecter', self)
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
        
        # Grid layout for top buttons
        top_layout = QGridLayout()

        self.turn_left_btn1 = QPushButton(self)
        self.turn_left_btn1.setIcon(QIcon(r'images/L'))
        self.turn_left_btn1.setIconSize(QSize(50, 50))
        self.turn_left_btn1.clicked.connect(self.turn_left1)
        self.turn_left_btn1.setEnabled(False)
        top_layout.addWidget(self.turn_left_btn1, 0, 0)
        
        self.forward_btn = QPushButton(self)
        self.forward_btn.setIcon(QIcon(r'images/up_blue_arrow'))
        self.forward_btn.setIconSize(QSize(50, 50))
        self.forward_btn.clicked.connect(self.move_forward)
        self.forward_btn.setShortcut('up')
        self.forward_btn.setEnabled(False)
        top_layout.addWidget(self.forward_btn, 0, 1)

        self.turn_right_btn1 = QPushButton(self)
        self.turn_right_btn1.setIcon(QIcon(r'images/R'))
        self.turn_right_btn1.setIconSize(QSize(50, 50))
        self.turn_right_btn1.clicked.connect(self.turn_right1)
        self.turn_right_btn1.setEnabled(False)
        top_layout.addWidget(self.turn_right_btn1, 0, 2)
        
        movement_layout.addLayout(top_layout)

        # Horizontal layout for left and right arrows
        
        horizontal_layout = QHBoxLayout()
        self.turn_left_btn = QPushButton(self)
        self.turn_left_btn.setIcon(QIcon(r'images/left_blue_arrow'))
        self.turn_left_btn.setIconSize(QSize(50, 50))
        self.turn_left_btn.clicked.connect(self.turn_left)
        self.turn_left_btn.setShortcut('left')
        self.turn_left_btn.setEnabled(False)
        horizontal_layout.addWidget(self.turn_left_btn)

        self.turn_right_btn = QPushButton(self)
        self.turn_right_btn.setIcon(QIcon(r'images/right_blue_arrow'))
        self.turn_right_btn.setIconSize(QSize(50, 50))
        self.turn_right_btn.clicked.connect(self.turn_right)
        self.turn_right_btn.setShortcut('right')
        self.turn_right_btn.setEnabled(False)
        horizontal_layout.addWidget(self.turn_right_btn)

        movement_layout.addLayout(horizontal_layout)

        self.backward_btn = QPushButton(self)
        self.backward_btn.setIcon(QIcon(r'images/down_blue_arrow'))
        self.backward_btn.setIconSize(QSize(50, 50))
        self.backward_btn.clicked.connect(self.move_backward)
        self.backward_btn.setShortcut('down')
        self.backward_btn.setEnabled(False)
        movement_layout.addWidget(self.backward_btn)
        
      

        movement_box.setLayout(movement_layout)
        left_layout.addWidget(movement_box)

        # Additional Controls
        controls_box = QGroupBox("Additional Controls")
        controls_layout = QVBoxLayout()

        # Grid layout for buttons
        buttons_layout = QGridLayout()

        self.dance_btn = QPushButton('Danse', self)
        self.dance_btn.setIcon(QIcon(r'images/dance'))
        self.dance_btn.setIconSize(QSize(35, 35))
        self.dance_btn.clicked.connect(self.dance)
        self.dance_btn.setEnabled(False)
        buttons_layout.addWidget(self.dance_btn, 0, 0)
        
        self.celeb_btn = QPushButton('celebration', self)
        self.celeb_btn.setIcon(QIcon(r'images/celebrate'))
        self.celeb_btn.setStyleSheet("QPushButton { text-align: center; }")
        self.celeb_btn.setIconSize(QSize(35, 35))
        self.celeb_btn.clicked.connect(self.dance)
        self.celeb_btn.setEnabled(False)
        buttons_layout.addWidget(self.celeb_btn, 0, 1)


        self.stand_btn = QPushButton('Se tenir droit', self)
        self.stand_btn.setIcon(QIcon(r'images/stand'))
        self.stand_btn.setStyleSheet("QPushButton { text-align: center; }")
        self.stand_btn.setIconSize(QSize(35, 35))
        self.stand_btn.clicked.connect(self.stand_straight)
        self.stand_btn.setEnabled(False)
        buttons_layout.addWidget(self.stand_btn, 1, 0)

        self.sound_btn = QPushButton('Jouer son ID 1', self)
        self.sound_btn.setIcon(QIcon(r'images/sound'))
        self.sound_btn.setStyleSheet("QPushButton { text-align: center; }")
        self.sound_btn.setIconSize(QSize(35, 35))
        self.sound_btn.clicked.connect(self.play_sound)
        self.sound_btn.setEnabled(False)
        buttons_layout.addWidget(self.sound_btn, 1, 1)



        self.stop_btn = QPushButton('Arrêter', self)
        self.stop_btn.setIcon(QIcon(r'images/stop'))
        self.stop_btn.setStyleSheet("QPushButton { text-align: center; }")
        self.stop_btn.setIconSize(QSize(35, 35))
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setEnabled(False)
        buttons_layout.addWidget(self.stop_btn, 2, 0)

        self.high_five_btn = QPushButton('High Five', self)
        self.high_five_btn.setIcon(QIcon(r'images/high_five'))
        self.high_five_btn.setIconSize(QSize(35, 35))
        self.high_five_btn.clicked.connect(self.high_five)
        self.high_five_btn.setEnabled(False)
        buttons_layout.addWidget(self.high_five_btn, 2, 1)
        
        controls_layout.addLayout(buttons_layout)

        self.distance_btn = QPushButton('Obtenir distance', self)
        self.distance_btn.setIconSize(QSize(35, 35))
        self.distance_btn.clicked.connect(self.get_distance)
        self.distance_btn.setEnabled(False)
        controls_layout.addWidget(self.distance_btn)
        
        self.dist_label = QLabel('valeur du capteur de distance : ', self)
        controls_layout.addWidget(self.dist_label)

        self.accelerometer_btn = QPushButton('Obtenir accéléromètre', self)
        self.accelerometer_btn.setIconSize(QSize(35, 35))
        self.accelerometer_btn.clicked.connect(self.get_accelerometer)
        self.accelerometer_btn.setEnabled(False)
        controls_layout.addWidget(self.accelerometer_btn)
        
        self.acc_label = QLabel('valeur de l\'accéléromètre: ', self)
        controls_layout.addWidget(self.acc_label)
        
        #champ de saisie pour entrer la position des yeux.
        #tu dois saisir soit :'angry', 'excited', 'normal', 'wide', or 'wiggle' sinon tu saisis un angle
        self.eyes_label = QLabel('Position des yeux: (Saisissez angry, excited, normal, wide ou wiggle \n sinon saisissez un angle) ', self)
        controls_layout.addWidget(self.eyes_label)

        self.eyes_input = QLineEdit(self)
        controls_layout.addWidget(self.eyes_input)
        
        self.eyes_btn = QPushButton('Bouger les yeux', self)
        self.eyes_btn.clicked.connect(self.move_eyes)
        self.eyes_btn.setEnabled(False)
        controls_layout.addWidget(self.eyes_btn)
        
        #mode couleurs boutton
        self.detect_colors_btn = QPushButton('Mode Couleur', self)
        self.detect_colors_btn.clicked.connect(self.start_color_detection)
        self.detect_colors_btn.setEnabled(False)  
        controls_layout.addWidget(self.detect_colors_btn)

        self.maze_color_detect_btn = QPushButton('Détecter les couleurs des labyrinthes', self)
        self.maze_color_detect_btn.clicked.connect(self.MazeColorDetect)
        self.maze_color_detect_btn.setEnabled(False)
        controls_layout.addWidget(self.maze_color_detect_btn)
        
        controls_box.setLayout(controls_layout)
        right_layout.addWidget(controls_box)

    def connect_to_marty(self):
        ip1 = self.ip_input1.text()
        ip2 = self.ip_input2.text()
        if ip1:
            try:
                self.marty_robot1 = MartyRobot(ip1)
                self.status_label.setText(f'Connecté à Marty 1 à {ip1}')
            except MartyConfigException as e:
                self.status_label.setText(f'Erreur de connexion à Marty 1: {e}')

        if ip2:
            try:
                self.marty_robot2 = MartyRobot(ip2)
                if self.marty_robot1:
                    self.status_label.setText(self.status_label.text() + f'\nConnecté à Marty 2 à {ip2}')
                else:
                    self.status_label.setText(f'Connecté à Marty 2 à {ip2}')
            except MartyConfigException as e:
                self.status_label.setText(self.status_label.text() + f'\nErreur de connexion à Marty 2: {e}')

        self.enable_buttons(self.marty_robot1 is not None or self.marty_robot2 is not None)


    def enable_buttons(self, enabled):
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
        self.detect_colors_btn.setEnabled(enabled)
        self.maze_color_detect_btn.setEnabled(enabled)
        
    def walk(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.marcher, args=(5))
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.marcher, args=(5))
            mon_thread2.start()

    def dance(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.danse)
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.danse)
            mon_thread2.start()
            
    def celebrer(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.celebration)
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.celebration)
            mon_thread2.start()

    def stand_straight(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.se_tenir_droit)
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.se_tenir_droit)
            mon_thread2.start()

    def play_sound(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.jouer_son, args=(1))
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.jouer_son, args=(1))
            mon_thread2.start()

    def get_distance(self):
        if self.marty_robot1:
            distance = self.marty_robot1.obtenir_distance()
            mon_thread = threading.Thread(target = self.controls_label.setText(f'Distance: {distance} cm'))
            mon_thread.start()

    def get_accelerometer(self):
        if self.marty_robot1:
            accelerometer = self.marty_robot1.obtenir_accelerometre()
            mon_thread = threading.Thread(target = self.controls_label.setText(f'Accéléromètre: {accelerometer}'))
            mon_thread.start()

    def stop(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.arreter)
            mon_thread1.start()

    def high_five(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.high_five)
            mon_thread1.start()
        if self.marty_robot1:
            mon_thread2 = threading.Thread(target = self.marty_robot2.high_five)
            mon_thread2.start()
    
    def turn_right(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.tourner_droite)
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.tourner_droite)
            mon_thread2.start()
    
    def turn_left(self):
        if self.marty_robot1:
            mon_thread = threading.Thread(target = self.marty_robot1.tourner_gauche)
            mon_thread.start()
        if self.marty_robot2:
            mon_thread = threading.Thread(target = self.marty_robot2.tourner_gauche)
            mon_thread.start()
    
    def move_forward(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target=self.marty_robot1.marcher_avant)
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target=self.marty_robot2.marcher_avant)
            mon_thread2.start()
    
    def move_backward(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.marcher_arriere)
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.marcher_arriere)
            mon_thread2.start()

    def turn_right1(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.marcher, args=(3, 'auto', -20, 25, 3000))
            mon_thread1.start()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.marcher, args=(3, 'auto', -20, 25, 3000))
            mon_thread2.start()
        
    def turn_left1(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.marcher, args=(3, 'auto', 20, 25, 3000))
            mon_thread1.start()
        if self.marty_robot1:
            mon_thread2 = threading.Thread(target = self.marty_robot2.marcher, args=(3, 'auto', 20, 25, 3000))
            mon_thread2.start()
            
    def get_battery(self):
        if self.marty_robot1:
            battery = self.marty_robot1.obtenir_niveau_batterie()
            mon_thread = threading.Thread(target = self.battery_label.setText(f'Niveau de batterie: {battery["percentage"]}%'))
            mon_thread.start()
    
    def move_eyes(self):
        if self.marty_robot1:
            pose_or_angle = self.eyes_input.text()
            try:
                # Check if the input is a number and convert to int
                pose_or_angle = int(pose_or_angle)
            except ValueError:
                # If input is not a number, it will be treated as a pose string
                pass
            self.marty_robot1.bouger_oeil(pose_or_angle)
        if self.marty_robot2:
            pose_or_angle = self.eyes_input.text()
            try:
                # Check if the input is a number and convert to int
                pose_or_angle = int(pose_or_angle)
            except ValueError:
                # If input is not a number, it will be treated as a pose string
                pass
            self.marty_robot2.bouger_oeil(pose_or_angle)
    
    def start_color_detection(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.act_on_color)
            mon_thread1.start()
    
    def MazeColorDetect(self):
        if self.marty_robot1:
            mon_thread1 = threading.Thread(target = self.marty_robot1.detectMazeColors)
            mon_thread1.start()
            matrice1 = self.marty_robot1.detectMazeColors()
        if self.marty_robot2:
            mon_thread2 = threading.Thread(target = self.marty_robot2.detectMazeColors)
            mon_thread2.start()
            matrice2 = self.marty_robot2.detectMazeColors()
        self.merge_and_act_on_colors(matrice1, matrice2)
    
    def merge_and_act_on_colors(self, matrice1, matrice2):
        merged_colors = []
        for color1, color2 in zip(matrice1, matrice2):
            if color1 != "noir":
                merged_colors.append(color1)
            elif color2 != "noir":
                merged_colors.append(color2)

        for color in merged_colors:
            if self.marty_robot2:
                self.marty_robot2.act_on_color1(color)
                
 

