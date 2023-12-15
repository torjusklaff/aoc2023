import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

from functools import cache
day = 12


@cache
def solve(parts, numbers, ans=0):
    if parts.count("#") + parts.count("?") < sum(numbers):
        return 0
    if parts[0] == '#':
        r = parts[:numbers[0]]
        if '.' in r:
            return 0
        else:
            if len(numbers) == 1:
                if len(r) >= numbers[0] and parts[numbers[0]:].count('#') == 0:
                    return 1
            elif parts[numbers[0]] != '#':
                ans += solve(parts=parts[numbers[0]+1:], numbers=numbers[1:], ans=ans)
            else:
                return 0
        
    elif parts[0] == '?':
        p1 = parts[1:]
        p2 = '#' + parts[1:]
        ans += solve(p1, numbers,ans) + solve(p2, numbers, ans)
    else:
        ans += solve(parts[1:], numbers, ans)      
    return ans

def do(input):
    code_start_time = time.time()
    
    ans1 = 0
    ans2 = 0

    # Part 1

    for line in input:
        parts, number = line.split()
        numbers = [int(x) for x in number.split(',')]
        numbers2 = numbers*5
        parts2 = "?".join([parts]*5)
        pattern = []
        ans1 += solve(parts, tuple(numbers))
        ans2 += solve(parts2, tuple(numbers2))

        if True: 
            continue

        # Fill in first? 
        for n in numbers:
            p = "#"*n
            pattern.append(p)
        
        pot = parts.count('?')
        missing = sum(numbers) - parts.count("#")

        all_possible = 2**pot - 2**(pot-missing) + 1

        i = 2**missing - 1
        nfirst = 0
        last_working = 0
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
                        first += '.'
                    j+=1
                else:
                    first += p
            
            series = [x for x in first.split(".") if x]
            if series == pattern:
                nfirst += 1
                if first[-1] == "#":
                    last_working += 1
            i += 1

    # Part 2
        if nfirst == last_working:
            ans2 += nfirst**5
        elif parts.endswith('.'):
            nparts = 0
            parts2 = '?' + parts
            pot = parts2.count('?')
            missing = sum(numbers) - parts2.count("#")

            all_possible = 2**pot - 2**(pot-missing) + 1

            i = 2**missing - 1
            while i < all_possible:
                first = ''
                j = 0
                test = bin(i)[::-1]
                if test.count('1') != missing:
                    i += 1
                    continue
                for p in parts2:
                    if p == "?":
                        if j < len(test) - 2 and test[j] == '1':
                            first += "#"
                        else:
                            first += '.'
                        j+=1
                    else:
                        first += p
                
                series = [x for x in first.split(".") if x]
                if series == pattern:
                    nparts += 1
                i += 1  
            ans2 += nfirst*nparts**4
        else:
            nparts = 0
            parts2 = parts + '?'
            pot = parts2.count('?')
            missing = sum(numbers) - parts2.count("#")

            all_possible = 2**pot - 2**(pot-missing) + 1

            i = 2**missing - 1
            while i < all_possible:
                first = ''
                j = 0
                test = bin(i)[::-1]
                if test.count('1') != missing:
                    i += 1
                    continue
                for p in parts2:
                    if p == "?":
                        if j < len(test) - 2 and test[j] == '1':
                            first += "#"
                        else:
                            first += '.'
                        j+=1
                    else:
                        first += p
                
                series = [x for x in first.split(".") if x]
                if series == pattern:
                    nparts += 1
                i += 1  
            ans2 += nfirst*nparts**4


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