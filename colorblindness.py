#   prolog
#   Author: Avity Ngonyani
#   Email:  avity4585@gmail.com
#   Project: Color blindness test
color = 'FFFFFF'
#   function to extract red
def get_red(color):
    redval = int(color[0:2], 16)
    return redval
#   function to extract green
def get_green(color):
    greenval = int(color[2:4], 16)
    return greenval
#   function to extract blue
def get_blue(color):
    blueval = int(color[4:6], 16)
    return blueval
# function to run tests
def run_tests():
    get_red(color)
    get_green(color)
    get_blue(color)

red_component = get_red(color)
green_component = get_green(color)
blue_component =  get_blue(color)
# print out the color codes for red green and blue
print(red_component, green_component, blue_component)
# determine if patient has protanopia
def id_protanopia():
    print('Test for protanopia')
    if red_component < 64:
        return 'True'
    else:
        return 'False'
# determine if patient has deuteranopia
def id_deuteranopia():
    print('Test for deuteranopia')
    if green_component < 64:
        return 'True'
    else:
        return 'False'
# determine if patient has tritanopia
def id_tritanopia():
    print('Test for tritanopia')
    if (blue_component > 0) and (red_component > 230) and (green_component > 220):
        return 'True'
    else: 
        return 'False'

print(id_protanopia())
print(id_deuteranopia())
print(id_tritanopia())

