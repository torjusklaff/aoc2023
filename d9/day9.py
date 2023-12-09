import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
from collections import defaultdict

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    data_lines = [s_to_int_list(a) for a in input]


    for data_line in data_lines:
        data_line = [int(x) for x in data_line]
        diffs = defaultdict(int)
        diffs[0] = data_line
        zero_level = False
        level = 1
        while not zero_level:
            diffs[level] = []
            for j in range(1, len(diffs[level-1])):
                diffs[level].append(diffs[level-1][j]-diffs[level-1][j-1])
            
            if diffs[level] == [0 for a in range(len(diffs[level]))]:
                zero_level = True
            else:
                level += 1
        from copy import deepcopy
        diffs2 = deepcopy(diffs)
        for i in range(level-2, -1, -1):
            diffs[i].append(diffs[i][-1]+diffs[i+1][-1])
        ans1 += diffs[0][-1]
    # Part 2
        for i in range(level-2, -1, -1):
            diffs2[i].append(diffs2[i][0]-diffs2[i+1][-1])
        ans2 += diffs2[0][-1]

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print()
    print("Day: ")
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()