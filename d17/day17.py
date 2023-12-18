import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
from functools import cache
import time

day = 17
dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}

@cache
def search(heat, lowest, path, heatmap):
    r,c = path[-1]
    heat += heatmap[r][c]
    nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
    for nb in nbs:
        if nb not in path:
            break


    return lowest
def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    dirs = { 'u':(-1,0), 'l': (0,-1), 'r': (0,1), 'd':(1,0)}

    heat_loss_map = [[int(x) for x in r] for r in input]
    rmax = len(heat_loss_map)
    cmax = len(heat_loss_map[0])
    import math
    dist = [[math.inf for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]
    prev = [[[] for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]
    q2 = [[True for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]
    dist[0][0] = 0
    q = [(r,c) for c in range(len(heat_loss_map[0])) for r in range(len(heat_loss_map))]

    dirsteps = 0
    #ans > 937 < 997
    while q:
        mindist = math.inf
        for coord in q:
            if dist[coord[0]][coord[1]] < mindist:
                f = coord
                mindist = dist[coord[0]][coord[1]]
        r,c = q.pop(q.index(f))
        q2[r][c] = False
        nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
        for nb in nbs:
            try:
                if nb[0] >= 0 and nb[1] >= 0:
                    if q2[nb[0]][nb[1]]:
                        rb,cb = nb
                        if prev[r][c] and len(prev[r][c]) == 3:
                            re, ce = prev[r][c][0]
                            if abs(re-rb) == 4 or abs(ce-cb) == 4:
                                continue
                                
                        ndist = mindist + heat_loss_map[rb][cb]
                        if ndist < dist[rb][cb]:
                            dist[rb][cb] = ndist
                            if prev[r][c]:
                                if len(prev[r][c]) < 3:
                                    prev[rb][cb] = [x for x in prev[r][c]]
                                    prev[rb][cb].append((r,c))
                                else:
                                    prev[rb][cb] = [x for x in prev[r][c][1:]]
                                    prev[rb][cb].append((r,c))
                            else:
                                prev[rb][cb] = [(r,c)]
            except IndexError:
                pass


    ans1 = dist[rmax-1][cmax-1]
    start = (rmax-1,cmax-1)
    steps = [start]
    while start != (0,0):
        start = prev[start[0]][start[1]][-1]
        steps.append(start)
    for r in range(rmax):
        p = ''
        for c in range(cmax):
            if (r,c) in steps:
                p+='#'
            else:
                p+='.'
        print(p)
    # Part 2

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print()
    print("Day: ", day)
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()