from __future__ import annotations
from typing import List, Tuple, NamedTuple

# PART 1
def earliest_bus(earliest_depart: int, departures: List[int]) -> int:
    earliest: Tuple[int, int] = (1, 10000)
    for departure in departures:
        diff = departure * ((earliest_depart // departure) + 1) - earliest_depart
        if earliest[1] > diff:
            earliest = (departure, diff)
    return earliest[0] * earliest[1]


# PART 2
class Bus(NamedTuple):
    bus_id: int
    wait: int

    @staticmethod
    def parse(raw: str) -> List[Bus]:
        return [Bus(int(x), i) for i, x in enumerate(raw.split(",")) if x != "x"]


def brute_force(buses: Bus) -> int:
    for num in range(1000000000000000):
        good_buses = 0
        for i, bus in enumerate(buses):
            if i == 0:
                continue
            if ((buses[0].bus_id * num) + bus.wait) % bus.bus_id == 0:
                good_buses += 1
            else:
                break
            if good_buses == len(buses) - 1:
                return buses[0].bus_id * num
    return -1


def congru(a: int, b: int, n: int) -> int:
    for k in range(0, n):
        if (a * k) % n == b:
            return k


def inverse(a: int, n: int):
    """
    https://en.wikipedia.org/wiki/Extended_Euclidean_algorithm#Modular_integers
    Find t such that a*t ≋ 1 (mod n)
    Examples:
    >>> inverse(3, 11)
    4
    which satisfies 3*4 ≋ 1 (mod 11)
    """

    t = 0
    newt = 1
    r = n
    newr = a

    while newr != 0:
        quotient = r // newr
        (t, newt) = (newt, t - quotient * newt)
        (r, newr) = (newr, r - quotient * newr)

    if r > 1:
        raise Exception("a is not invertible")
    if t < 0:
        t += n

    return t


def chinese_remainder_theorem(buses: List[Bus]) -> int:
    M = 1
    for bus in buses:
        M *= bus.bus_id
    Mi = [M // bus.bus_id for bus in buses]
    Yi = [congru(mi, 1, bus.bus_id) for mi, bus in zip(Mi, buses)]
    X = [(bus.bus_id - bus.wait) * mi * yi for bus, mi, yi in zip(buses, Mi, Yi)]
    return sum(X) % M


# # TEST
RAW = """939
7,13,x,x,59,x,31,19"""

# earliest_departure, buses = RAW.split("\n")
# buses = [int(x) for x in buses.split(",") if x != "x"]
# print(earliest_bus(int(earliest_departure), buses))
# buses = Bus.parse(RAW.split("\n")[1])
# print(brute_force(buses))
# print(chinese_remainder_theorem(buses))


# EXERCISE
with open("inputs/day13.txt") as f:
    erl_dep, buses = f.read().splitlines()

buses_ids = [int(x) for x in buses.split(",") if x != "x"]
print(earliest_bus(int(erl_dep), buses_ids))
buses = Bus.parse(buses)

n = [bus.bus_id for bus in buses]
a = [bus.bus_id - bus.wait for bus in buses]
print(chinese_remainder_theorem(buses))
