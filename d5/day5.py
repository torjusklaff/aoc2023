import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list, readfile
filepath = pathlib.Path(__file__).parent.resolve()
import sys

def do(input):
    sections = input.split('\n\n')
    seeds = sections[0]
    s, num = seeds.split(':')
    seeds = [int(x) for x in num.split()]
    seeds_2 = []
    stepsecs = {}
    locs = []
    highest = 0
    for sec in sections[1::]:
        sec = sec.splitlines()
        maps = sec[1::]
        stepsecs[sec[0]] = [] 
        for line in maps:
            l = [int(x) for x in line.split()]
            stepsecs[sec[0]].append(l)
    
    print("Part 1")
    for seed in seeds:
        line = seed
        for step in stepsecs.keys():
            for m in stepsecs[step]:
                if line >= m[1] and line < m[1] + m[2]:
                    line = line - m[1] + m[0]
                    break 
        locs.append(line)
    
    print(min(locs))
    import time
    now = time.time()
    print("Part 2 the right way")
    seeds = [(seed, seed + seeds[seeds.index(seed) + 1] ) for seed in seeds[::2]]
    ranges = []
    lowest = max(locs)
    for seed in seeds:
        ranges = []
        s, e = seed
        x = (s,e)
        ranges.append(x)
        for step in stepsecs.keys():
            new_ranges = []
            for r in ranges:
                matched_ranges = []
                for m in stepsecs[step]:
                    curr, prev, ran = m
                    y = (prev, prev + ran)
                    z = (max(r[0], y[0]), min(r[1], y[1]))
                    if z[1] > z[0]:
                        #we have intersection
                        new_ranges.append((z[0] - prev + curr,z[1] - prev + curr))
                        matched_ranges.append((z[0], z[1]))
                
                if len(matched_ranges) == 0:
                    new_ranges.append(r)

                # elif sum([len(m) for m in matched_ranges]) < len(r):
                #     for z in matched_ranges:
                #         if z[0] > r[0]:
                #             new_ranges.append((r[0], z[0]))
                #         if z[-1] < r[1]:
                #             new_ranges.append(range(z[-1] + 1, r[-1] + 1))

            ranges = new_ranges
        for ra in ranges:
            if ra[0] < lowest:
                lowest = ra[0]

    print(time.time() - now)
    print(lowest)

    # 0 = 3151478994

    # try mapping bottom up
    # Yeah this was extremely stupid but it worked in the end, leave it for posterity
    # print("Part 2")
    # seeds = [(seed, seed + seeds[seeds.index(seed)+1]) for seed in seeds[::2]]
    # r = [key for key in stepsecs.keys()]
    # found = False
    # loc = 0
    # index = 0 # substituted answer from task 1
    # while not found:
    #     loc = index
    #     for l in r[::-1]:
    #         for m in stepsecs[l]:

    #             if loc >= m[0] and loc < m[0] + m[2]:
    #                 loc = loc - m[0] + m[1]
    #                 s = s 
    #                 break
    #     for start, end in seeds:
    #         if loc in range(start, end):
    #             found = True
    #     if not found:
    #         index += 1
    # print(index)
    # return

def main():
    print("Example: ")
    do(readfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()