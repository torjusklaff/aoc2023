import pathlib
from Tools.common import readfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
from collections import defaultdict

day = 15

def do(input):
    code_start_time = time.time()
    input, *a = input.splitlines()

    ans1 = 0
    ans2 = 0

    # Part 1
    stri = input.split(',')
    for s in stri:
        tot = 0
        for a in s:
            tot += ord(a)
            tot *= 17
            tot = tot % 256
        ans1 += tot

    # Part 2
    boxes = defaultdict(int)
    for i in range(256):
        boxes[i] = []
    for s in stri:
        hash = 0
        b, *q =s.split('-')
        b, *q =b.split('=')
        for a in b:
            hash += ord(a)
            hash *= 17
            hash = hash % 256
        if '-' in s:
            code, *o = s.split('-')
            for p in boxes[hash]:
                if p[0] == code:
                    boxes[hash].remove(p)
                    break

        else:
            code, num = s.split('=')
            num = int(num)
            for ind, p in enumerate(boxes[hash]):
                if p[0] == code:
                    boxes[hash][ind] = (code,num)
                    break
            if (code, num) not in boxes[hash]:
                boxes[hash].append((code,num))
    for i in boxes.keys():
        for j, b in enumerate(boxes[i]):
            ans2 += (i+1)*(j+1)*b[1]
                
            



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
    do(readfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()