import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
from itertools import permutations

def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1

    for line in input:
        parts, number = line.split()
        numbers = [int(x) for x in number.split(',')]
        numbers2 = numbers*5
        parts2 = "?".join(parts*5) # parts + "?" + parts + "?" + parts + "?" + parts + "?" + parts 
        pattern = []
        # Fill in first? 
        for n in numbers:
            p = "#"*n
            pattern.append(p)

        # 16384 = 2^14
        pot = parts.count('?')
        missing = sum(numbers) - parts.count("#")

        all_possible = 2**pot - 2**(pot-missing) + 1

        i = 2**missing - 1
        while i < all_possible:
            first = ''
            j = 0
            test = bin(i)[::-1]
            if test.count('1') != missing:
                i += 1
                continue
            for p in parts:
                if p == "?":
                    if j < len(test) - 2 and test[j] == '1':
                        first += "#"
                    else:
                        first += ''
                    j+=1
                else:
                    first += p
            
            series = [x for x in first.split(".") if x]
            if series == pattern:
                ans1 += 1

            i += 1



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
    print("Day: 12")
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()