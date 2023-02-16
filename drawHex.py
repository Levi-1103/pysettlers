import pygame
import math

def hexToPixel(size, q, r, start):
    x = size * (math.sqrt(3) * q + math.sqrt(3) / 2 * r)
    y = size * (3 / 2 * r)
    return (x + start , y + start)

def vertToPixel(size, q, r, xoffset,yoffset):
    x = size * (math.sqrt(3) * q + math.sqrt(3) / 2 * r)
    y = size * (3 / 2 * r)
    return (x + xoffset , y + yoffset)


print(hexToPixel(10,1,1,0))
print(vertToPixel(10,1,1,-10,10))

#fix coord calculations so vertices and hexes align correctly