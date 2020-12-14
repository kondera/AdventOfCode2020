from __future__ import annotations
from typing import List, NamedTuple, Tuple


class Instruction(NamedTuple):
    action: str
    value: int

    @staticmethod
    def parse(line: str) -> Instruction:
        return Instruction(line[0], int(line[1:]))


DIRECTIONS = ["N", "E", "S", "W"]


class Ship:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.direction: str = "E"

    def process_instruction(self, instr: Instruction) -> None:
        if instr.action == "N":
            self.y += instr.value
        elif instr.action == "S":
            self.y -= instr.value
        elif instr.action == "E":
            self.x += instr.value
        elif instr.action == "W":
            self.x -= instr.value
        elif instr.action == "R":
            self.direction = DIRECTIONS[
                (DIRECTIONS.index(self.direction) + instr.value // 90) % 4
            ]
        elif instr.action == "L":
            self.direction = DIRECTIONS[
                (DIRECTIONS.index(self.direction) - instr.value // 90) % 4
            ]
        elif instr.action == "F":
            if self.direction == "N":
                self.y += instr.value
            elif self.direction == "S":
                self.y -= instr.value
            elif self.direction == "E":
                self.x += instr.value
            elif self.direction == "W":
                self.x -= instr.value

    def manhattan(self) -> int:
        return abs(self.x) + abs(self.y)


class ShipAndWaypoint:
    def __init__(self):
        self.x: int = 0
        self.y: int = 0
        self.direction: str = "E"
        self.waypoint_x: int = 10
        self.waypoint_y: int = 1

    def process_instruction(self, instr: Instruction) -> None:
        if instr.action == "N":
            self.waypoint_y += instr.value
        elif instr.action == "S":
            self.waypoint_y -= instr.value
        elif instr.action == "E":
            self.waypoint_x += instr.value
        elif instr.action == "W":
            self.waypoint_x -= instr.value
        elif instr.action == "R":
            # x,y = y,-x
            for _ in range(instr.value // 90):
                self.waypoint_x, self.waypoint_y = self.waypoint_y, -self.waypoint_x
        elif instr.action == "L":
            # x,y = -y,x
            for _ in range(instr.value // 90):
                self.waypoint_x, self.waypoint_y = -self.waypoint_y, self.waypoint_x
        elif instr.action == "F":
            self.x += instr.value * self.waypoint_x
            self.y += instr.value * self.waypoint_y

    def manhattan(self) -> int:
        return abs(self.x) + abs(self.y)


def parse_raw(raw: str) -> List[Instruction]:
    return [Instruction.parse(line) for line in raw.split("\n")]


# TESTS
RAW = """F10
N3
F7
R90
F11"""

# lst = parse_raw(RAW)

# s = Ship()
# for instr in lst:
#     s.process_instruction(instr)
# print(s.x, s.y)
# print(s.manhattan())

# s2 = ShipAndWaypoint()
# for instr in lst:
#     s2.process_instruction(instr)
# print(s2.x, s2.y, s2.waypoint_x, s2.waypoint_y)
# print(s2.manhattan())

# PUZZLE

with open("inputs/day12.txt") as f:
    data = [Instruction.parse(line) for line in f.read().split("\n")]

my_ship = Ship()
for instr in data:
    my_ship.process_instruction(instr)

print(my_ship.x, my_ship.y)
print(my_ship.manhattan())

my_ship2 = ShipAndWaypoint()
for instr in data:
    my_ship2.process_instruction(instr)

print(my_ship2.x, my_ship2.y)
print(my_ship2.manhattan())