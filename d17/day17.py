import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
from functools import cache
import time
import math

day = 17
dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    dirs = { 'u':(-1,0), 'l': (0,-1), 'r': (0,1), 'd':(1,0)}

    heat_loss_map = [[int(x) for x in r] for r in input]
    rmax = len(heat_loss_map)
    cmax = len(heat_loss_map[0])
    dist = [[math.inf for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]
    prev = [[() for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]
    dist[0][0] = 0
    end = (len(heat_loss_map)-1, len(heat_loss_map[0])-1)
    visited = set()
    import heapq
    q2 = []
    goal = (rmax-1,cmax-1)
    heapq.heappush(q2,(0,(0,0,'d','d')))
    heapq.heappush(q2,(0,(0,0,'r','r')))
    ndirs = {'d': ['l','r'],'r': ['d','u'],'l': ['d','u'],'u': ['l','r']}

    while q2:
        mindist, a = heapq.heappop(q2)

        r,c,pd,d = a
        if a in visited:
            continue

        visited.add(a)
        
        dr, dc = dirs[d]
        pr, pc = dirs[pd]
        rb, cb = r,c
        ndist = mindist
        if dist[r][c] >= mindist:
            dist[r][c] = mindist
            prev[r][c] = (rb-pr, cb-pc)

        if (r,c) == goal:
            break
        
        for i in range(3):
            rb += dr
            cb += dc
            if 0 <= rb < rmax and 0 <= cb < cmax:
                ndist += heat_loss_map[rb][cb]
                ndir = [s for s in ndirs[d]]
                for nd in ndir:
                    nex = (rb,cb,d,nd)
                    heapq.heappush(q2,(ndist,nex))
            else:
                break
                    

    ans1 = dist[rmax-1][cmax-1]
    start = (rmax-1,cmax-1)
    steps = [start]
    while start != (0,0):
        start = prev[start[0]][start[1]]
        steps.append(start)
    for r in range(rmax):
        p = ''
        for c in range(cmax):
            if (r,c) in steps:
                p+='#'
            else:
                p+='.'
        if False:
            print(p)

    # Part 2
    q2 = []
    heapq.heappush(q2,(0,(0,0,'d')))
    heapq.heappush(q2,(0,(0,0,'r')))
    visited = set()
    dist = [[math.inf for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]
    prev = [[() for c in range(len(heat_loss_map[0]))] for r in range(len(heat_loss_map))]

    while q2:
        mindist, a = heapq.heappop(q2)

        r,c,d = a
        if a in visited:
            continue

        visited.add(a)

        if dist[r][c] >= mindist:
            dist[r][c] = mindist

        if (r,c) == goal:
            break

        dr, dc = dirs[d]
        rb, cb = r,c
        ndist = mindist

        for i in range(10):
            rb += dr
            cb += dc
            if 0 <= rb < rmax and 0 <= cb < cmax:
                if i < 3:
                    if (rb,cb) == end:
                        break
                    ndir = []

                else:
                    ndir = [s for s in ndirs[d]]

                ndist += heat_loss_map[rb][cb]
                for nd in ndir:
                    nex = (rb,cb,nd)
                    heapq.heappush(q2,(ndist,nex))

            else:
                break


    ans2 = dist[rmax-1][cmax-1]

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