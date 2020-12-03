from functools import reduce

def ready_data(down=1):
    with open('inputs/day3.txt') as f:
        data = f.readlines()[::down]
        data = [list(x.strip('\n')) for x in data]
    return data

def encountered_trees(right, down=1):
    trees = 0
    for i, line in enumerate(ready_data(down)):
        if line[i * right % len(line)] == '#':
            trees += 1
    return trees


def multiple_trees(lst_of_slopes):
    result = [encountered_trees(*x) for x in lst_of_slopes]
    return reduce((lambda x,y: x*y), result)

if __name__ == '__main__':
    print("First part:")
    print(encountered_trees(3,1))
    print("Second part")
    print(multiple_trees([(1,1), (3,1), (5,1), (7,1), (1,2)]))
