class Robot:

    #constructor
    def __init__(self, baterie, delka_rukou):
        self.bat = baterie
        self.del_ruk = delka_rukou
    

robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(50, 0.6)
robot_4 = Robot(38, 0.4)

print(robot_1.bat)
print(robot_1.del_ruk)

print(robot_2.bat)
print(robot_2.del_ruk)

print(robot_3.bat)
print(robot_3.del_ruk)

print(robot_4.bat)
print(robot_4.del_ruk)
