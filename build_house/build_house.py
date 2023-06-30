import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time
import datetime
import math

### Variables
# Materials
air = 0
stone = 1
bricks = 45
stone_bricks = 98
wood = 5
glass = 20
# Size data
width  = 6 # width of house
height = 1 # hight of house
length = 6 # lenght of house

# Start code
time.sleep(3)
#mc.player.setPos(0.0, -58.0, 120.0)
pos = mc.player.getPos()

def clearTerrain():
  time.sleep (3)
  mc.postToChat("Clear terrain 10 block to each side and high 10 blocks")
  for i in range(1,10):
    mc.setBlocks(pos.x - 10, pos.y, pos.z -10, pos.x + i, pos.y +i, pos.z + i, air)
    time.sleep (1)

def build_foundation():
  time.sleep(2)
  mc.setBlocks(pos.x + 2, pos.y - 1, pos.z +2, pos.x + 2 + width, pos.y - 1, pos.z + 2 + length, block.GRASS.id)


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

clearTerrain()
build_foundation()
buildEmptyBox()
