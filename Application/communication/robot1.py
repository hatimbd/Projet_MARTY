from marty_robot import MartyRobot  # Assuming the class MartyRobot is saved in a file named marty_robot.py

robot1 = MartyRobot("192.168.1.10", "192.168.1.20")
robot1.start_server_thread()  # Start the server to receive data from the other robot
robot1.detect_and_communicate()  # Start detection and communication
