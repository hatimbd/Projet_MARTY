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
        
        
    def get_color_name(self):
        color_sensor_reading = self.marty.get_ground_sensor_reading('LeftColorSensor')
        print(color_sensor_reading)
        if 14 <= color_sensor_reading <= 16 :
            print("Noir")
            return "Noir"
        elif 19 <= color_sensor_reading <= 22 : 
            print("Bleu")
            return "Bleu"
        elif 84 <= color_sensor_reading <= 89 :
            print("violet")
            return "violet"
        elif 27 <= color_sensor_reading <= 30:
            print("Vert")
            return "Vert"
        elif 167 <= color_sensor_reading <= 171 :
            print("Jaune")
            return "Jaune"
        elif 73 <= color_sensor_reading <= 76 :
            print("Rouge")
            return "Rouge"
        else:
            print("Couleur inconnue")
            return "Couleur inconnue"
        
    def act_on_color(self, color):
        while True:
            if color == "Rouge":
                self.marty.dance()
                self.marty.stand_straight()
            elif color == "Jaune":
                self.marty.walk(num_steps=2, step_length=-25, move_time=1500, blocking=True)
                self.marty.stand_straight()
            elif color == "Vert":
                self.marty.walk(num_steps=2, step_length=25, move_time=1500, blocking=True)
                self.marty.stand_straight()
            elif color == "Bleu":
                self.marty.sidestep('left', steps=1, step_length=35, move_time=1000, blocking=True)
                self.marty.stand_straight()
            elif color == "violet":
                self.marty.sidestep('right', steps=1, step_length=35, move_time=1000, blocking=True)
                self.marty.stand_straight()
            elif color == "noir":
                self.marty.stop()
        
