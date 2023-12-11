import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    # rows = []
    # for row in input:
    #     rows.append([i for i in row])
    #     if "#" not in row:
    #         rows.append([i for i in row])
    # cols = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0])) ]
    # rows = []
    # for col in cols:
    #     rows.append([i for i in col])
    #     if "#" not in col:
    #         rows.append([i for i in col])

    # rows = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0])) ]
    # galaxies = []
    # for r, row in enumerate(rows):
    #     for c, col in enumerate(row):
    #         if col == "#":
    #             galaxies.append((r,c))
    
    # while galaxies:
    #     curr = galaxies.pop()
    #     for g in galaxies:
    #         ans1 += abs(curr[0]-g[0]) + abs(curr[1]-g[1])
    # Part 2


    rows = []
    empty_rows = []
    empty_cols = []
    for i, row in enumerate(input):
        rows.append([x for x in row])
        if "#" not in row:
            empty_rows.append(i)

    cols = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0])) ]

    for i, col in enumerate(cols):
        if "#" not in col:
            empty_cols.append(i)

    galaxies = []
    for r, row in enumerate(rows):
        for c, col in enumerate(row):
            if col == "#":
                galaxies.append((r,c))
    
    ans1 = 0
    while galaxies:
        curr = galaxies.pop()
        for g in galaxies:
            ans1 += abs(curr[0]-g[0]) + abs(curr[1]-g[1])
            ans2 += abs(curr[0]-g[0]) + abs(curr[1]-g[1])
            sr, er = (min([curr[0], g[0]]), max([curr[0], g[0]]))
            sc, ec = (min([curr[1], g[1]]), max([curr[1], g[1]]))
            for i in empty_rows:
                if i in range(sr,er+1):
                    ans1 += 1
                    ans2 += 999999
            for i in empty_cols:
                if i in range(sc,ec+1):
                    ans1 += 1
                    ans2 += 999999

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