import pygame
import math


def hexToPixel(size, q, r, offset):
    """
    Converts the hex grid coordinates to pixel coordinates

            Parameters:
                    size: The size of hexagons in the grid
                    q (int): q coordinate
                    r (int): r coordinate
                    offset: amount to offset pixel coordinates

            Returns:
                    (x-coord, y-coord)
    """

    x = size * (math.sqrt(3) * q + math.sqrt(3) / 2 * r)
    y = size * (3 / 2 * r)
    return (x + offset, y + offset)


def vertToPixel(size, q, r, xoffset, yoffset):
    """
    Converts the hex grid coordinates of vertices or edges to pixel coordinates

            Parameters:
                    size: The size of hexagons in the grid
                    q (int): q coordinate
                    r (int): r coordinate
                    xoffset: amount to offset x coordinates
                    yoffset: amount to offset y coordinates

            Returns:
                    (x-coord, y-coord)
    """
    x = size * (math.sqrt(3) * q + math.sqrt(3) / 2 * r)
    y = size * (3 / 2 * r)
    return (x + xoffset, y + yoffset)

