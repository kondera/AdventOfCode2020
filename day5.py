from typing import List, Tuple

instructions = {
    'F': 1,
    'B': 0,
    'R': 0,
    'L': 1,
}

def lower_half(lst: List[int]) -> List[int]:
    return [lst[0], int((lst[0]+lst[1])/2)]

def upper_half(lst: List[int]) -> List[int]:
    return [int((lst[0] +lst[1])/2)+1, lst[1]]

def calculate_from_list(lst: List[int], lst_of_instr: List[int]) -> List[int]:
    for instr in lst_of_instr:
        if instr == 0:
            lst = upper_half(lst)
        else:
            lst = lower_half(lst)
    return lst

def parse(line: str) -> Tuple[int, int]:
    row_instr = [instructions.get(x) for x in line[:-3]]
    col_instr = [instructions.get(x) for x in line[-3:]]
    row = calculate_from_list([0,127], row_instr)[0]
    col = calculate_from_list([0,7], col_instr)[0]
    return row, col

def get_id_from_binary(line: str) -> int:
    row = int(''.join(['1' if i == 'B' else '0' for i in line[:-3]]), 2)
    col = int(''.join(['1' if i == 'R' else '0' for i in line[-3:]]), 2)
    return row * 8 + col

def calculate_id(line: str) -> int:
    r,c = parse(line)
    return r*8+c

def create_list_of_all_ids(lst: List[int]) -> List[int]:
    return [x for x in range(min(lst), max(lst))]

if __name__ == "__main__":
    with open('inputs/day5.txt') as f:
        # old way:
        # data = [calculate_id(line.strip()) for line in f.readlines()]
        # and new way:
        # yeah i didn't notice that binary code was the key
        data = [get_id_from_binary(line.strip()) for line in f.readlines()]
        print(max(data))
        all_ids = create_list_of_all_ids(data)
        diff = [x for x in all_ids if x not in data]
        print(diff)
