from __future__ import annotations
from typing import List
from pprint import pprint

Grid = List[List[str]]

adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def evolve(grid: Grid, i: int, j: int) -> str:
    rows = len(grid)
    cols = len(grid[0])
    neighbors = {"#": 0, "L": 0, ".": 0}
    for adj_i, adj_j in adjacent:
        if 0 <= i + adj_i < rows and 0 <= j + adj_j < cols:
            neighbors[grid[i + adj_i][j + adj_j]] += 1

    cell = grid[i][j]
    if cell == "L" and neighbors["#"] == 0:
        return "#"
    elif cell == "#" and neighbors["#"] >= 4:
        return "L"
    else:
        return cell


def evolution(grid: Grid) -> Grid:
    return [
        [evolve(grid, i, j) for j, c in enumerate(row)] for i, row in enumerate(grid)
    ]


def stabilize(grid: Grid) -> int:
    while True:
        g = evolution(grid)
        if g == grid:
            break
        grid = g
    return sum(c == "#" for row in grid for c in row)


def find_first_seat(grid: Grid, i: int, j: int, di: int, dj: int) -> str:
    rows = len(grid)
    cols = len(grid[0])

    while True:
        i += di
        j += dj
        if 0 <= i < rows and 0 <= j < cols:
            if grid[i][j] == "#" or grid[i][j] == "L":
                return grid[i][j]
        else:
            return "."


def evolve2(grid: Grid, i: int, j: int):
    rows = len(grid)
    cols = len(grid[0])

    neighbors = {"#": 0, "L": 0, ".": 0}
    for di, dj in adjacent:
        first_seat = find_first_seat(grid, i, j, di, dj)
        neighbors[first_seat] += 1

    cell = grid[i][j]
    if cell == "L" and neighbors["#"] == 0:
        return "#"
    elif cell == "#" and neighbors["#"] >= 5:
        return "L"
    else:
        return cell


def evolution2(grid: Grid) -> Grid:
    return [
        [evolve2(grid, i, j) for j, c in enumerate(row)] for i, row in enumerate(grid)
    ]


def stabilize2(grid: Grid) -> int:
    while True:
        g = evolution2(grid)
        if g == grid:
            break
        grid = g
    return sum(c == "#" for row in grid for c in row)


# TESTS
RAW = """L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL"""


GRID = [list(row) for row in RAW.split("\n")]
print(stabilize(GRID))
pprint(stabilize2(GRID))

# REAL DATA
with open("inputs/day11.txt") as f:
    data = [list(line.strip()) for line in f]

print(stabilize(data))
print(stabilize2(data))