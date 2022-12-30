# -*- coding: utf-8 -*-

class Coordinate(object):
    def __init__(self,x,y):
        assert type(x) == int and type(y) == int
        self.x = x
        self.y = y
        
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"
        
    def __add__(self, other):
        return Coordinate(self.x + other.x, self.y + other.y)