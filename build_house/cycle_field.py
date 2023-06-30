import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time
import datetime
import math

# Size data
radius  = 20
height = 2

# Define current location
pos = mc.player.getTilePos()
print(f"\nCurrent position is {pos.x} {pos.y} {pos.z}")

# Center
x_center = pos.x + radius + 2
y_center = pos.y
z_center = pos.z

# Build field
def cyclefield():
    for x in range(x_center - radius, x_center + radius + 1):
        for z in range(z_center - radius, z_center + radius + 1):
            for high in range(0, 10):
                mc.setBlock(x, y_center + high, z, block.AIR.id)
            if math.sqrt((x - x_center) ** 2 + (z - z_center) ** 2) <= radius:
                time.sleep(0.1)
                mc.setBlock(x, y_center, z, block.GRASS.id)
    mc.setBlock(x, y_center, z, block.WATER.id)

cyclefield()