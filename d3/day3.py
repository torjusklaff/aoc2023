import pathlib
from Tools.common import readlinesfromfile
filepath = pathlib.Path(__file__).parent.resolve()
import re

def do(input):
    total = 0
    totall = 0
    digits = '1234567890'
    rows = input

    coords = [
        [-1, 0],
        [-1, -1],
        [-1, 1],
        [1, 0],
        [1, 1],
        [1, -1],
        [0, -1],
        [0, 1],

    ]
    gear_locations = []
    for r in range(len(rows)):
        for c in range(len(rows[r])):
            if rows[r][c] == '*':
                gear_locations.append((r,c))
    gears = {str(gear): [] for gear in gear_locations}
    for r, row in enumerate(rows):
        
        nums = re.findall(r'\d+', row)

        for num in nums:
            l = len(num)
            ind = row.index(num)
            around = []
            for i in range(ind, ind + l):
                around += [[r+rn,i+cn] for [rn, cn] in coords]
            
            around = [[rn,cn] for [rn,cn] in around if rn > -1 and rn < len(rows) and cn > -1 and cn < (len(row)-1)]
            around = set(tuple(ar) for ar in around)
            for coor in around:
                if coor in gear_locations:
                    gears[str(coor)].append(num)
            for rn, cn in around:
                if rows[rn][cn] != '.' and rows[rn][cn] not in digits:
                    total += int(num)
                    break

            #stupid workaround to get index to work
            row = list(row)
            for s in range(ind,ind+l):
                row[s] = '.' 
            sr = ''
            for s in row:
                sr+=s
            row = sr
            
            totall += int(num)

    tot2 = 0
    for gear in gears.values():
        if len(gear) == 2:
            tot2+= int(gear[0])*int(gear[1])
    print(tot2)

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()