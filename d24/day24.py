import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
from collections import defaultdict
import sympy
day = 24

def do(input, ex):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    if ex:
        low, high = (7,27)
    else:
        low, high = (200000000000000,400000000000000)

    hail_trajectories = defaultdict(int)
    i = 0
    for line in input:
        pos, der = line.split('@')
        pos = [int(x) for x in pos.split(', ')]
        der = [int(x) for x in der.split(', ')]
        hail_trajectories[i] = (pos,der)
        i += 1

    endpoints = defaultdict(int)
    for ind, info in hail_trajectories.items():
        pos, der = info
        x0,y0,z0 = pos
        dx,dy,dz = der
        s_to_start = 0
        if x0 >= low and x0 <= high:  
            if y0 < low:
                s_to_start = (low-y0)/dy
            elif y0 > high:
                s_to_start = (high-y0)/dy
        elif x0 < low:
            s_to_start = (low-x0)/dx
        else:
            s_to_start = (high-x0)/dx
        start = (x0+s_to_start*dx,y0+s_to_start*dy)
        x_start, y_start = start
        if dx < 0:
            if dy < 0:
                stex = (low-x_start)/dx
                stey = (low-y_start)/dy
            else:
                stex = (low-x_start)/dx
                stey = (high-y_start)/dy
        else:
            if dy < 0:
                stex = (high-x_start)/dx
                stey = (low-y_start)/dy
            else:
                stex = (high-x_start)/dx
                stey = (high-y_start)/dy
        x1 = x_start + min(stex,stey)*dx
        y1 = y_start + min(stex,stey)*dy
        end = (x1,y1)


        endpoints[ind] = [start,end]

                

    for ind, info in endpoints.items():
        start1, end1 = info
        dx1 = end1[0] - start1[0]
        dy1 = end1[1] - start1[1]
        line1 = (start1,end1)

        for i in range(ind+1,len(endpoints)):
            inf2 = endpoints[i]
            start2, end2 = inf2
            dx2 = end2[0] - start2[0]
            dy2 = end2[1] - start2[1]
            line2 = (start2,end2)
            xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
            ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

            def det(a, b):
                return a[0] * b[1] - a[1] * b[0]

            div = det(xdiff, ydiff)
            if div == 0:
                continue
            else:
                d = (det(*line1), det(*line2))
                x = det(d, xdiff) / div
                y = det(d, ydiff) / div
                xmin1 = min(start1[0],end1[0])
                xmin2 = min(start2[0],end2[0])
                xmax1 = max(start1[0],end1[0])
                xmax2 = max(start2[0],end2[0])
                ymin1 = min(start1[1],end1[1])
                ymin2 = min(start2[1],end2[1])
                ymax1 = max(start1[1],end1[1])
                ymax2 = max(start2[1],end2[1])
                if x >= low and x <= high and y >= low and y <= high and x >= xmin1 and x <= xmax1 and y>=ymin1 and y<=ymax1 and x >= xmin2 and x <= xmax2 and y>=ymin2 and y<=ymax2:
                    ans1 += 1

        
                    



    # Part 2
    # Is this just math?
    ans2 = 0
    # 300 hailstones, need at least 300 datapoints
    # Wtf math, at least integer collisions? Line intersection with x lines??
    h0 = hail_trajectories[0]
    h1 = hail_trajectories[1]
    h2 = hail_trajectories[2]
    c0, d0 = h0
    c1, d1 = h1
    c2, d2 = h2
    x0, y0, z0 = c0
    dx0, dy0, dz0 = d0
    x1, y1, z1 = c1
    dx1, dy1, dz1 = d1
    x2, y2, z2 = c2
    dx2, dy2, dz2 = d2
    x, y, z, dx, dy, dz = sympy.symbols('x y z dx dy dz')
    sympy.init_printing()
    ans = sympy.linsolve([x*(dy0-dy1) + y*(dx1-dx0) + dx*(y1-y0) + dy*(x0-x1) - dy0*x0 + dx0*y0 + dy1*x1 - dx1*y1, \
                x*(dz0-dz1) + z*(dx1-dx0) + dx*(z1-z0) + dz*(x0-x1) - dz0*x0 + dx0*z0 + dz1*x1 - dx1*z1, \
                y*(dz0-dz1) + z*(dy1-dy0) + dy*(z1-z0) + dz*(y0-y1) - dz0*y0 + dy0*z0 + dz1*y1 - dy1*z1, \
                x*(dy1-dy2) + y*(dx2-dx1) + dx*(y2-y1) + dy*(x1-x2) - dy1*x1 + dx1*y1 + dy2*x2 - dx2*y2, \
                x*(dz1-dz2) + z*(dx2-dx1) + dx*(z2-z1) + dz*(x1-x2) - dz1*x1 + dx1*z1 + dz2*x2 - dx2*z2, \
                y*(dz1-dz2) + z*(dy2-dy1) + dy*(z2-z1) + dz*(y1-y2) - dz1*y1 + dy1*z1 + dz2*y2 - dy2*z2], (x, y, z, dx, dy, dz))
    for i in range(3):
        ans2 += ans.args[0][i]


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
    do(readlinesfromfile(str(filepath)+"/example.txt"), True)
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"), False)
    print()

if __name__=="__main__":
    main()