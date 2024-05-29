import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit
from PyQt6.QtCore import Qt
from martypy import Marty, MartyConfigException

class MartyRobot:
    def __init__(self, adresse_ip):
        try:
            self.marty = Marty("wifi", adresse_ip)
            print(f"Connected to Marty at {adresse_ip}")
        except MartyConfigException as e:
            print(f"Error connecting to Marty: {e}")

    def bouger_articulation(self, articulation, position, temps_mouvement=1, bloquant=True):
        self.marty.move_joint(articulation, position, temps_mouvement, bloquant)

    def marcher(self, pas, tourner=0, temps_mouvement=1, longueur_pas=50):
        self.marty.walk(pas, tourner, temps_mouvement, longueur_pas)

    def tourner(self, angle):
        self.marty.turn(angle)

    def danse_cercle(self):
        self.marty.circle_dance()

    def se_tenir_droit(self):
        self.marty.stand_straight()

    def incliner(self, direction):
        self.marty.lean(direction)

    def bouger_oeil(self, oeil, position):
        self.marty.move_eye(oeil, position)

    def definir_led(self, led, r, g, b):
        self.marty.set_led(led, r, g, b)

    def jouer_son(self, id_son):
        self.marty.play_sound(id_son)

    def obtenir_distance(self):
        return self.marty.get_distance()

    def obtenir_accelerometre(self):
        return self.marty.get_accelerometer()

    def arreter(self):
        self.marty.stop()

    def high_five(self):
        self.marty.high_five()

class MartyControlApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

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

        self.move_btn = QPushButton('Bouger articulation (left_hip à 20 degrés)', self)
        self.move_btn.clicked.connect(self.move_joint)
        self.layout.addWidget(self.move_btn)

        self.walk_btn = QPushButton('Marcher 5 pas', self)
        self.walk_btn.clicked.connect(self.walk)
        self.layout.addWidget(self.walk_btn)

        self.turn_btn = QPushButton('Tourner de 90 degrés', self)
        self.turn_btn.clicked.connect(self.turn)
        self.layout.addWidget(self.turn_btn)

        self.dance_btn = QPushButton('Danse en cercle', self)
        self.dance_btn.clicked.connect(self.dance_circle)
        self.layout.addWidget(self.dance_btn)

        self.stand_btn = QPushButton('Se tenir droit', self)
        self.stand_btn.clicked.connect(self.stand_straight)
        self.layout.addWidget(self.stand_btn)

        self.lean_btn = QPushButton('Incliner à gauche', self)
        self.lean_btn.clicked.connect(self.lean_left)
        self.layout.addWidget(self.lean_btn)

        self.eye_btn = QPushButton('Bouger œil gauche à 45 degrés', self)
        self.eye_btn.clicked.connect(self.move_eye)
        self.layout.addWidget(self.eye_btn)

        self.led_btn = QPushButton('Définir LED gauche à rouge', self)
        self.led_btn.clicked.connect(self.set_led)
        self.layout.addWidget(self.led_btn)

        self.sound_btn = QPushButton('Jouer son ID 1', self)
        self.sound_btn.clicked.connect(self.play_sound)
        self.layout.addWidget(self.sound_btn)

        self.distance_btn = QPushButton('Obtenir distance', self)
        self.distance_btn.clicked.connect(self.get_distance)
        self.layout.addWidget(self.distance_btn)

        self.accelerometer_btn = QPushButton('Obtenir accéléromètre', self)
        self.accelerometer_btn.clicked.connect(self.get_accelerometer)
        self.layout.addWidget(self.accelerometer_btn)

        self.stop_btn = QPushButton('Arrêter', self)
        self.stop_btn.clicked.connect(self.stop)
        self.layout.addWidget(self.stop_btn)

        self.high_five_btn = QPushButton('High Five', self)
        self.high_five_btn.clicked.connect(self.high_five)
        self.layout.addWidget(self.high_five_btn)

    def connect_to_marty(self):
        ip = self.ip_input.text()
        try:
            self.marty_robot = MartyRobot(ip)
            self.status_label.setText(f'Connecté à Marty à {ip}')
        except MartyConfigException as e:
            self.status_label.setText(f'Erreur: {e}')

    def move_joint(self):
        self.marty_robot.bouger_articulation('left_hip', 20)

    def walk(self):
        self.marty_robot.marcher(5)

    def turn(self):
        self.marty_robot.tourner(90)

    def dance_circle(self):
        self.marty_robot.danse_cercle()

    def stand_straight(self):
        self.marty_robot.se_tenir_droit()

    def lean_left(self):
        self.marty_robot.incliner('left')

    def move_eye(self):
        self.marty_robot.bouger_oeil('left', 45)

    def set_led(self):
        self.marty_robot.definir_led('left', 255, 0, 0)

    def play_sound(self):
        self.marty_robot.jouer_son(1)

    def get_distance(self):
        distance = self.marty_robot.obtenir_distance()
        self.status_label.setText(f'Distance: {distance} cm')

    def get_accelerometer(self):
        accelerometer = self.marty_robot.obtenir_accelerometre()
        self.status_label.setText(f'Accéléromètre: {accelerometer}')

    def stop(self):
        self.marty_robot.arreter()

    def high_five(self):
        self.marty_robot.high_five()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MartyControlApp()
    ex.show()
    sys.exit(app.exec())
