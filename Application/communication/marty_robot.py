from martypy import Marty, MartyConfigException
import time
import requests
from flask import Flask, request, jsonify
import threading

app = Flask(__name__)
robot_recepteur = None  # Global variable to store the robot instance

class MartyRobot:
    def __init__(self, adresse_ip, autre_robot_ip):
        try:
            self.marty = Marty("wifi", adresse_ip)
            self.autre_robot_ip = autre_robot_ip
            self.detected_color = None
            self.color_readings = {}
            self.detection_running = False
            robot_recepteur = self  # Set the global variable
            print(f"Connected to Marty at {adresse_ip}")
        except MartyConfigException as e:
            print(f"Error connecting to Marty: {e}")

    def set_autre_robot_ip(self, ip):
        self.autre_robot_ip = ip

    def envoyer_couleur(self, couleur):
        if self.autre_robot_ip:
            url = f"http://{self.autre_robot_ip}:5000/couleur"
            try:
                response = requests.post(url, json={"couleur": couleur})
                print(f"Envoyé couleur {couleur} à {self.autre_robot_ip}: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Erreur lors de l'envoi des données: {e}")
        else:
            print("Adresse IP de l'autre robot non définie")

    def recevoir_couleur(self, couleur):
        print(f"Couleur reçue : {couleur}")
        self.detected_color = couleur
        self.process_color(couleur)

    def process_color(self, couleur):
        if couleur == "rouge":
            self.danse()
        elif couleur == "jaune":
            self.marcher_arriere()
        elif couleur == "bleu":
            self.tourner_gauche()
        elif couleur == "violet":
            self.tourner_droite()
        elif couleur == "vert":
            self.marcher_avant()



    def run_server(self):
        app.run(host='0.0.0.0', port=5000)

    def start_server_thread(self):
        server_thread = threading.Thread(target=self.run_server)
        server_thread.start()
        
    def detect_color(self, reading):
        closest_color = None
        min_diff = float('inf')
        for color, value in self.color_readings.items():
            diff = abs(reading - value)
            if diff < min_diff:
                min_diff = diff
                closest_color = color
        return closest_color

    def detect_and_communicate(self):
        for _ in range(9):  # Par exemple, 9 cases à parcourir
            reading = self.marty.get_ground_sensor_reading("left")
            detected_color = self.detect_color(reading)
            print(f"Couleur détectée : {detected_color}")

            if detected_color == "noir":
                print("Case noire détectée, en attente d'information de l'autre robot...")
                while self.detected_color is None:
                    time.sleep(1)  # Attendre que l'autre robot envoie la couleur
                self.process_color(self.detected_color)
                self.detected_color = None  # Réinitialiser pour la prochaine itération
            else:
                self.envoyer_couleur(detected_color)
                self.process_color(detected_color)

            time.sleep(1)  # Attendre une seconde avant la prochaine lecture

    def marcher(self, pas, start_foot, tourner, step_length, temps_mouvement):
        self.marty.walk(pas, start_foot, tourner, step_length, temps_mouvement)
        self.marty.stand_straight()

    def marcher_avant(self):
        self.marty.walk(num_steps=2, step_length=25, move_time=1500, blocking=True)
        self.marty.stand_straight()
         
    def marcher_arriere(self):
        self.marty.walk(num_steps=2, step_length=-25, move_time=1500, blocking=True)
        self.marty.stand_straight()
        
    def celebration(self):
        self.marty.celebrate(3000)
   
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
        return self.marty.get_distance_sensor()

    def obtenir_accelerometre(self):
        return self.marty.get_accelerometer()

    def arreter(self):
        self.marty.stop()

    def high_five(self):
        self.marty.arms(0, 100, 1000)
        
    def obtenir_niveau_batterie(self):
        percentage = self.marty.get_battery_remaining()
        return {"percentage": percentage}

    def bouger_oeil(self, pose_or_angle, move_time=1000, bloquant=None):
        self.marty.eyes(pose_or_angle, move_time, bloquant)
    
    
@app.route('/couleur', methods=['POST'])
def recevoir_couleur_route():
    data = request.get_json()
    couleur = data.get("couleur")
    if robot_recepteur:
        robot_recepteur.recevoir_couleur(couleur)
    return jsonify({"status": "success"}), 200
