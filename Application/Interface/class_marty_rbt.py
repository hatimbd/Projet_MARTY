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
        self.marty.arms(0, 180, 1000)
        
    def obtenir_niveau_batterie(self):
        percentage = self.marty.get_battery_remaining()
        return {"percentage": percentage}
    
    def bouger_oeil(self, pose_or_angle, move_time=1000, bloquant=None):
        self.marty.eyes(pose_or_angle, move_time, bloquant)