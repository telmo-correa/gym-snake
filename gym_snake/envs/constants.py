from enum import IntEnum


class ObjectColor:
    """ Object color used on observation encoding """
    empty = 0, 0, 0
    apple = 255, 0, 0
    own_head = 0, 0, 255
    own_body = 0, 255, 0
    other_head = 128, 128, 255
    other_body = 128, 255, 128
    dead_head = 128, 128, 128
    dead_body = 64, 64, 64


class GridType(IntEnum):
    """ Style of grid to use for environment """
    square = 0
    hex = 1


class Action4(IntEnum):
    """ Actions to be taken by an agent in a square grid """
    forward = 0
    right = 1
    left = 2


class Action6(IntEnum):
    """ Actions to be taken by an agent in a hex grid """
    forward = 0
    right = 1
    right_right = 2
    left_left = 3
    left = 4


class Direction4(IntEnum):
    """ Square grid orientations """
    north = 0
    east = 1
    south = 2
    west = 3

    def add_action(self, action):
        if action == Action4.forward:
            return self

        if action == Action4.left:
            if self == Direction4.north:
                return Direction4.west
            if self == Direction4.west:
                return Direction4.south
            if self == Direction4.south:
                return Direction4.east
            return Direction4.north

        if action == Action4.right:
            if self == Direction4.north:
                return Direction4.east
            if self == Direction4.east:
                return Direction4.south
            if self == Direction4.south:
                return Direction4.west
            return Direction4.north

        raise ValueError('Unexpected action: ', action)

    def add_to_point(self, point):
        if self == Direction4.north:
            return point[0], point[1] - 1
        if self == Direction4.east:
            return point[0] + 1, point[1]
        if self == Direction4.south:
            return point[0], point[1] + 1
        return point[0] - 1, point[1]


class Direction6(IntEnum):
    """ Hex grid orientations (even-row coordinates) """
    northeast = 0
    east = 1
    southeast = 2
    southwest = 3
    west = 4
    northwest = 5

    def add_action(self, action):
        if action == Action6.forward:
            return self

        if action == Action6.left:
            if self == Direction6.northeast:
                return Direction6.northwest
            if self == Direction6.northwest:
                return Direction6.west
            if self == Direction6.west:
                return Direction6.southwest
            if self == Direction6.southwest:
                return Direction6.southeast
            if self == Direction6.southeast:
                return Direction6.east
            return Direction6.northeast

        if action == Action6.right:
            if self == Direction6.northwest:
                return Direction6.northeast
            if self == Direction6.northeast:
                return Direction6.east
            if self == Direction6.east:
                return Direction6.southeast
            if self == Direction6.southeast:
                return Direction6.southwest
            if self == Direction6.southwest:
                return Direction6.west
            return Direction6.northwest

        if action == Action6.left_left:
            if self == Direction6.northeast:
                return Direction6.west
            if self == Direction6.northwest:
                return Direction6.southwest
            if self == Direction6.west:
                return Direction6.southeast
            if self == Direction6.southwest:
                return Direction6.east
            if self == Direction6.southeast:
                return Direction6.northeast
            return Direction6.northwest

        if action == Action6.right_right:
            if self == Direction6.northwest:
                return Direction6.east
            if self == Direction6.northeast:
                return Direction6.southeast
            if self == Direction6.east:
                return Direction6.southwest
            if self == Direction6.southeast:
                return Direction6.west
            if self == Direction6.southwest:
                return Direction6.northwest
            return Direction6.northeast

        raise ValueError('Unexpected action: ', action)

    def add_to_point(self, point):
        if self == Direction6.east:
            return point[0] + 1, point[1]
        if self == Direction6.west:
            return point[0] - 1, point[1]

        py = point[1] % 2

        if self == Direction6.northeast:
            return point[0] + (1 - py), point[1] - 1
        if self == Direction6.southwest:
            return point[0] - py, point[1] + 1
        if self == Direction6.southeast:
            return point[0] + (1 - py), point[1] + 1
        return point[0] - py, point[1] - 1
