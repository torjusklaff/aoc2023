import pathlib
from Tools.common import readlinesfromfile, readfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    segments = input.split('\n\n')

    for seg in segments:

        

        rows = seg.splitlines()
        cols = [[rows[j][i] for j in range(len(rows))] for i in range(len(rows[0])) ]

        rfound = len(rows) + 1
        cfound = len(rows[0]) + 1

        found = False
        
        for i, r in enumerate(rows):
            if i > 0:
                prev = rows[i-1]
                if r == prev:
                    found = True
                    for j in range(1, min(i, len(rows)-i)):
                        up = rows[i - 1 - j]
                        down = rows[i + j]
                        if up != down:
                            found = False
                            break

                if found:
                    ans1 += 100*i 
                    rfound = i
                    break
                else:
                    found = False
        if not found:
            for i, r in enumerate(cols):
                if i > 0:
                    prev = cols[i-1]
                    if r == prev:
                        found = True
                        for j in range(1, min(i, len(cols)-i)):
                            up = cols[i - 1 - j]
                            down = cols[i + j]
                            if up != down:
                                found = False
                                break

                        if found:
                            ans1 += i
                            cfound = i
                            break

        # Part 2

        found = False
        desmudged = False
        for i, r in enumerate(rows):
            if i > 0:
                prev = rows[i-1]
                diff = 0
                for a in range(len(r)):
                    if diff > 1:
                        break
                    if r[a] != prev[a]:
                        diff += 1
                if diff == 1: 
                    desmudged = True
                if desmudged or r == prev:
                    found = True
                    for j in range(1, min(i, len(rows)-i)):
                        up = rows[i - 1 - j]
                        down = rows[i + j]
                        if up != down and desmudged:
                            desmudged = False
                            found = False
                            break
                        else:
                            diff = 0
                            for a in range(len(r)):
                                if diff > 1:
                                    break
                                if up[a] != down[a]:
                                    diff += 1
                            if diff == 1:
                                desmudged = True

                        
                if found and desmudged and i != rfound:
                    ans2 += i*100
                    break
                else:
                    found = False
                    desmudged = False

        if not desmudged:
            for i, r in enumerate(cols):
                if i > 0:
                    prev = cols[i-1]
                    diff = 0
                    for a in range(len(r)):
                        if diff > 1:
                            break
                        if r[a] != prev[a]:
                            diff += 1
                    if diff == 1: 
                        desmudged = True
                    if desmudged or r == prev:
                        found = True
                        for j in range(1, min(i, len(cols)-i)):
                            up = cols[i - 1 - j]
                            down = cols[i + j]
                            if up != down and desmudged:
                                desmudged = False
                                found = False
                                break
                            else:
                                diff = 0
                                for a in range(len(r)):
                                    if diff > 1:
                                        break
                                    if up[a] != down[a]:
                                        diff += 1
                                if diff == 1:
                                    desmudged = True

                    if found and desmudged and i != cfound:
                        ans2 += i
                        break
                    else:
                        found = False
                        desmudged = False
                

    code_end_time = time.time()
    print("Part 1: ")
    print(ans1)
    print("Part 2: ")
    print(ans2)
    print("Time: ", code_end_time - code_start_time)
    return

def main():
    print()
    print("Day: 13")
    print("Example: ")
    do(readfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()