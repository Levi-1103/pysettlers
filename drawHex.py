import pygame
import math

def hexToPixel(size, q, r):
    x = size * (math.sqrt(3) * q + math.sqrt(3) / 2 * r)
    y = size * (3 / 2 * r)
    return (x , y)


print(hexToPixel(25,4,4))