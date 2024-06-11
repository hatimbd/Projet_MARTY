from martypy import Marty, MartyConfigException
import time

class MartyRobot:
    def __init__(self, adresse_ip):
        try:
            self.marty = Marty("wifi", adresse_ip)
            print(f"Connected to Marty at {adresse_ip}")
            self.color_readings = {}
            self.detection_thread = None
            self.detection_running = False
        except MartyConfigException as e:
            print(f"Error connecting to Marty: {e}")

 
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
        self.marty.arms(0, 180, 1000)
        
    def obtenir_niveau_batterie(self):
        percentage = self.marty.get_battery_remaining()
        return {"percentage": percentage}
    
    def bouger_oeil(self, pose_or_angle, move_time=1000, bloquant=None):
        self.marty.eyes(pose_or_angle, move_time, bloquant)
        
    def calibrate_color(self, color_name):
        print(f"Placez la couleur {color_name} sous le capteur et appuyez sur Entrée.")
        input()  # Attendre que l'utilisateur appuie sur Entrée
        readings = []
        for _ in range(10):
            reading = self.marty.get_ground_sensor_reading('left')
            readings.append(reading)
            time.sleep(0.1)
        avg_reading = sum(readings) / len(readings)
        self.color_readings[color_name] = avg_reading
        print(f"Lecture moyenne pour {color_name}: {avg_reading}")
        
    def detect_color(self, reading):
        closest_color = None
        min_diff = float('inf')
        for color, value in self.color_readings.items():
            diff = abs(reading - value)
            if diff < min_diff:
                min_diff = diff
                closest_color = color
        return closest_color
    
    def start_detection(self):
        print("Début de la détection des couleurs...")
        self.detection_running = True
        try:
            while self.detection_running:
                reading = self.marty.get_ground_sensor_reading("left")
                detected_color = self.detect_color(reading)
                print(f"Couleur détectée : {detected_color}")

                if detected_color == "rouge":
                    self.danse()
                elif detected_color == "jaune":
                    self.marcher_arriere()
                elif detected_color == "bleu":
                    self.tourner_gauche()
                elif detected_color == "violet":
                    self.tourner_droite()
                elif detected_color == "vert":
                    self.marcher_avant()
                
                time.sleep(1)  # Attendre une seconde avant la prochaine lecture
        except KeyboardInterrupt:
            print("Détection des couleurs terminée.")
