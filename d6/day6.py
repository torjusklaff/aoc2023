import pathlib
from math import sqrt, ceil, floor
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

def do(input):
    code_start_time = time.time()

    timers = input[0]
    dist = input[1]

    times = s_to_pos_list(timers)
    times1 = [int(x) for x in times]
    dis = s_to_pos_list(dist)
    dis1 = [int(x) for x in dis]

    ans1 = 1
    for i, x in enumerate(times1):
        wins = 0
        for s in range(x+1):
            if s*(x-s) > dis1[i]:
                wins += 1
        ans1 *= wins
        



    times2 = ''
    for x in times: times2 += x
    times2 = int(times2)
    
    dis2 = ''
    for x in dis: dis2 += x
    dis2 = int(dis2)

    wins = 0

    s1 = times2/2 + sqrt(times2**2 - 4*dis2) / 2
    s2 = times2/2 - sqrt(times2**2 - 4*dis2) / 2
    
    ans2 = floor(max(s1,s2)) - ceil(min(s1, s2)) + 1


    # Got my answer with this

    # for s in range(times2 + 1):
    #     if s*(times2-s) > dis2:
    #         wins += 1

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()