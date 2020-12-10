from __future__ import annotations
from typing import Dict, List, Tuple


def sort_and_create_chain(
    lst_of_voltages: List[int],
) -> Tuple[List[int], Dict[int, int]]:
    lst = sorted(lst_of_voltages + [0])
    diff = {0: 0, 1: 0, 2: 0, 3: 0}

    chain = []
    for i in range(len(lst) - 1):
        if (lst[i + 1] - lst[i]) <= 3:
            diff[lst[i + 1] - lst[i]] += 1
            chain.append(lst[i + 1])
        else:
            break

    chain.append(chain[-1] + 3)
    diff[3] += 1
    return chain, diff


def part1(dict_of_diff: Dict[int, int]) -> int:
    return dict_of_diff[1] * dict_of_diff[3]


# using Joel Grus code, didn
def part2(lst_of_adapters: List[int]) -> int:
    adapters = sorted(lst_of_adapters + [0])
    adapters.append(adapters[-1] + 3)

    end = adapters[-1]

    ways = [0] * (end + 1)

    ways[0] = 1
    ways[1] = 1 if 1 in adapters else 0
    if 2 in adapters and 1 in adapters:
        ways[2] = 2
    elif 2 in adapters:
        ways[2] = 1

    for n in range(3, end + 1):
        if n not in adapters:
            continue

        ways[n] = sum(ways[n - 3 : n])

    return ways[end]


# my improved version
def part2_improved(lst_of_adapters: List[int]) -> int:
    lst_of_adapters.append(max(lst_of_adapters) + 3)
    ways = [1] + [0] * max(lst_of_adapters)
    for x in sorted(lst_of_adapters):
        ways[x] = sum(ways[max(0, x - 3) : x])
    return ways[max(lst_of_adapters)]


# other solution using math
# explanation:
# https://www.reddit.com/r/adventofcode/comments/ka9pc3/2020_day_10_part_2_suspicious_factorisation/
def part2_math(
    lst_of_voltages: List[int],
) -> int:
    pow2 = 0
    pow7 = 0
    lst = sorted(lst_of_voltages + [0])
    lst.append(lst[-1] + 3)

    for i in range(1, len(lst) - 1):
        if i >= 3 and (lst[i + 1] - lst[i - 3]) == 4:
            pow7 += 1
            pow2 -= 2
        elif (lst[i + 1] - lst[i - 1]) == 2:
            pow2 += 1

    return (2 ** pow2) * (7 ** pow7)


with open("inputs/day10.txt") as f:
    data = f.read()

print("Part 1 and part 2:")
lst_of_ints = [int(x) for x in data.split("\n")]
chain, diff = sort_and_create_chain(lst_of_ints)
print(part1(diff))
print(part2_improved(lst_of_ints))

# TESTS
RAW = """16
10
15
5
1
11
7
19
6
12
4"""

RAW2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""

print("\nTests:")
a = [int(x) for x in RAW.split("\n")]
chain, diff = sort_and_create_chain(a)
print(part1(diff))
print(part2_improved(a))


a = [int(x) for x in RAW2.split("\n")]
chain, diff = sort_and_create_chain(a)
print(part1(diff))
print(part2_improved(a))
