from ev3robot import *
robot = LegoRobot()
gear = Gear()
robot.addPart(gear)

def kuer():
    gear.right(100)
    gear.forward(300)
    gear.left(30)
    leftArc(18,500)
    gear.right(200)
    leftArc(18,500)
    gear.left(30)
    gear.forward(300)
    
    
kuer()
