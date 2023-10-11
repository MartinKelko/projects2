class Robot:

    #constructor
    def __init__(self, baterie, delka_rukou):
        self.bat = baterie
        self.del_ruk = delka_rukou
        self.ukony_do_kontroly = 1000
    
    def krok_vpred(self):
        print("robot ide vpred")
        self.ukony_do_kontroly -= 1
    def krok_vzad(self):
        print("robot ide dozadu")
        self.ukony_do_kontroly -= 1

    
robot_1 = Robot(24, 0.6)
robot_2 = Robot(48, 0.5)
robot_3 = Robot(50, 0.6)
robot_4 = Robot(38, 0.4)

print(robot_1.bat)
print(robot_1.del_ruk)
print(robot_1.ukony_do_kontroly)

robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()
robot_1.krok_vpred()
robot_1.krok_vzad()
print(robot_1.ukony_do_kontroly)

print(robot_2.bat)
print(robot_2.del_ruk)

print(robot_3.bat)
print(robot_3.del_ruk)

print(robot_4.bat)
print(robot_4.del_ruk)
