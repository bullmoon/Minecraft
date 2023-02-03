import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'player_position'))
from gps import *
import mcpi.block as block
import time
import datetime
import math

### Variables
# Size data
size  = 6 # Block side

time.sleep(3)
pos = mc.player.getPos()

for i in range(80):
    mc.setBlock(pos.x - i, pos.y, pos.z, i)
    i += 1
