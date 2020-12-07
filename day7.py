from __future__ import annotations
from typing import NamedTuple, List, Dict
from collections import deque


class Bag(NamedTuple):
    color: str
    holds: Dict[str, int]


def parse_line(line: str) -> Bag:
    lst = line.split("contain")
    color = " ".join(line.split()[:2])
    if "no other bags" in lst[1]:
        holds = {}
    else:
        holds = {
            " ".join(x.strip().split(" ")[1:3]): int(x.strip().split(" ")[0])
            for x in lst[1].strip().split(",")
        }
    return Bag(color, holds)


def ready_for_bfs(lst_of_bags: List[Bag]) -> Dict[str, List[str]]:
    bfs_ready: Dict[str, List[str]] = {}
    for bag in lst_of_bags:
        for child in bag.holds:
            if bfs_ready.get(child):
                bfs_ready[child].append(bag.color)
            else:
                bfs_ready[child] = [bag.color]
    return bfs_ready


def part_1(dct: Dict[str : List[str]]) -> int:
    checked = set()
    q = deque(["shiny gold"])

    while q:
        child = q.popleft()
        checked.add(child)
        for el in dct.get(child, []):
            if el not in checked:
                q.append(el)
    return len(checked) - 1


def part_2(bags: List[Bag]) -> int:
    colors = {bag.color: bag for bag in bags}

    result = 0
    stack = [("shiny gold", 1)]
    while stack:
        color, mult = stack.pop()
        bag = colors[color]
        for child, count in bag.holds.items():
            result += mult * count
            stack.append((child, count * mult))
    return result


with open("inputs/day7.txt") as f:
    bags = [parse_line(x) for x in f.readlines()]
    print(part_1(ready_for_bfs(bags)))
    print(part_2(bags))
