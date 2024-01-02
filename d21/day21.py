import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
from functools import cache

from collections import defaultdict

dirs = { 'u':(-1,0), 'l': (0,-1), 'r': (0,1), 'd':(1,0)}

# @cache
# def get_locs(steps_left, steps, garden, locs):
#     if steps_left == 0:
#         return len(locs)
#     steps_left -= 1
#     for loc in locs:
#         r,c = loc
#         nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
#         nlocs = set()
#         for nb in nbs:
#             rb,cb = nb
#             if rb >= 0 and rb < len(garden) and cb >= 0 and cb < len(garden[0]) and garden[rb%len(garden)][cb%len(garden[0])] != '#':
#                 nlocs.add((rb,cb))
#         steps += get_locs(steps_left, steps, garden, tuple(nlocs))
    
#     return steps

day = 21

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    garden = [[x for x in r] for r in input]
    found = False
    for r, row in enumerate(garden):
        if found:
            break
        for c, col in enumerate(row):
            if col == 'S':
                start = (r,c)
                found = True
                break

    visited = [[False for c in r] for r in garden]
    visited[r][c] = True
    rmax = len(visited)
    cmax = len(visited[0])
    q = set([start])
    for steps in range(64):
        nq = set()
        for s in q:
            r,c = s

            nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
            for nb in nbs:
                rb,cb = nb
                if rb >= 0 and rb < rmax and cb >= 0 and cb < cmax and garden[rb][cb] != '#':
                    nq.add((rb,cb))
            
        q = nq
    ans1 = len(q)
    # Part 2

    garden = tuple([tuple(g) for g in garden])
    vis = {}
    for r, row in enumerate(garden):
        for c, col in enumerate(row):
            nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
            locked = all([garden[r%rmax][c%cmax] == '#' for (r,c) in nbs])
            if col in '.S' and not locked:
                vis[(r,c)] = set()
    
    starts = [start,(0,cmax//2),(rmax-1,cmax//2),(rmax//2,0),(rmax//2,cmax-1), (0,0), (0,cmax-1),(rmax-1,0), (rmax-1,cmax-1)]
    filled_per_step_per_start = {start: defaultdict(int) for start in starts}
    q = set([start])
    filled_per_step = defaultdict(int)
    step = 1
    for step in range(1,start[0]+rmax*2+2):
        nq = set()
        for s in q:
            r,c = s

            nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
            for nb in nbs:
                rb,cb = nb
                if garden[rb%rmax][cb%cmax] != '#':
                    nq.add((rb,cb))


        q = nq
        filled_per_step[step] = len(q)
        if step in (start[0], start[0]+rmax, start[0]+rmax*2):
            print(step, len(q)) 

        if len(filled_per_step) >= 3 and filled_per_step[step] == filled_per_step[step-2]:
            break
    for s in range(step+1):
        filled_per_step_per_start[start][s] = filled_per_step[s]
    

    

            # nq = set()
            # for s in q:
            #     r,c = s

            #     nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
            #     for nb in nbs:
            #         rb,cb = nb
            #         if garden[rb%rmax][cb%cmax] != '#':
            #             nq.add((rb,cb))

            #             vis[(rb%rmax, cb%cmax)].add((rb//rmax,cb//cmax))
            # qs.append(nq) 
            # q = nq
    a1,b1,c1 = start[0]**2,start[0],-filled_per_step[start[0]]
    a2,b2,c2 = (start[0]+rmax)**2,start[0]+rmax,-filled_per_step[start[0]+rmax]
    a3,b3,c3 = (start[0]+2*rmax)**2,start[0]+2*rmax,-filled_per_step[start[0]+2*rmax]
    a4,b4 = 26501365**2,26501365 
    import sympy
    a,b,c,an2 = sympy.symbols('a b c an2')
    ans = sympy.linsolve([a*a1 + b*b1 + c + c1, \
                a*a2 + b*b2 + c + c2, \
                a*a3 + b*b3 + c + c3, \
                a*a4 + b*b4 + c + an2], (a,b,c,an2))
    for i in ans:
        print(i)

    cyc_its = (26501365-rmax//2)/rmax
    # corners: 958, 947, 951, 961       980, 981, 982, 990
    # edge: 5766, 5759, 5752, 5773
    # center: 7483, 7541
    num_filled = cyc_its*4 + 4*sum(range(int(cyc_its))) + 1
    # ans2 = num_filled*(filled_per_step[len(filled_per_step)-1]+filled_per_step[len(filled_per_step)-2])/2
    while False:
        steps_to_fill = steps
        vis2 = {}
        for co in q:
            r,c = co
            if (r//rmax,c//cmax) not in vis2.keys():
                vis2[(r//rmax,c//cmax)] = 1
            else: 
                vis2[(r//rmax,c//cmax)] += 1

        out = 0
        for v in vis.values():
            for val in v:
                if val != (0,0):
                    out += 1
        sxsxs = sorted([x for x in vis2.keys()])
        max_steps = 26501365
        steps_left = max_steps - steps_to_fill
        cyc_len = steps_to_fill
        cyc_its = steps_left//cyc_len
        steps += cyc_len*cyc_its
        n_steps_left = max_steps - steps
        full_blocks = cyc_its * 2 + sum(range(cyc_its)) * 2
            #       ft           fb              fl              fr     
        starts = [(0,cmax//2),(rmax-1,cmax//2),(rmax//2,0),(rmax//2,cmax-1)]
        queues = [[starts[0],starts[2]],[starts[0],starts[3]],[starts[1],starts[2]], [starts[1],starts[3]], [starts[0]],[starts[1]],[starts[2]],[starts[3]]]
        steps_per_start = []
        for q in queues:
            for steps in range(n_steps_left+steps_to_fill//2):
                nq = set()
                for s in q:
                    r,c = s

                    nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
                    for nb in nbs:
                        rb,cb = nb
                        if rb >= 0 and rb < rmax and cb >= 0 and cb < cmax and garden[rb][cb] != '#':
                            nq.add((rb,cb))
                    
                q = nq
            steps_per_start.append(len(q))
        # 778064728020200 too high 614863076637600 too low, not 614864596322712
        ans2 = full_blocks*len(vis)
        half_blocks = 2*(cyc_its+1) - 4
        halfblocks2 = (cyc_its + 1)*2 + 2*sum(range(cyc_its+1)) - full_blocks - 4
        ans2 += sum(steps_per_start[4:]) + sum(steps_per_start[:4]) * half_blocks
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