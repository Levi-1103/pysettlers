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


#fix coord calculations so vertices and hexes align correctly