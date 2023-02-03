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

def coub():
    ### Variables
    # current location
    pos = mc.player.getTilePos()

    # Size data
    width  = 18    # parameter z (to the left of the cloud way)
    length = 18    # parameter x (along the cloud way)
    height = 8    # parameter Y
    xDelta = 2    # space in front of the player
    zDelta = 9    # left shift of the player (along the cloud way)
    
    # start building position
    startX = pos.x - xDelta
    startY = pos.y - 1
    startZ = pos.z + zDelta
    foundation = block.STONE_BRICK.id
    walls = block.BRICK_BLOCK.id
    AIR = 0
    spawner_id = 52
    
    # foundation
    mc.setBlocks(startX, startY, startZ, startX - length, startY, startZ - width, foundation, 3)
    # 2-nd line
    time.sleep(1)
    i = 1
    while i < height:
        mc.setBlocks(startX, startY + i, startZ, startX - length, startY + i, startZ - width, walls)
        mc.setBlocks(startX - 1, startY + i, startZ - 1 , startX - length + 1, startY + i, startZ - width + 1, AIR)
        i += 1
    print(i)
    # roof
    mc.setBlocks(startX, startY + height, startZ, startX - length, startY + height, startZ - width, foundation, 3)
    # water channel 1
    mc.setBlocks(startX -1, startY + 1, startZ - 1, startX - length, startY + 2, startZ - width + 1, foundation, 2) # fill in with stone
    mc.setBlocks(startX -1, startY + 1, pos.z, startX - length + 1, startY + 2, pos.z, AIR) # fill in with air
    mc.setBlock(startX - 1, startY + 1, pos.z, 8) # flowing water
    mc.setBlock(startX - length + 1, startY + 1, pos.z, 8) # flowing water
    mc.setBlock(startX - 9, startY, pos.z, AIR) # out space
    # water channel 2
    mc.setBlocks(startX -9, startY + 1, startZ - 1, startX - 9, startY + 2, startZ - width + 1, AIR) # fill in with air
    mc.setBlock(startX - 9, startY + 1, startZ - 1, 8) # flowing water
    mc.setBlock(startX - 9, startY + 1, startZ - width + 1, 8) # flowing water
    # spawner place
    mc.setBlock(startX - 9, startY + 4, pos.z, spawner_id, 10) # flowing water
coub()