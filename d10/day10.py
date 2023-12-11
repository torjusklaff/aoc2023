import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    pipelines = input
    for i, p in enumerate(pipelines):
        if "S" in p:
            start = (i, p.index("S"))
            break
    
    pipes = "|LFJ-7"
    steps = [start]
    if pipelines[start[0]][ start[1] + 1] in "J-7":
        curr = (start[0], start[1] + 1)
    elif pipelines[start[0]][ start[1] - 1] in "L-F":
        curr = (start[0], start[1] - 1)
    elif pipelines[start[0] + 1][ start[1]] in "F|7":
        curr = (start[0] + 1, start[1] )
    elif pipelines[start[0] - 1][ start[1]] in "L|J":
        curr = (start[0] - 1, start[1])

    inside = {}

    while curr != start:
        diffr, diffc = (curr[0] - steps[-1][0], curr[1] - steps[-1][1])
        r, c = curr
        pipe = pipelines[r][c]
        steps.append(curr)
        if diffc == 1:  # came from west, possible curr = J-7
            if pipe == "J":

                curr = (r - 1, c)
            elif pipe == "-":
                curr = (r, c + 1)
            elif pipe == "7":
                curr = (r + 1, c)
        elif diffr == 1:  # came from north
            if pipe == "|":
                curr = (r + 1, c)
            elif pipe == "L":
                curr = (r, c + 1)
            elif pipe == "J":
                curr = (r, c - 1)
        elif diffc == -1:  # came from east
            if pipe == "F":
                curr = (r + 1, c)
            elif pipe == "-":
                curr = (r, c - 1)
            elif pipe == "L":
                curr = (r - 1, c)
        elif diffr == -1:  # came from south
            if pipe == "F":
                curr = (r, c + 1)
            elif pipe == "|":
                curr = (r - 1, c)
            elif pipe == "7":
                curr = (r, c - 1)
    
    ans1 = len(steps)/2
    # Part 2
    max_pos = len(pipelines)*len(p) - len(steps)

    # Anything in the loop is caught, find inside edge, check everything not in if surrounded by inside edges? 
    # Try to transpose so that we get a rectangle instead? 
    coor_inside = []
    prev = start

    # 450 > ans > 189 
    

    up = (start[0]-1, start[1])
    down = (start[0]+1, start[1])
    print(steps.index(start), steps.index(up), steps.index(down))
    inside = "up"
    for step in steps:
        r,c = step
        pipe = pipelines[r][c]


        if inside == "up":
            for i in range(r-1, -1, -1):
                if (i,c) in steps:
                    break
                else:
                    coor_inside.append((i,c))
        elif inside == "down":
            for i in range(r+1, len(pipelines)):
                if (i,c) in steps:
                    break
                else:
                    coor_inside.append((i,c))
        elif inside == "left":
            for i in range(c-1, -1, -1):
                if (r,i) in steps:
                    break
                else:
                    coor_inside.append((r,i))
        elif inside == "right":
            for i in range(c+1, len(pipelines[0])):
                if (r,i) in steps:
                    break
                else:
                    coor_inside.append((r,i))

        if pipe in "LFJ7":
            if inside == "up":
                if pipe in "L7": inside = "right"
                elif pipe in "FJ": inside = "left"
            elif inside == "down":
                if pipe in "L7": inside = "left"
                elif pipe in "FJ": inside = "right"
            elif inside == "left":
                if pipe in "JF": inside = "up"
                elif pipe in "L7": inside = "down"
            elif inside == "right":
                if pipe in "JF": inside = "down"
                elif pipe in "L7": inside = "up"

            if inside == "up":
                for i in range(r-1, -1, -1):
                    if (i,c) in steps:
                        break
                    else:
                        coor_inside.append((i,c))
            elif inside == "down":
                for i in range(r+1, len(pipelines)):
                    if (i,c) in steps:
                        break
                    else:
                        coor_inside.append((i,c))
            elif inside == "left":
                for i in range(c-1, -1, -1):
                    if (r,i) in steps:
                        break
                    else:
                        coor_inside.append((r,i))
            elif inside == "right":
                for i in range(c+1, len(pipelines[0])):
                    if (r,i) in steps:
                        break
                    else:
                        coor_inside.append((r,i))
        
    ans2 = len(set(coor_inside))

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print()
    print("Day: 10")
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()