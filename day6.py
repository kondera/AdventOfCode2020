from typing import List
from pprint import pprint

def get_count_of_group(group: str) -> int:
    """ab\nac"""
    group = set([x for x in group.strip() if x != '\n'])
    return len(group)

def get_anyone_counts(lst_of_groups: List[str]) -> int:
    return sum([get_count_of_group(x) for x in lst_of_groups])

def get_input() -> List[str]:
    with open('inputs/day6.txt') as f:
        data = f.read()
        data = data.split('\n\n')

    return data


print(get_anyone_counts(get_input()))


def part2(lst_of_str: List[str]) -> int:
    a = [[set(x) for x in y.split()] for y in lst_of_str]
    return sum([len(x[0].intersection(*x)) for x in a])

print(part2(get_input()))
