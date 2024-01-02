import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
from collections import defaultdict
import heapq

day = 22

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    bricks = defaultdict()
    for i, line in enumerate(input):
        start, end = line.split('~')
        start = tuple([int(x) for x in start.split(',')])
        end = tuple([int(x) for x in end.split(',')])
        if start == end:
            bricks[i] = [start]
        else:
            w = abs(start[0]-end[0]) + 1
            b = abs(start[1]-end[1]) + 1

            if w > 1:
                xmin = min(start[0],end[0])
                xmax = max(start[0],end[0])
                l = []
                for x in range(xmin,xmax+1):
                    l.append((x,start[1],start[2]))
                bricks[i] = l
            elif b > 1:
                ymin = min(start[1],end[1])
                ymax = max(start[1],end[1])
                l = []
                for y in range(ymin,ymax+1):
                    l.append((start[0],y,start[2]))
                bricks[i] = l
            else:
                zmin = min(start[2],end[2])
                zmax = max(start[2],end[2])
                l = []
                for z in range(zmin,zmax+1):
                    l.append((start[0],start[1],z))
                bricks[i] = l

    bricks2 = [(i,brick) for i, brick in bricks.items()]
    r = sorted(bricks2, key=lambda value: value[1][0][2])
    filled_coords = set()
    filled_is = []
    while r:
        curr = r.pop(0)
        ind, brick = curr
        stopped = False
        while not stopped:
            n_brick = [(x,y,z-1) for x,y,z in brick]
            for b in n_brick:
                if b in filled_coords or b[2] == 0:
                    stopped = True
                    break
            if not stopped:
                brick = n_brick
        for b in brick:
            filled_coords.add(b)
        filled_is.append(ind)
        bricks[ind] = brick
    brick_supports = defaultdict(int)
    brick_supported_by = defaultdict(int)
    for i in filled_is:
        brick = bricks[i]
        above = [(x,y,z+1) for x,y,z in brick]
        below = [(x,y,z-1) for x,y,z in brick]
        supports = []
        supported = []
        for a in above:
            if a in filled_coords and a not in brick:
                supports.append(a)
        for b in below:
            if b in filled_coords and b not in brick:
                supported.append(b)
        supports_is = set()
        supported_by_is = set()
        for j, br in bricks.items():
            if not supports and not supported:
                break
            for a in supports:
                if a in br:
                    supports_is.add(j)
                    supports.remove(a)

            for b in supported:
                if b in br:
                    supported_by_is.add(j)
                    supported.remove(b)
        brick_supports[i] = supports_is
        brick_supported_by[i] = supported_by_is
        
    must_keep = set()
    for i, sup in brick_supported_by.items():
        if sup and len(sup) == 1:
            for s in sup:
                must_keep.add(s)

    ans1 = len(bricks) - len(must_keep)
            
    # Part 2
    for i in must_keep:
        q = [brick_supports[i]]
        a = set()
        a.add(i)
        while q:
            supp = q.pop(0)
            if supp:
                for s in supp:
                    crumble = True
                    for b in brick_supported_by[s]:
                        if b not in a:
                            crumble = False
                            break
                    if crumble:
                        a.add(s)
                        q.append(brick_supports[s])
        ans2 += len(a) - 1
    

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