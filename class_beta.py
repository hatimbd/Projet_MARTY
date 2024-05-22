import martypy

class MartyRobot:
    def __init__(self, adresse_ip):
        """
        Initialiser Marty avec l'adresse IP.
        :param adresse_ip: Adresse IP de Marty
        """
        self.marty = martypy.Marty(adresse_ip)

    def bouger_articulation(self, articulation, position, temps_mouvement=1, bloquant=True):
        """
        Bouger une articulation spécifique à une position donnée.
        :param articulation: Nom de l'articulation
        :param position: Position à atteindre
        :param temps_mouvement: Temps de mouvement en secondes
        :param bloquant: Si True, la fonction attend la fin du mouvement
        """
        self.marty.move_joint(articulation, position, temps_mouvement, bloquant)
    
    def marcher(self, pas, tourner=0, temps_mouvement=1, longueur_pas=50):
        """
        Faire marcher Marty un nombre spécifié de pas.
        :param pas: Nombre de pas à faire
        :param tourner: Angle de rotation à chaque pas
        :param temps_mouvement: Temps de mouvement en secondes
        :param longueur_pas: Longueur de chaque pas
        """
        self.marty.walk(pas, tourner, temps_mouvement, longueur_pas)
    
    def tourner(self, angle):
        """
        Faire tourner Marty d'un angle spécifique.
        :param angle: Angle en degrés
        """
        self.marty.turn(angle)
    
    def danse_cercle(self):
        """
        Faire danser Marty en cercle.
        """
        self.marty.circle_dance()

    def se_tenir_droit(self):
        """
        Faire tenir Marty droit.
        """
        self.marty.stand_straight()

    def incliner(self, direction):
        """
        Incliner Marty dans une direction spécifiée.
        :param direction: Direction d'inclinaison
        """
        self.marty.lean(direction)
    
    def bouger_oeil(self, oeil, position):
        """
        Bouger l'œil de Marty à une position spécifiée.
        :param oeil: Œil à bouger (gauche ou droit)
        :param position: Position à atteindre
        """
        self.marty.move_eye(oeil, position)
    
    def definir_led(self, led, r, g, b):
        """
        Définir la couleur d'une LED spécifique.
        :param led: LED à contrôler (gauche, droit, etc.)
        :param r: Valeur rouge (0-255)
        :param g: Valeur verte (0-255)
        :param b: Valeur bleue (0-255)
        """
        self.marty.set_led(led, r, g, b)
    
    def jouer_son(self, id_son):
        """
        Jouer un son par son ID.
        :param id_son: ID du son à jouer
        """
        self.marty.play_sound(id_son)
    
    def obtenir_distance(self):
        """
        Obtenir la lecture de distance du capteur de Marty.
        :return: Distance en centimètres
        """
        return self.marty.get_distance()

    def obtenir_accelerometre(self):
        """
        Obtenir les lectures de l'accéléromètre.
        :return: Données de l'accéléromètre
        """
        return self.marty.get_accelerometer()

    def arreter(self):
        """
        Arrêter tous les mouvements en cours.
        """
        self.marty.stop()

    def high_five(self):
        """
        Faire un high five avec Marty.
        """
        self.marty.high_five()
