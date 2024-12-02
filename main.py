#import my_module

#from my_module import greeting

import modules.my_module as spam

print(dir(spam))

#print(my_module.person)

#print(greetng)

from color50 import rgb, constants
my_color = rgb(128, 0, 128)
print(constants.CYAN + "Hello, World!" + constants.RESET)