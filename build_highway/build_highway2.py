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
width  = 6 # widt of road
length  = 250
high = 5

# Start code
time.sleep(3)
pos = mc.player.getPos()

# Create a base line, filling out of GRASS blocks
# mc.setBlocks(x,y,z,x+lenght,y,z,5)e
def build_foundation():
  time.sleep(2)
  print("Position X is", pos.x)
  print("Position Z is", pos.z)
  xxx = pos.x + 3
  zzz = pos.z + 1
  mc.setBlocks(xxx, pos.y - 1,    zzz, xxx - width, pos.y + high, zzz + length, block.AIR.id) # Full block
  mc.setBlocks(xxx, pos.y - 1,    zzz, xxx - width, pos.y - 1, zzz + length, block.WOOD.id) # Bottom
  mc.setBlocks(xxx, pos.y + high, zzz, xxx - width, pos.y + high, zzz + length, block.WOOD.id) # Ceiling
  
  mc.setBlocks(xxx, pos.y,        zzz, xxx, pos.y + high -1, zzz + length, block.FENCE_SPRUCE.id) # Left fence
  mc.setBlocks(xxx - width, pos.y, zzz, xxx - width, pos.y + high -1, zzz + length, block.FENCE_SPRUCE.id) # Right fence


# clearTerrain()
build_foundation()
# buildEmptyBox()
