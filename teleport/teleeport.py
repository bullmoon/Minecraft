import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time
import datetime
import math

# Start code

pos = mc.player.getPos()
# mc.player.setTilePos(62, 63, -273) # Home
