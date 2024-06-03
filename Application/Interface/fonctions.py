import sys
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QHBoxLayout, QGroupBox, QLineEdit
from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize
from PyQt6.QtGui import QIcon
from martypy import Marty, MartyConfigException
import threading
def walk(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher, args=(5))
            mon_thread.start()

    def dance(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.danse)
            mon_thread.start()
            
    def celebrer(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.celebration)
            mon_thread.start()

    def stand_straight(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.se_tenir_droit)
            mon_thread.start()

    def play_sound(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.jouer_son, args=(1))
            mon_thread.start()

    def get_distance(self):
        if self.marty_robot:
            distance = self.marty_robot.obtenir_distance()
            mon_thread = threading.Thread(target = self.status_label.setText(f'Distance: {distance} cm'))
            mon_thread.start()

    def get_accelerometer(self):
        if self.marty_robot:
            accelerometer = self.marty_robot.obtenir_accelerometre()
            mon_thread = threading.Thread(target = self.status_label.setText(f'Accéléromètre: {accelerometer}'))
            mon_thread.start()

    def stop(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.arreter)
            mon_thread.start()

    def high_five(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.high_five)
            mon_thread.start()
    
    def turn_right(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.tourner_droite)
            mon_thread.start()
    
    def turn_left(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.tourner_gauche)
            mon_thread.start()
    
    def move_forward(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher_avant)
            mon_thread.start()
    
    def move_backward(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher_arriere)
            mon_thread.start()

    def turn_right1(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher, args=(3, 'auto', -20, 25, 3000))
            mon_thread.start()
        
    def turn_left1(self):
        if self.marty_robot:
            mon_thread = threading.Thread(target = self.marty_robot.marcher, args=(3, 'auto', 20, 25, 3000))
            mon_thread.start()
    
    def get_battery(self):
        if self.marty_robot:
            battery = self.marty_robot.obtenir_niveau_batterie()
            mon_thread = threading.Thread(target = self.battery_label.setText(f'Niveau de batterie: {battery["percentage"]}%'))
            mon_thread.start()
    
    def move_eyes(self):
        if self.marty_robot:
            pose_or_angle = self.eyes_input.text()
            try:
                # Check if the input is a number and convert to int
                pose_or_angle = int(pose_or_angle)
            except ValueError:
                # If input is not a number, it will be treated as a pose string
                pass
            self.marty_robot.bouger_oeil(pose_or_angle)
