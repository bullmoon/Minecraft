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
# Materials
air = 0
blackwool = 1
whitewool = 35 
wood = 5
# Size data
width  = 6 # widt of road
length  = 250
high = 5

# Start code
time.sleep(3)
pos = mc.player.getPos()

# Create a base line, filling out of GRASS blocks
# mc.setBlocks(x,y,z,x+lenght,y,z,5)
def build_foundation():
  time.sleep(2)
  print("Position X is", pos.x)
  print("Position Z is", pos.z)
  xxx = pos.x - 1
  zzz = pos.z + 3
  mc.setBlocks(xxx, pos.y - 1, zzz, xxx + length, pos.y + high, zzz - width, block.AIR.id)
  mc.setBlocks(xxx, pos.y - 1, zzz, xxx + length, pos.y - 1, zzz - width, block.WOOD.id) # Bottom
  mc.setBlocks(xxx, pos.y + high, zzz, xxx + length, pos.y + high, zzz - width, block.WOOD.id) # Ceiling
  mc.setBlocks(xxx, pos.y, zzz, xxx + length, pos.y + high -1, zzz, block.FENCE_SPRUCE.id) # Left fence
  mc.setBlocks(xxx, pos.y, zzz - width, xxx + length, pos.y + high -1, zzz - width, block.FENCE_SPRUCE.id) # Right fence


def buildEmptyBox():
  time.sleep(2)
  startPosX = pos.x + 2
  finishPosX = startPosX + width
  startY = pos.y
  high = startY + 5
  startPosZ = pos.z +2
  finishPosZ = startPosZ + length

  mc.setBlocks(startPosX, startY, startPosZ, finishPosX, high, finishPosZ, block.WOOD_PLANKS.id) # Create a big box
  mc.setBlocks(startPosX + 1, startY, startPosZ + 1, finishPosX -1, high - 2, finishPosZ - 1, air)    # Cut a little box
  mc.setBlocks(startPosX, startY, startPosZ + 3, startPosX, startY + 1, startPosZ + 3, air)    # create a door
  mc.setBlock(startPosX, startY + 1, startPosZ + 3, block.DOOR_JUNGLE.id)    # create a door
  mc.setBlock(startPosX + 3, startY + 1, startPosZ, glass)    # create a window
  mc.setBlock(startPosX + 3, startY + 1, finishPosZ, glass)    # create a window

# clearTerrain()
build_foundation()
# buildEmptyBox()
