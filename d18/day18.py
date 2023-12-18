import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 18

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    dirs = {'R': (0,1), 'L': (0,-1), 'D':(1,0), 'U':(-1,0)}
    trace = [(0,0, '(#000000)')]
    curr = (0,0)
    j = 0
    for line in input:
            
        d, l, color = line.split()
        r, c = curr
        if j == 1:
            j = 4
            if d == 'U':
                first_inside = (curr[0]+1, curr[1]-1)
            else:
                first_inside = (curr[0]+1, curr[1]-1)

        elif j == 0:
            j += 1
        for i in range(int(l)):
            trace.append((r + dirs[d][0] * (i+1), c + dirs[d][1] * (i+1), color))
        
        r += dirs[d][0] * (i+1)
        c += dirs[d][1] * (i+1)
        curr = (r,c)

        
    rs = [x[0] for x in trace]
    cs = [x[1] for x in trace]
    coords = list(zip(rs,cs))
    minr, maxr = min(rs), max(rs)
    minc, maxc = min(cs), max(cs)
    ans1 += len(set(coords))
    arr = [[0 for i in range(minc,maxc+1)] for j in range(minr,maxr+1)]
    first_inside = (first_inside[0]-minr, first_inside[1]-minc)
    for coord in coords:
        r,c = coord
        arr[r-minr][c-minc] = 1

    fillers = [first_inside]
    while fillers:
        fill = fillers.pop()
        r,c = fill
        nbs = [(r+rd, c+cd) for rd,cd in dirs.values()]
        for nb in nbs:
            if arr[nb[0]][nb[1]] == 0:
                fillers.append(nb)
        if arr[r][c] == 0:
            ans1 += 1
            arr[r][c] = 1

    # Part 2

    curr = (0,0)
    j = 0
    dirs2 = 'RDLU'
    corners = [(0,0)]
    for line in input:
            
        d, l, color = line.split()
        r, c = curr
        l = color[2:len(color)-2]
        l = int(l, 16)
        d = color[-2]
        d = dirs2[int(d)]
        r += dirs[d][0] * l
        c += dirs[d][1] * l
        curr = (r,c)
        corners.append((r,c))
        
    ans2 = 0
    for i, point in enumerate(corners):
        x1 = point[1]
        y1 = point[0]
        if i == len(corners)-1: 
            x2 = corners[0][1]
            y2 = corners[0][0]
        else:
            x2 = corners[i+1][1]
            y2 = corners[i+1][0]
        ans2 += abs(x2-x1) + abs(y2-y1)
        ans2 += (x1 * y2 - x2 * y1)
    ans2 = ans2/2
    ans2 += 1

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