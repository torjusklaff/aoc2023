import pathlib
from Tools.common import readlinesfromfile, readfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    lines = input
    coords = [(r,c) for c in range(len(lines[0])) for r in range(len(lines))]
    stonemap = {}
    for coord in coords:
        stonemap[coord] = lines[coord[0]][coord[1]]
    # Part 1
    tilted = [[x for x in r] for r in lines]
    for r in range(1,len(lines)):
        for c in range(len(lines[0])):
            if lines[r][c] == "O":
                for un in range(r-1, -1, -1):
                    if tilted[un][c] != '.':
                        tilted[r][c] = '.'
                        tilted[un+1][c] = 'O'
                        break
                    elif un == 0 and tilted[un][c] == '.':
                        tilted[r][c] = '.'
                        tilted[un][c] = 'O'

    l = len(tilted)
    for r, row in enumerate(tilted):
        ans1 += row.count('O')*(l-r)
    

    # Part 2
    num_cycles = 1000000000

    cyc = 0
    rlen = len(lines)
    clen = len(lines[0])
    tilted = [[x for x in r] for r in lines]
    tilts = {}
    found = False
    import copy
    while cyc < num_cycles:
        for r in range(1,rlen):
            for c in range(clen):
                if tilted[r][c] == "O":
                    for un in range(r-1, -1, -1):
                        if tilted[un][c] != '.':
                            tilted[r][c] = '.'
                            tilted[un+1][c] = 'O'
                            break
                        elif un == 0 and tilted[un][c] == '.':
                            tilted[r][c] = '.'
                            tilted[un][c] = 'O'
        for c in range(1,clen):
            for r in range(rlen):
                if tilted[r][c] == "O":
                    for un in range(c-1, -1, -1):
                        if tilted[r][un] != '.':
                            tilted[r][c] = '.'
                            tilted[r][un+1] = 'O'
                            break
                        elif un == 0 and tilted[r][un] == '.':
                            tilted[r][c] = '.'
                            tilted[r][un] = 'O'
        for r in range(rlen-1,-1,-1):
            for c in range(clen):
                if tilted[r][c] == "O":
                    for un in range(r+1, rlen):
                        if tilted[un][c] != '.':
                            tilted[r][c] = '.'
                            tilted[un-1][c] = 'O'
                            break
                        elif un == rlen-1 and tilted[un][c] == '.':
                            tilted[r][c] = '.'
                            tilted[un][c] = 'O'
        for c in range(clen-1,-1,-1):
            for r in range(rlen):
                if tilted[r][c] == "O":
                    for un in range(c+1, clen):
                        if tilted[r][un] != '.':
                            tilted[r][c] = '.'
                            tilted[r][un-1] = 'O'
                            break
                        elif un == clen-1 and tilted[r][un] == '.':
                            tilted[r][c] = '.'
                            tilted[r][un] = 'O'
        cyc += 1
        if not found:
            for c, m in tilts.items():
                found = True
                for r, ro in enumerate(m):
                    if ro != tilted[r]:
                        found = False
                        break
                if not found:
                    continue

                cyc_left = num_cycles - cyc
                cyc_len = cyc - c
                cyc_its = cyc_left//cyc_len
                cyc += cyc_len*cyc_its
                break
            tilts[cyc] = copy.deepcopy(tilted)
        



    for r, row in enumerate(tilted):
        ans2 += row.count('O')*(l-r)

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