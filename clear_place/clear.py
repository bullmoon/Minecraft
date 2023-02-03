import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time
import datetime
import math

# Variables
air = 0
stone = 1
bricks = 45
stone_bricks = 98

# Start code

pos = mc.player.getPos()

def build_stack():
  mc.postToChat("Clear terrain 10 block to each side and high 10 blocks")
  mc.setBlocks(pos.x - 10, pos.y, pos.z -10, pos.x + 10, pos.y +20, pos.z + 50, air)

build_stack()
