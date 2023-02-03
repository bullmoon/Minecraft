import sys, os
from tarfile import BLKTYPE
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
length = 8    # parameter x (along the cloud way)
high   = 0    # parameter Y
xDelta = 2    # space in front of the player
zDelta = 2    # left shift of the player (along the cloud way)

# Start code
time.sleep(3)
pos = mc.player.getTilePos()

def buildButtomLevel():
  high   = 0    # parameter Y
  blk    = block.COAL_ORE.id
  
  time.sleep(1)
  startPosX = pos.x - xDelta      # 
  finishPosX = startPosX - length  #
  startPosY = pos.y - 1
  finishPosY = startPosY - high
  startPosZ = pos.z + zDelta
  finishPosZ = startPosZ - width
  mc.setBlocks(startPosX, startPosY, startPosZ, finishPosX, finishPosY, finishPosZ, blk)
  return startPosX, startPosY, startPosZ, finishPosX, finishPosY, finishPosZ

def curb():
  stpx = buildButtomLevel()
  i = stpx[0]
  # blk = block.FENCE.id
  blk = block.STONE.id
  blk_type = 6      # "6" is a type of stone (STONE_ANDESITE_SMOOTH)

  while i >= stpx[3]:
    mc.setBlock(i, stpx[1], stpx[2], blk, blk_type) # left side
    mc.setBlock(i, stpx[1], stpx[5], blk, blk_type) # right side
    i -= 1

def streetLight():
  strl = buildButtomLevel()
  var_y = strl[0]
  
  blk = block.FENCE.id
  blk_light = block.TORCH.id
  blk_type = 5
  while var_y >= strl[3]:
    mc.setBlock(var_y, pos.y, strl[2], blk, blk_type) # left side fence
    mc.setBlock(var_y, pos.y, strl[5], blk, blk_type) # right side fence
    mc.setBlock(var_y, pos.y + 1, strl[2], blk_light, blk_type) # left side lamp
    mc.setBlock(var_y, pos.y + 1, strl[5], blk_light, blk_type) # right side lamp
    var_y -= 3

# buildEmptyBox()
buildButtomLevel()
streetLight()
curb()