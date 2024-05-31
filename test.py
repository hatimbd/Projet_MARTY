import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import Qt
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
        self.marty.arms(100, 100, 1000)
    
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
        self.setGeometry(100, 100, 400, 300)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.ip_label = QLabel('Adresse IP de Marty:', self)
        self.layout.addWidget(self.ip_label)

        self.ip_input = QLineEdit(self)
        self.layout.addWidget(self.ip_input)

        self.connect_btn = QPushButton('Connecter à Marty', self)
        self.connect_btn.clicked.connect(self.connect_to_marty)
        self.layout.addWidget(self.connect_btn)

        self.status_label = QLabel('', self)
        self.layout.addWidget(self.status_label)

        self.pas_label = QLabel('Nombre de pas:', self)
        self.layout.addWidget(self.pas_label)

        self.pas_input = QLineEdit(self)
        self.layout.addWidget(self.pas_input)

        self.walk_btn = QPushButton('Marcher', self)
        self.walk_btn.clicked.connect(self.walk)
        self.layout.addWidget(self.walk_btn)

        self.turn_right_btn = QPushButton('Tourner à droite', self)
        self.turn_right_btn.clicked.connect(self.turn_right)
        self.turn_right_btn.setEnabled(False)
        self.layout.addWidget(self.turn_right_btn)
        
        self.turn_left_btn = QPushButton('Tourner à gauche', self)
        self.turn_left_btn.clicked.connect(self.turn_left)
        self.turn_left_btn.setEnabled(False)
        self.layout.addWidget(self.turn_left_btn)

        self.dance_btn = QPushButton('Danse', self)
        self.dance_btn.clicked.connect(self.dance)
        self.dance_btn.setEnabled(False)
        self.layout.addWidget(self.dance_btn)

        self.stand_btn = QPushButton('Se tenir droit', self)
        self.stand_btn.clicked.connect(self.stand_straight)
        self.stand_btn.setEnabled(False)
        self.layout.addWidget(self.stand_btn)

        self.sound_btn = QPushButton('Jouer son ID 1', self)
        self.sound_btn.clicked.connect(self.play_sound)
        self.sound_btn.setEnabled(False)
        self.layout.addWidget(self.sound_btn)

        self.distance_btn = QPushButton('Obtenir distance', self)
        self.distance_btn.clicked.connect(self.get_distance)
        self.distance_btn.setEnabled(False)
        self.layout.addWidget(self.distance_btn)

        self.accelerometer_btn = QPushButton('Obtenir accéléromètre', self)
        self.accelerometer_btn.clicked.connect(self.get_accelerometer)
        self.accelerometer_btn.setEnabled(False)
        self.layout.addWidget(self.accelerometer_btn)

        self.stop_btn = QPushButton('Arrêter', self)
        self.stop_btn.clicked.connect(self.stop)
        self.stop_btn.setEnabled(False)
        self.layout.addWidget(self.stop_btn)

        self.high_five_btn = QPushButton('High Five', self)
        self.high_five_btn.clicked.connect(self.high_five)
        self.high_five_btn.setEnabled(False)
        self.layout.addWidget(self.high_five_btn)
        
        self.battery_btn = QPushButton('Obtenir niveau de batterie', self)
        self.battery_btn.clicked.connect(self.get_battery)
        self.battery_btn.setEnabled(False)
        self.layout.addWidget(self.battery_btn)
        
        self.battery_label = QLabel('Niveau de batterie: ', self)
        self.layout.addWidget(self.battery_label)

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
        self.turn_right_btn.setEnabled(enabled)
        self.turn_left_btn.setEnabled(enabled)
        self.dance_btn.setEnabled(enabled)
        self.stand_btn.setEnabled(enabled)
        self.sound_btn.setEnabled(enabled)
        self.distance_btn.setEnabled(enabled)
        self.accelerometer_btn.setEnabled(enabled)
        self.stop_btn.setEnabled(enabled)
        self.high_five_btn.setEnabled(enabled)
        self.battery_btn.setEnabled(enabled)

    def walk(self, pas):
        if self.marty_robot:
            pas = int(self.pas_input.text())
            self.marty_robot.marcher(pas, 'auto', 0, 25, 3000)

    def turn_right(self):
        if self.marty_robot:
            self.marty_robot.marcher(3, 'auto', -20, 25, 3000)
            self.marty_robot.se_tenir_droit()
    
    def turn_left(self):
        if self.marty_robot:
            self.marty_robot.marcher(3, 'auto', 20, 25, 3000)
            self.marty_robot.se_tenir_droit()

    def dance(self):
        if self.marty_robot:
            self.marty_robot.danse()

    def stand_straight(self):
        if self.marty_robot:
            self.marty_robot.se_tenir_droit()

    def play_sound(self):
        if self.marty_robot:
            self.marty_robot.jouer_son(1)

    def get_distance(self):
        if self.marty_robot:
            distance = self.marty_robot.obtenir_distance()
            self.status_label.setText(f'Distance: {distance} cm')

    def get_accelerometer(self):
        if self.marty_robot:
            accelerometer = self.marty_robot.obtenir_accelerometre()
            self.status_label.setText(f'Accéléromètre: {accelerometer}')

    def stop(self):
        if self.marty_robot:
            self.marty_robot.arreter()

    def high_five(self):
        if self.marty_robot:
            self.marty_robot.high_five()
            
    def get_battery(self):
        if self.marty_robot:
            battery = self.marty_robot.obtenir_niveau_batterie()
            self.battery_label.setText(f'Niveau de batterie: {battery["percentage"]}%')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControlApp()
    ex.show()
    sys.exit(app.exec())
