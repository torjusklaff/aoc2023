import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 16

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    beams = [(0,0, 'r')]
    dirs = {'r': (0,1), 'l': (0,-1), 'd':(1,0), 'u':(-1,0)}
    energized = {}
    mirrmap = input
    rmax = len(mirrmap)
    cmax = len(mirrmap[0])

    while beams:
        curr = beams.pop()
        while 1:
            r, c, d = curr
            if r < 0 or c < 0 or r == rmax or c == cmax:
                break 
            if (r,c) in energized.keys():
                if d in energized[(r,c)]:
                    break
                else:
                    energized[(r,c)].append(d)
            else:
                energized[(r,c)] = [d]
            
            point = mirrmap[r][c]

            nd = d
            if point == '|' and d in 'lr':
                if d == 'r' and 'l' in energized[(r,c)] or d == 'l' and 'r' in energized[(r,c)]:
                    break
                beams.append((r+dirs['u'][0], c+dirs['u'][1], 'u'))
                nd = 'd'
            elif point == '-' and d in 'ud':
                if d == 'u' and 'd' in energized[(r,c)] or d == 'd' and 'u' in energized[(r,c)]:
                    break
                beams.append((r+dirs['l'][0], c+dirs['l'][1], 'l'))
                nd = 'r'
            elif point == '/':
                if d == 'd': nd = 'l'
                elif d == 'u': nd = 'r'
                elif d == 'r': nd = 'u'
                else: nd = 'd'
            elif point == '\\':
                if d == 'd': nd = 'r'
                elif d == 'u': nd = 'l'
                elif d == 'r': nd = 'd'
                else: nd = 'u'
            
            curr = (r+dirs[nd][0],c+dirs[nd][1], nd)

        ans1 = len(energized.keys())

    # Part 2
    start_beams = [(0,0, 'r'),(0,0, 'd'),(0,cmax-1, 'l'),(0,cmax-1, 'd'),(rmax-1,0, 'r'),(rmax-1,0, 'u'),(rmax-1,cmax-1, 'l'),(rmax-1,cmax-1, 'u')]
    for r in range(1, rmax-1):
        start_beams.append((r,0,'r'))
        start_beams.append((r,cmax-1,'l'))
    for c in range(1, cmax-1):
        start_beams.append((0,c,'d'))
        start_beams.append((rmax-1,c,'u'))
    while start_beams:
        beams = [start_beams.pop()]
        
        energized = {}

        while beams:

            curr = beams.pop()
            while 1:
                r, c, d = curr
                if r < 0 or c < 0 or r == rmax or c == cmax:
                    break 
                if (r,c) in energized.keys():
                    if d in energized[(r,c)]:
                        break
                    else:
                        energized[(r,c)].append(d)
                else:
                    energized[(r,c)] = [d]
                
                point = mirrmap[r][c]

                nd = d
                if point == '|' and d in 'lr':
                    if d == 'r' and 'l' in energized[(r,c)] or d == 'l' and 'r' in energized[(r,c)]:
                        break
                    beams.append((r+dirs['u'][0], c+dirs['u'][1], 'u'))
                    nd = 'd'
                elif point == '-' and d in 'ud':
                    if d == 'u' and 'd' in energized[(r,c)] or d == 'd' and 'u' in energized[(r,c)]:
                        break
                    beams.append((r+dirs['l'][0], c+dirs['l'][1], 'l'))
                    nd = 'r'
                elif point == '/':
                    if d == 'd': nd = 'l'
                    elif d == 'u': nd = 'r'
                    elif d == 'r': nd = 'u'
                    else: nd = 'd'
                elif point == '\\':
                    if d == 'd': nd = 'r'
                    elif d == 'u': nd = 'l'
                    elif d == 'r': nd = 'd'
                    else: nd = 'u'
                
                curr = (r+dirs[nd][0],c+dirs[nd][1], nd)
        if len(energized.keys()) > ans2:
            ans2 = len(energized.keys())


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