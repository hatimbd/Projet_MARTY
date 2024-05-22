from martypy import Marty

def Connection():
    global my_marty
    my_marty = Marty("wifi","192.168.0.8")
    
def Dance():    
    my_marty.dance()


Connection()
Dance()
