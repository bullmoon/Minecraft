import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time

# Code
time.sleep(3)
message = "Start moving z"
print(message)
mc.postToChat(message)
pos = mc.player.getTilePos()
print("pos.x is ", pos.x)
print("pos.y is ", pos.y)
print("pos.z is ", pos.z)

mv = 1
while mv < 5:
    time.sleep(1)
    mc.player.setTilePos(pos.x, pos.y, pos.z)
    print(pos.z)
    pos.z +=1
    mv +=1