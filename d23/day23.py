import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

dirs = { 'u':(-1,0), 'l': (0,-1), 'r': (0,1), 'd':(1,0)}

day = 23
yolo = True
hardy = []

from functools import cache

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0
    # Part 1
    if False:
        maze = tuple([tuple([c for c in r]) for r in input])
    else:
        maze = [[c for c in r] for r in input]
        for r, row in enumerate(maze):
            for c, col in enumerate(row):
                if col != '#':
                    maze[r][c] = '.'
        maze = tuple([tuple([c for c in r]) for r in maze])

    start = (0,1)
    rmax = len(maze)
    cmax = len(maze[0])

    # @cache
    # def bfs(prev, curr, longest):
    #     r,c = curr
    #     prev = list(set(prev))
    #     if maze[r][c] == '>':
    #         prev.append((r,c))
    #         curr = (r, c + 1)
    #     elif maze[r][c] == 'v':
    #         prev.append((r,c))
    #         curr = (r + 1, c)
    #     r,c = curr
    #     longest = max(longest,len(prev))
    #     nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
    #     for nb in nbs:
    #         rb, cb = nb
    #         if nb not in prev and rb >= 0 and rb < rmax and cb >= 0 and cb < cmax and maze[rb][cb] != '#':
    #             if (maze[rb][cb] == '>' and (cb-c) == 1) or (maze[rb][cb] == 'v' and (rb-r) == 1) or maze[rb][cb] == '.':
    #                 prev.append(curr)
    #                 longest = max(bfs(tuple(prev),nb,longest), longest)
        
    #     return longest
    
    # ans1 = bfs((),start,0)
    prev = [[0, [(start, 'd')]]]
    end = (rmax-1,cmax-2)
    longest = 0
    longest_route = []
    ds = 'ulrd'
    q = prev
    tree_dists = {}
    end_step = []
    while q:
        time_start = time.time()
        for ind, path in enumerate(q):
            p_steps = 0
            n_steps, crossroads = path
            curr, d = crossroads[-1]
            crs = [x[0] for x in crossroads]

            if end_step and curr == end_step[0][0]:
                d = end_step[0][1]

            if (curr, d) in tree_dists.keys():
                p_steps, curr = tree_dists[(curr,d)]
                pos = []
                if curr not in crs:
                    n_steps += p_steps
                    if curr != end:
                    
                        r,c = curr
                        nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
                        for dub, nb in enumerate(nbs):
                            rb, cb = nb
                            if nb != prev and rb >= 0 and rb < rmax and cb >= 0 and cb < cmax and maze[rb][cb] != '#':
                                if (maze[rb][cb] == '>' and (cb-c) == 1) or (maze[rb][cb] == 'v' and (rb-r) == 1) or maze[rb][cb] == '.':
                                    pos.append((ds[dub],nb))
                    
            else:
                r,c = curr
                r,c = (r+dirs[d][0], c + dirs[d][1])
                prev = curr
                curr = (r,c)
                nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
                n_steps += 1
                p_steps += 1
                pos = []
                for dub, nb in enumerate(nbs):
                    rb, cb = nb
                    if nb != prev and rb >= 0 and rb < rmax and cb >= 0 and cb < cmax and maze[rb][cb] != '#':
                        if (maze[rb][cb] == '>' and (cb-c) == 1) or (maze[rb][cb] == 'v' and (rb-r) == 1) or maze[rb][cb] == '.':
                            pos.append((ds[dub],nb))

                while len(pos) == 1:
                    prev = curr
                    nd, curr = pos[0]
                    rb, cb = curr
                    pos = []
                    n_steps += 1
                    p_steps += 1
                    nbs = [(rb+rd, cb+cd) for rd,cd in dirs.values()]
                    for dub, nb in enumerate(nbs):
                        rb, cb = nb
                        if nb != prev and rb >= 0 and rb < rmax and cb >= 0 and cb < cmax and maze[rb][cb] != '#' and nb not in crs:
                            if (maze[rb][cb] == '>' and (cb-c) == 1) or (maze[rb][cb] == 'v' and (rb-r) == 1) or maze[rb][cb] == '.':
                                pos.append((ds[dub],nb))

            if len(pos) == 0:
                line = q.pop(ind)
                if curr == end:
                    tree_dists[crossroads[-1]] = (p_steps, curr)
                    end_step = [crossroads[-1]]
                    if n_steps > ans2:
                        ans2 = n_steps
                        longest_route = line

            else:
                if crossroads[-1] not in tree_dists.keys():
                    tree_dists[crossroads[-1]] = (p_steps, curr)
                    
                if nd == 'u': pd = 'd'
                elif nd == 'd': pd = 'u' 
                elif nd == 'r': pd = 'l'
                else: pd = 'r'
                if (curr,pd) not in tree_dists.keys():
                    tree_dists[(curr,pd)] = (p_steps,crossroads[-1][0])

                crossroads.append((curr,pos[0][0]))
                q[ind] = [n_steps, crossroads]
                for p in pos[1:]:
                    cr = [a for a in crossroads[:-1]]
                    cr.append((curr,p[0]))
                    q.append([n_steps, cr])

        time_it = time.time()
        if time_it - time_start > 100:
            print(time_it-code_start_time)
            print(ans2)

                    




    # ans < 2111 ans 2 > 6138

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