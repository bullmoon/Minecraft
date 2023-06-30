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
pos = mc.player.getPos()
cl = pos.y + 1


def testDoors():
    mc.setBlocks(pos.x + 3, cl, pos.z - 1, pos.x, 42)
    mc.setBlock(pos.x + 3, cl, pos.z + 1, 42)
    mc.setBlock(pos.x + 3, cl, pos.z, 324)
    mc.setBlock(pos.x + 3, cl + 1, pos.z, 324)

def install_door():
    time.sleep(1)
    for y in (cl, cl + 1):
        mc.setBlock(pos.x + 3, y, pos.z - 2, block.GRASS.id)
    time.sleep(1)
    for y in (cl, cl + 1):
        mc.setBlock(pos.x + 3, y, pos.z, block.GRASS.id)
    time.sleep(1)
    mc.setBlock(pos.x + 3, cl + 1, pos.z - 1, block.DOOR_WOOD.id, 8)  # Устанавливаем верхнюю часть двери
    time.sleep(1)
    mc.setBlock(pos.x + 3, cl, pos.z - 1, block.DOOR_WOOD.id, 0)  # Устанавливаем нижнюю часть двери

#sources()
#testDoors()
install_door()