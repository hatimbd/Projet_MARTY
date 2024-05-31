import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from martypy import Marty, MartyConfigException
import threading

class MartyRobot:
    def __init__(self, adresse_ip):
        try:
            self.marty = Marty("wifi", adresse_ip)
            print(f"Connected to Marty at {adresse_ip}")
        except MartyConfigException as e:
            print(f"Error connecting to Marty: {e}")

 
    def marcher(self, pas, start_foot, tourner, step_length, temps_mouvement):
        self.marty.walk(pas, start_foot, tourner, step_length, temps_mouvement)

    def marcher_avant(self):
         self.marty.walk(num_steps=2, step_length=25, move_time=1500, blocking=True)
         
    
    def marcher_arriere(self):
         self.marty.walk(num_steps=2, step_length=-25, move_time=1500, blocking=True)
   
    def tourner_droite(self):
        self.marty.sidestep('right', steps=1, step_length=35, move_time=1000, blocking=True)
    
    def tourner_gauche(self):
        self.marty.sidestep('left', steps=1, step_length=35, move_time=1000, blocking=True)

    def danse(self):
        self.marty.dance()

    def se_tenir_droit(self):
        self.marty.stand_straight()


    def jouer_son(self, id_son):
        self.marty.play_sound(id_son)

    def obtenir_distance(self):
        return self.marty.get_distance()

    def obtenir_accelerometre(self):
        return self.marty.get_accelerometer()

    def arreter(self):
        self.marty.stop()

    def high_five(self):
        self.marty.arms(0, 100, 1000)
        
    def obtenir_niveau_batterie(self):
        percentage = self.marty.get_battery_remaining()
        return {"percentage": percentage}


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

        self.dance_btn = QPushButton('Danse en cercle', self)
        self.dance_btn.clicked.connect(self.dance)
        self.dance_btn.setEnabled(False)
        controls_layout.addWidget(self.dance_btn)

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



    def walk(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher, args=(5))

    def dance(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.danse)

    def stand_straight(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.se_tenir_droit)

    def play_sound(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.jouer_son, args=(1))

    def get_distance(self):
        if self.marty_robot:
            distance = self.marty_robot.obtenir_distance()
            mon_thread = threading.Thread(target = self.status_label.setText(f'Distance: {distance} cm'))

    def get_accelerometer(self):
        if self.marty_robot:
            accelerometer = self.marty_robot.obtenir_accelerometre()
            mon_thread = threading.Thread(target = self.status_label.setText(f'Accéléromètre: {accelerometer}'))

    def stop(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.arreter)

    def high_five(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.high_five)
    
    def turn_right(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.tourner_droite)
    
    def turn_left(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.tourner_gauche)
    
    def move_forward(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher_avant)
    
    def move_backward(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher_arriere)

    def turn_right1(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher, args=(3, 'auto', -20, 25, 3000))
            self.marty_robot.se_tenir_droit()
        
    def turn_left1(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher, args=(3, 'auto', 20, 25, 3000))
            self.marty_robot.se_tenir_droit()
    
    def get_battery(self):
        if self.marty_robot:
            battery = self.marty_robot.obtenir_niveau_batterie()
            mon_thread = threading.Thread(target = self.battery_label.setText(f'Niveau de batterie: {battery["percentage"]}%'))
            mon_thread.start()
    
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControlApp()
    ex.show()
    sys.exit(app.exec())
