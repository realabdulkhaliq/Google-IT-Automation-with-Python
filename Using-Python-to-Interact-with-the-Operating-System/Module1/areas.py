import math

def triangle(base, height):
    return 0.5 * base * height

def rectangle(length, width):
    return length * width

def circle(radius):
    return math.pi * radius ** 2

def donut(outside_radius, inside_radius):
    return circle(outside_radius) - circle(inside_radius)