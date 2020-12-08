from __future__ import annotations
from typing import NamedTuple, List, Set


class Instruction(NamedTuple):
    operation: str
    argument: int

    @staticmethod
    def parse(line: str) -> Instruction:
        op, arg = line.split()
        return Instruction(op, int(arg))


class Program:
    def __init__(self, instructions: List[Instruction]) -> None:
        self.instructions = instructions
        self.accumulator = 0
        self.index = 0

    def execute_instruction(self) -> None:
        op, arg = self.instructions[self.index]

        if op == "nop":
            self.index += 1
        elif op == "acc":
            self.index += 1
            self.accumulator += arg
        elif op == "jmp":
            self.index += arg

    def run_one_loop(self) -> None:
        executed: Set[int] = set()

        while self.index not in executed:
            executed.add(self.index)
            self.execute_instruction()

    def program_ends(self) -> bool:
        executed: Set[int] = set()

        while self.index not in executed:
            if self.index == len(self.instructions):
                return True
            executed.add(self.index)
            self.execute_instruction()

        return False


def repair_program(lst_of_instr: List[Instruction]) -> int:
    for i, (op, arg) in enumerate(lst_of_instr):
        instr = lst_of_instr[:]

        if op == "jmp":
            instr[i] = Instruction("nop", arg)
        elif op == "nop":
            instr[i] = Instruction("jmp", arg)

        pr = Program(instr)
        if pr.program_ends():
            return pr.accumulator

    return -1


with open("inputs/day8.txt") as f:
    instr = [Instruction.parse(x) for x in f.readlines()]

# part 1
p = Program(instr)
p.run_one_loop()
print(p.accumulator)
# part 2
print(repair_program(instr))

# RAW = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6"""

# instructions = [Instruction.parse(x) for x in RAW.split("\n")]
# print(repair_program(instructions))
# program = Program(instructions)
# program.run_one_loop()
# print(program.accumulator)