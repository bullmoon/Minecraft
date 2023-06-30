import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'connection'))
from connect import *
import mcpi.block as block
import time
import datetime
import math

### Variables
# Materials
AIR = 0
STONE = 1
COBBLESTONE = 4
GRAVEL = 13
GOLDORE = 14
BRICK_BLOCK = 45
STONE_BRICK = 98
WOOD_PLANKS = 5
OAK_LOG = 17
OAK_STAIRS = 53
GLASS = 20
GLASS_PANE = 102
OAK_DOOR = 324

# Size data
width  = 12 # width of house
height = 10 # hight of house
length = 10 # lenght of house

# Define current location
pos = mc.player.getTilePos()
print(f"\nCurrent position is {pos.x} {pos.y} {pos.z}")

closeX = pos.x + 2
print(f"Current closeX is {closeX}")
farX = closeX + length
print(f"Lenght of building is {closeX} to {farX}\n")

leftZ = pos.z - (width // 2)
rightZ = leftZ + width - 1
print(f"Current leftZ is {leftZ}")
print(f"Current rightZ is {rightZ}")

# Layer functions
def clear():
    for item in range (0, height + 1):
        mc.setBlocks(closeX, pos.y - 1, leftZ - 10, farX + 10, pos.y - 1 + item, rightZ +10, AIR)

def layer_0():
    time.sleep(1)
    mc.setBlocks(closeX, pos.y - 1, leftZ, farX, pos.y - 1, rightZ, STONE)
    mc.setBlocks(closeX, pos.y - 1, leftZ, closeX + 4, pos.y - 1, leftZ + 5, GRAVEL)

def layer_1():
    time.sleep(1)
    cl = pos.y                                                                      # Current level
    mc.setBlocks(closeX, cl, leftZ + 5, closeX, cl, rightZ, WOOD_PLANKS)      # line 1
    for ol in(leftZ, leftZ + 5, rightZ):
        mc.setBlock(closeX, cl, ol, OAK_LOG)                                     # Install OAK LOGS on line 1

    mc.setBlock(closeX + 1, cl, leftZ + 5, WOOD_PLANKS)                          # line 2
    mc.setBlock(closeX + 1, cl, rightZ, WOOD_PLANKS)                             # line 2

    mc.setBlock(closeX + 2, cl, leftZ + 5, WOOD_PLANKS)                          # line 3
    mc.setBlock(closeX + 2, cl, rightZ, WOOD_PLANKS)                             # line 3

    mc.setBlock(closeX + 3, cl, pos.z, AIR)                                      # line 4
    mc.setBlock(closeX + 3, cl, rightZ, WOOD_PLANKS)                             # line 4

    mc.setBlocks(closeX + 4, cl, leftZ, closeX + 4, cl, rightZ, WOOD_PLANKS)  # line 5
    mc.setBlock(closeX + 4, cl, leftZ + 6, AIR)                                  # line 5
    for ol in(leftZ, rightZ):
        mc.setBlock(closeX + 4, cl, ol, OAK_LOG)                                 # Install OAK LOGS on line 5

    for row in range(5, 10):
        mc.setBlock(closeX + row, cl, leftZ, WOOD_PLANKS)                        # line 6-11
        mc.setBlock(closeX + row, cl, rightZ, WOOD_PLANKS)                       # line 6-11
    mc.setBlock(closeX + 6, cl, leftZ, OAK_LOG)                                  # OAK_LOG in line 7
    mc.setBlock(closeX + 7, cl, leftZ, AIR)                                      # line 8
    mc.setBlock(closeX + 8, cl, leftZ, OAK_LOG)                                  # OAK_LOG in line 9
    for wp10 in range(int(rightZ - 4), int(rightZ)):                                # WOOD_PLANKS in line 10
        mc.setBlock(closeX + 9, cl, wp10, WOOD_PLANKS)
    mc.setBlock(closeX + 9, cl, leftZ + 7, OAK_STAIRS, 2)                        # OAK_STAIRS in line 10
    mc.setBlocks(farX, cl, leftZ, farX, cl, rightZ, WOOD_PLANKS)              # line 11
    for ol11 in(leftZ, leftZ + 5, rightZ):
        mc.setBlock(closeX + 10, cl, ol11, OAK_LOG)                              # Install OAK LOGS on line 11

def layer_2():
    time.sleep(1)
    cl = pos.y + 1
    mc.setBlocks(closeX, cl, leftZ, closeX, cl, rightZ, WOOD_PLANKS)  # line 1
    mc.setBlocks(closeX, cl, leftZ + 1, closeX, cl, leftZ + 4, AIR)   # line 1
    for ol in(leftZ, leftZ + 5, rightZ):
        mc.setBlock(closeX, cl, ol, OAK_LOG)                                 # Install OAK LOGS on line 1
    for gl in(leftZ + 7, leftZ + 9):
        mc.setBlock(closeX, cl, gl, GLASS)                                   # Install GLASS on line 1
    mc.setBlock(closeX + 1, cl, leftZ + 5, GLASS)                            # Install GLASS on line 2
    mc.setBlock(closeX + 1, cl, rightZ, WOOD_PLANKS)                         # Install WOOD PLANKS on line 2
    mc.setBlock(closeX + 2, cl, rightZ, GLASS)                               # Install GLASS on line 3
    mc.setBlock(closeX + 2, cl, leftZ +5, WOOD_PLANKS)                       # Install WOOD PLANKS on line 3
    mc.setBlock(closeX + 3, cl, rightZ, WOOD_PLANKS)                         # Install WOOD PLANKS on line 4
    mc.setBlocks(closeX +4, cl, leftZ, closeX + 4, cl, rightZ, WOOD_PLANKS)  # line 5
    for ol in(leftZ, rightZ):
        mc.setBlock(closeX + 4, cl, ol, OAK_LOG)                             # Install OAK LOGS on line 5
    for gl in(leftZ + 2, leftZ + 3):
        mc.setBlock(closeX + 4, cl, gl, GLASS)                               # Install GLASS on line 5
    mc.setBlock(closeX + 4, cl, leftZ + 6, AIR)                              # AIR in line 5
    mc.setBlock(closeX + 5, cl, leftZ, GLASS)                                # GLASS in line 6
    mc.setBlock(closeX + 5, cl, rightZ, WOOD_PLANKS)                         # WOOD_PLANKS in line 6
    mc.setBlock(closeX + 6, cl, leftZ, OAK_LOG)                              # OAK_LOG in line 7
    mc.setBlock(closeX + 6, cl, rightZ, WOOD_PLANKS)                         # WOOD_PLANKS in line 7
    mc.setBlock(closeX + 7, cl, leftZ, AIR)                                  # AIR in line 8
    mc.setBlock(closeX + 7, cl, rightZ, GLASS)                               # GLASS in line 8
    mc.setBlock(closeX + 8, cl, leftZ, OAK_LOG)                              # OAK_LOG in line 9
    mc.setBlock(closeX + 8, cl, rightZ, GLASS)                               # GLASS in line 9
    mc.setBlock(closeX + 9, cl, leftZ, GLASS)                                # GLASS in line 10
    for wp10 in range(rightZ - 3, rightZ + 1):                                          # WOOD_PLANKS in line 10
        mc.setBlock(closeX + 9, cl, wp10, WOOD_PLANKS)
    mc.setBlock(closeX + 9, cl, leftZ + 8, OAK_STAIRS, 2)                        # OAK_STAIRS in line 10
    for wp11 in range(int(leftZ), int(rightZ)):
        mc.setBlock(closeX + 10, cl, wp11, WOOD_PLANKS)                        # WOOD_PLANKS in line 11
    for ol11 in(leftZ, leftZ + 5, rightZ):
        mc.setBlock(closeX + 10, cl, ol11, OAK_LOG)                            # Install OAK LOGS on line 11
    for gl11 in(leftZ + 2, leftZ + 3, leftZ + 6, leftZ + 7):
        mc.setBlock(closeX + 10, cl, gl11, GLASS)                              # Install GLASS on line 11

    doors = [
        (closeX + 7, cl, leftZ, block.DOOR_WOOD.id, 0),
        (closeX + 7, cl + 1, leftZ, block.DOOR_WOOD.id, 8),
        (closeX + 3, cl + 1, leftZ + 5, block.DOOR_WOOD.id, 8),
        (closeX + 3, cl, leftZ + 5, block.DOOR_WOOD.id, 0),
        (closeX + 4, cl + 1, leftZ + 6, block.DOOR_WOOD.id, 8),
        (closeX + 4, cl, leftZ + 6, block.DOOR_WOOD.id, 0)
    ]
    mc.setBlock(*doors)                                                         # Install the OAK_Doors
    mc.setBlock(closeX + 7, cl - 1, leftZ, block.DOOR_WOOD.id, 0)
    mc.setBlock(closeX + 7, cl, leftZ, block.DOOR_WOOD.id, 0)
    mc.postToChat("Дверь установлена!")

def layer_3():
    time.sleep(1)

    oak_blocks = [
        (closeX, pos.y + 2, leftZ, OAK_LOG),                    # line 1
        (closeX, pos.y + 2, leftZ + 5, OAK_LOG),
        (closeX, pos.y + 2, rightZ, OAK_LOG),
        (closeX + 4, pos.y + 2, leftZ, OAK_LOG),                    # line 5
        (closeX + 4, pos.y + 2, rightZ, OAK_LOG),
        (closeX + 6, pos.y + 2, leftZ, OAK_LOG),                    # line 7
        (closeX + 7, pos.y + 2, leftZ, OAK_LOG),                    # line 8
        (closeX + 8, pos.y + 2, leftZ, OAK_LOG),                    # line 9
        (closeX + 10, pos.y + 2, leftZ, OAK_LOG),                   # line 11
        (closeX + 10, pos.y + 2, leftZ + 5, OAK_LOG),
        (closeX + 10, pos.y + 2, rightZ, OAK_LOG)
    ]

    wood_planks_line = [
        (closeX, pos.y + 2, leftZ + 5, closeX, pos.y +2, rightZ, WOOD_PLANKS),                # line 1
        (closeX + 4, pos.y + 2, leftZ + 1, closeX + 4, pos.y + 2, rightZ - 1, WOOD_PLANKS),   # line 5
        (closeX + 10, pos.y + 2, leftZ + 1, closeX + 10, pos.y + 2, rightZ - 1, WOOD_PLANKS)  # line 11
    ]

    wood_planks_row = [
        (closeX + 4, pos.y + 2, leftZ, farX, pos.y + 2, leftZ, WOOD_PLANKS),                 # row 1
        (closeX + 1, pos.y + 2, leftZ + 5, closeX + 3, pos.y + 2, leftZ + 5, WOOD_PLANKS),   # row 6
        (farX - 1, pos.y + 2, rightZ - 2, farX - 1, pos.y + 2, rightZ, WOOD_PLANKS),         # row 10
        (closeX + 1, pos.y + 2, rightZ, farX, pos.y + 2, rightZ, WOOD_PLANKS)                # row 11
    ]

    for wpl in wood_planks_line:
        mc.setBlocks(*wpl)
    
    for wpr in wood_planks_row:
        mc.setBlocks(*wpr)

    for ob in oak_blocks:
        mc.setBlock(*ob)

    mc.setBlock(closeX + 9, pos.y + 2, leftZ + 9, OAK_STAIRS, 2)                        # OAK_STAIRS in line 10

def layer_4():
    time.sleep(1)

    mc.setBlocks(closeX, pos.y + 3, leftZ, farX, pos.y + 3, rightZ, WOOD_PLANKS)
    oak_logs_line = [
        (closeX, pos.y + 3, leftZ, closeX, pos.y + 3, rightZ, OAK_LOG),              # line 1
        (closeX + 4, pos.y + 3, leftZ, closeX + 4, pos.y + 3, rightZ, OAK_LOG),      # line 5
        (closeX + 10, pos.y + 3, leftZ, closeX + 10, pos.y + 3, rightZ, OAK_LOG),    # line 11
        (closeX, pos.y + 3, leftZ, farX, pos.y + 3, leftZ, OAK_LOG),                 # row 1
        (closeX, pos.y + 3, leftZ + 5, farX, pos.y + 3, leftZ + 5, OAK_LOG),         # row 6
        (closeX, pos.y + 3, rightZ, farX, pos.y + 3, rightZ, OAK_LOG),               # row 12
    ]
    
    for ol in oak_logs_line:
        mc.setBlocks(*ol)

    for air in range(rightZ - 5, rightZ - 1):
        mc.setBlock(farX - 1, pos.y + 3, air, AIR)
    mc.setBlock(closeX + 9, pos.y + 3, leftZ + 10, OAK_STAIRS, 2)                        # OAK_STAIRS in line 10

def layer_5():
    time.sleep(1)

    oak_planks = [
        (closeX, pos.y + 4, leftZ + 5, closeX, pos.y + 4, rightZ, WOOD_PLANKS),            # line 1
        (closeX + 4, pos.y + 4, leftZ, closeX + 4, pos.y + 4, rightZ, WOOD_PLANKS),        # line 5
        (closeX + 7, pos.y + 4, leftZ + 5, closeX + 7, pos.y + 4, rightZ - 2, WOOD_PLANKS),# line 8
        (closeX + 10, pos.y + 4, leftZ, closeX + 10, pos.y + 4, rightZ, WOOD_PLANKS),      # line 11
        (closeX + 4, pos.y + 4, leftZ, farX, pos.y + 4, leftZ, WOOD_PLANKS),               # row 1
        (closeX, pos.y + 4, leftZ + 5, farX, pos.y + 4, leftZ + 5, WOOD_PLANKS),           # row 6
        (closeX + 4, pos.y + 4, rightZ - 2, closeX + 7, pos.y + 4, rightZ - 2, WOOD_PLANKS),           # row 10
        (closeX, pos.y + 4, rightZ, farX, pos.y + 4, rightZ, WOOD_PLANKS)                  # row 12
    ]

    oak_logs = [
        (closeX, pos.y + 4, leftZ, OAK_LOG),            # line 1
        (closeX, pos.y + 4, leftZ + 5, OAK_LOG),        # line 1
        (closeX, pos.y + 4, rightZ, OAK_LOG),           # line 1
        (closeX + 4, pos.y + 4, leftZ, OAK_LOG),        # line 5
        (closeX + 4, pos.y + 4, rightZ, OAK_LOG),       # line 5
        (farX, pos.y + 4, leftZ, OAK_LOG),              # line 11
        (farX, pos.y + 4, leftZ + 5, OAK_LOG),          # line 11
        (farX, pos.y + 4, rightZ, OAK_LOG),             # line 11
    ]

    fordoors = [
        (closeX + 3, pos.y + 4, leftZ + 5, AIR),
        (closeX + 4, pos.y + 4, leftZ + 4, AIR),
        (closeX + 4, pos.y + 4, rightZ - 1, AIR),
        (closeX + 7, pos.y + 4, leftZ + 7, AIR),
        (farX - 1, pos.y + 4, leftZ + 5, AIR),
    ]

    for op in oak_planks:
        mc.setBlocks(*op)

    for ol in oak_logs:
        mc.setBlock(*ol)

    for do in fordoors:
        mc.setBlock(*do)

def layer_6():
    time.sleep(1)

    oak_planks = [
        (closeX, pos.y + 5, leftZ + 5, closeX, pos.y + 5, rightZ, WOOD_PLANKS),            # line 1
        (closeX + 4, pos.y + 5, leftZ, closeX + 4, pos.y + 5, rightZ, WOOD_PLANKS),        # line 5
        (closeX + 7, pos.y + 5, leftZ + 5, closeX + 7, pos.y + 5, rightZ - 2, WOOD_PLANKS),# line 8
        (closeX + 10, pos.y + 5, leftZ, closeX + 10, pos.y + 5, rightZ, WOOD_PLANKS),      # line 11
        (closeX + 4, pos.y + 5, leftZ, farX, pos.y + 5, leftZ, WOOD_PLANKS),               # row 1
        (closeX, pos.y + 5, leftZ + 5, farX, pos.y + 5, leftZ + 5, WOOD_PLANKS),           # row 6
        (closeX + 4, pos.y + 5, rightZ - 2, closeX + 7, pos.y + 5, rightZ - 2, WOOD_PLANKS),           # row 10
        (closeX, pos.y + 5, rightZ, farX, pos.y + 5, rightZ, WOOD_PLANKS)                  # row 12
    ]

    oak_logs = [
        (closeX, pos.y + 5, leftZ, OAK_LOG),            # line 1
        (closeX, pos.y + 5, leftZ + 5, OAK_LOG),        # line 1
        (closeX, pos.y + 5, rightZ, OAK_LOG),           # line 1
        (closeX + 4, pos.y + 5, leftZ, OAK_LOG),        # line 5
        (closeX + 4, pos.y + 5, rightZ, OAK_LOG),       # line 5
        (farX, pos.y + 5, leftZ, OAK_LOG),              # line 11
        (farX, pos.y + 5, leftZ + 5, OAK_LOG),          # line 11
        (farX, pos.y + 5, rightZ, OAK_LOG),             # line 11
    ]

    fordoors = [
        (closeX + 3, pos.y + 5, leftZ + 5, AIR),
        (closeX + 4, pos.y + 5, leftZ + 4, AIR),
        (closeX + 4, pos.y + 5, rightZ - 1, AIR),
        (closeX + 7, pos.y + 5, leftZ + 7, AIR),
        (farX - 1, pos.y + 5, leftZ + 5, AIR),
    ]

    window = [
        (closeX, pos.y + 5, rightZ - 4, GLASS),
        (closeX, pos.y + 5, rightZ - 2, GLASS),
        (closeX + 4, pos.y + 5, leftZ + 2, GLASS),
        (closeX + 5, pos.y + 5, leftZ, GLASS),
        (closeX + 7, pos.y + 5, rightZ, GLASS),
        (closeX + 8, pos.y + 5, rightZ, GLASS),
        (closeX + 9, pos.y + 5, leftZ, GLASS),
        (farX, pos.y + 5, leftZ + 2, GLASS),
        (farX, pos.y + 5, leftZ + 3, GLASS),
        (farX, pos.y + 5, leftZ + 6, GLASS),
        (farX, pos.y + 5, leftZ + 7, GLASS),
    ]

    for op in oak_planks:
        mc.setBlocks(*op)

    for ol in oak_logs:
        mc.setBlock(*ol)
    
    for do in fordoors:
        mc.setBlock(*do)
    
    for wd in window:
        mc.setBlock(*wd)

def layer_7():
    time.sleep(1)

    oak_planks = [
        (closeX, pos.y + 6, leftZ + 5, closeX, pos.y + 6, rightZ, WOOD_PLANKS),            # line 1
        (closeX + 4, pos.y + 6, leftZ, closeX + 4, pos.y + 6, rightZ, WOOD_PLANKS),        # line 5
        (closeX + 7, pos.y + 6, leftZ + 5, closeX + 7, pos.y + 6, rightZ - 2, WOOD_PLANKS),# line 8
        (closeX + 10, pos.y + 6, leftZ, closeX + 10, pos.y + 6, rightZ, WOOD_PLANKS),      # line 11
        (closeX + 4, pos.y + 6, leftZ, farX, pos.y + 6, leftZ, WOOD_PLANKS),               # row 1
        (closeX, pos.y + 6, leftZ + 5, farX, pos.y + 6, leftZ + 5, WOOD_PLANKS),           # row 6
        (closeX + 4, pos.y + 6, rightZ - 2, closeX + 7, pos.y + 6, rightZ - 2, WOOD_PLANKS),           # row 10
        (closeX, pos.y + 6, rightZ, farX, pos.y + 6, rightZ, WOOD_PLANKS)                  # row 12
    ]

    oak_logs = [
        (closeX, pos.y + 6, leftZ, OAK_LOG),            # line 1
        (closeX, pos.y + 6, leftZ + 5, OAK_LOG),        # line 1
        (closeX, pos.y + 6, rightZ, OAK_LOG),           # line 1
        (closeX + 4, pos.y + 6, leftZ, OAK_LOG),        # line 5
        (closeX + 4, pos.y + 6, rightZ, OAK_LOG),       # line 5
        (farX, pos.y + 6, leftZ, OAK_LOG),              # line 11
        (farX, pos.y + 6, leftZ + 5, OAK_LOG),          # line 11
        (farX, pos.y + 6, rightZ, OAK_LOG),             # line 11
    ]

    for op in oak_planks:
        mc.setBlocks(*op)

    for ol in oak_logs:
        mc.setBlock(*ol)

def layer_8():
    time.sleep(1)
    cf = pos.y + 7  # Current floor
    layer = [
        (closeX, cf, leftZ, farX - 1, cf, rightZ, OAK_LOG),                 # Fill out the floor
        (closeX, cf, leftZ, closeX + 4, cf, leftZ + 5, WOOD_PLANKS),        # Fill in the terrace
        (closeX + 1, cf, leftZ + 7, farX - 2, cf, leftZ + 9, AIR),          # Cut out vert
        (closeX + 6, cf, leftZ + 1, farX - 2, cf, rightZ - 1, AIR),         # Cut out horiz
        (closeX, cf, rightZ, closeX + 4, cf, rightZ, AIR),                  # Cut out small vert
    ]
    for bl in layer:
        mc.setBlocks(*bl)

def layer_9():
    time.sleep(1)
    cf = pos.y + 8  # Current floor
    layer = [
        (closeX + 1, cf, leftZ + 7, farX - 2, cf, leftZ + 9, OAK_LOG),    # Fill in Vert
        (closeX + 6, cf, leftZ + 1, farX - 2, cf, rightZ - 1, OAK_LOG),   # Fill in Horiz
        (closeX + 2, cf, leftZ + 8, farX - 3, cf, leftZ + 8, AIR),        # Cut out Vert
        (closeX + 7, cf, leftZ + 2, closeX + 7, cf, rightZ - 2, AIR),     # Cut out Horiz
    ]
    for bl in layer:
        mc.setBlocks(*bl)

def layer_10():
    time.sleep(1)
    cf = pos.y + 9  # Current floor
    layer = [
        (closeX + 2, cf, leftZ + 8, farX - 3, cf, leftZ + 8, OAK_LOG),     # Fill in Vert
        (closeX + 7, cf, leftZ + 2, closeX + 7, cf, rightZ - 2, OAK_LOG)   # Fill in Horiz
    ]
    for bl in layer:
        mc.setBlocks(*bl)

# Building
time.sleep(1)
clear()
layer_0()
layer_1()
layer_2()
layer_3()
layer_4()
layer_5()
layer_6()
layer_7()
layer_8()
layer_9()
layer_10()