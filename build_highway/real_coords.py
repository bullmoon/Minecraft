import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'player_position'))
from gps import *
import mcpi.block as block # Now I can use block.BLOCK_NAME.id
import time
import datetime
import math

### Variables
# Size data
width  = 4    # parameter z (to the left of the cloud way)
length = 4    # parameter x (along the cloud way)
high   = 0    # parameter Y

xDelta = 2    # space in front of the player
zDelta = 2    # left shift of the player (along the cloud way)

# Start code
time.sleep(3)
pos = mc.player.getTilePos()

def buildEmptyBox():
  time.sleep(2)
  startPosX = pos.x - xDelta      # 
  finishPosX = startPosX - width  #
  startPosY = pos.y - 1
  finishPosY = startPosY - high
  startPosZ = pos.z + zDelta
  finishPosZ = startPosZ - width
  print("startPosX = pos.x - xDelta =", pos.x, "-", xDelta, "=", startPosX)
  print("finishPosX = startPosX - width =", startPosX, "-", width, "=", finishPosX)
  print("startPosZ = pos.x - zDelta =", pos.z, "+", zDelta, "=", startPosZ)
  print("finishPosZ = startPosZ - width =", startPosZ, "-", width, "=", finishPosZ)
  

  mc.setBlocks(startPosX, startPosY, startPosZ, finishPosX, finishPosY, finishPosZ, block.AIR.id) # Create an empty place
  
buildEmptyBox()
