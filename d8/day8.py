import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
import re

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    instructions = input[0].strip('\n')

    coords = {}
    for line in input[2::]:
        coord, lr = line.split(" = ")
        coords[coord] = re.findall(r'[\dA-Z]+', lr)
    
    curr = 'AAA'
    index = 0
    while curr != 'ZZZ':
        rl = instructions[index % len(instructions)]
        if rl == "L":
            curr = coords[curr][0]
        else:
            curr = coords[curr][1]
        index += 1
    
    ans1 = index


    # Part 2

    curr = [x for x in coords.keys() if x[2] == 'A']
    found_index = [0 for x in range(len(curr))]

    index = 0
    while not all(found_index):

        rl = instructions[index % len(instructions)]
        for i, c in enumerate(curr):
            if rl == "L":
                curr[i] = coords[c][0]
            else:
                curr[i] = coords[c][1]
            

        index += 1

        for c in range(len(curr)):
            if curr[c][2] == 'Z':
                found_index[c] = index


    from math import lcm
    ans2 = lcm(*found_index)

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()