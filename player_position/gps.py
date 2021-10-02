import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time

# Code
time.sleep(3)
message = "Hello my wild world!"
print(message)
mc.postToChat(message)
pos = mc.player.getTilePos()
print(pos.x)
print(pos.y)
print(pos.z)
