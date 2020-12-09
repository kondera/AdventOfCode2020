from __future__ import annotations
from typing import List, Set, Tuple
from pprint import pprint

RAW = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""


def is_num_valid(preamble: Set[int], num: int) -> bool:
    for el in preamble:
        if (num - el) in preamble:
            return True
    return False


def traverse_xmas(raw: str, lenght_of_preamble: int) -> int:
    nums = [int(x) for x in raw.split("\n")]
    for i, num in enumerate(nums):
        if i < lenght_of_preamble:
            continue
        preamble = set(nums[i - lenght_of_preamble : i])
        if not is_num_valid(preamble, num):
            return num
    return -1


def contigious_set_min_max(raw: str, goal_num: int) -> Tuple[int, int]:
    contigious_set: List[int] = []
    tolerance = 2
    for num in [int(x) for x in raw.split("\n")]:
        if sum(contigious_set) == goal_num:
            return (min(contigious_set), max(contigious_set))
        if sum(contigious_set) < goal_num:
            contigious_set.append(num)
        while sum(contigious_set) > goal_num:
            contigious_set.pop(0)
        # print(sum(contigious_set))


with open("inputs/day9.txt") as f:
    raw = f.read()

wrong_num = traverse_xmas(raw, 25)
print(wrong_num)
print(sum(contigious_set_min_max(raw, wrong_num)))