from martypy import Marty, MartyConfigException


class MartyRobot:
    def __init__(self, adresse_ip):
        try:
            self.marty = Marty("wifi", adresse_ip)
            print(f"Connected to Marty at {adresse_ip}")
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
        self.marty.arms(0, 100, 1000)
        
    def obtenir_niveau_batterie(self):
        percentage = self.marty.get_battery_remaining()
        return {"percentage": percentage}

    def bouger_oeil(self, pose_or_angle, move_time=1000, bloquant=None):
        self.marty.eyes(pose_or_angle, move_time, bloquant)

    def get_color_name(self):
        s=0
        for i in range(10) :
            color_sensor_reading = self.marty.get_ground_sensor_reading('LeftColorSensor')
            s+=color_sensor_reading
            i+=1
        s=s/10
        print(color_sensor_reading)
        if 14 <= s <= 17 :
            print("Noir")
            return "Noir"
        elif 19 <= s <= 23 : 
            print("BleuM")
            return "BleuM"
        elif 89 <= s <= 99 :
            print("Rose")
            return "Rose"
        elif 27 <= s <= 33:
            print("Vert")
            return "Vert"
        elif 167 <= s <= 193 :
            print("Jaune")
            return "Jaune"
        elif 73 <= s <= 87 :
            print("Rouge")
            return "Rouge"
        elif 49 <= s <= 52 :
            print("BleuC")
            return("BleuC")
        else:
            print("Couleur inconnue")
            return "Couleur inconnue"
    global scan 
    scan = True    
    def act_on_color(self):
        while scan:
            color = self.get_color_name()
            if color == "BleuC":
                self.marty.eyes('wiggle')
                self.marty.walk(num_steps=6, step_length=30, move_time=2000, blocking=True)
            if color == "Rouge":
                self.marty.dance()
                self.marty.stop()
            elif color == "Jaune":
                self.marty.walk(num_steps=4, step_length=-30, move_time=2000, blocking=True)
            elif color == "Vert":
                self.marty.walk(num_steps=6, step_length=30, move_time=2000, blocking=True)
            elif color == "BleuM":
                self.marty.sidestep('right', steps=6, step_length=35, move_time=2000, blocking=True)
                self.marty.stand_straight()
            elif color == "Rose":
                self.marty.sidestep('left', steps=6, step_length=35, move_time=2000, blocking=True)
                self.marty.stand_straight()
            elif color == "noir":
                self.marty.stop()
