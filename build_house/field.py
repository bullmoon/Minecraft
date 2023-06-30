import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time
import datetime
import math

### Variables
# Materials
STONE = 1
DIRT = 3
WATER = 8
FENCE = 85
FENCE_GATE = 107

# Size data
width  = 10 # width of house
height = 2 # hight of house
length = 10 # lenght of house

# Define current location
pos = mc.player.getTilePos()
print(f"\nCurrent position is {pos.x} {pos.y} {pos.z}")

closeX = pos.x + 2
print(f"Current closeX is {closeX}")
farX = closeX + length
print(f"Lenght of building is {closeX} to {farX}\n")

leftZ = pos.z - (width // 2)
rightZ = leftZ + width

def field():
    time.sleep(1)
    cl = pos.y                                                      # current level
    corners = [
        (closeX, cl + 2, leftZ),
        (farX, cl + 2, leftZ),
        (closeX, cl + 2, rightZ),
        (farX, cl + 2, rightZ)
    ]
    mc.setBlocks(closeX, cl - 1, leftZ, farX, cl - 1, rightZ, STONE)        # base for field
    mc.setBlocks(closeX, cl, leftZ, farX, cl, rightZ, DIRT)                 # field
    mc.setBlock(closeX + (length // 2), cl, leftZ + (length // 2), WATER)   # water on the centre
    for f in range(leftZ, rightZ):                                          # boarder
        mc.setBlock(closeX, cl + 1, f, FENCE)
        mc.setBlock(farX, cl + 1, f, FENCE)
    for f in range(closeX, farX):                                           # boarder
        mc.setBlock(f, cl + 1, leftZ, FENCE)
        mc.setBlock(f, cl + 1, rightZ, FENCE)                               
    mc.setBlock(closeX + (length // 2), cl + 1, leftZ, FENCE_GATE)
    for c in (corners):
        m = FENCE                                                            # material
        mc.setBlock(*c, m)
field()