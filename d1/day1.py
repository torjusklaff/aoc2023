import pathlib
from Tools.common import readlinesfromfile
filepath = pathlib.Path(__file__).parent.resolve()

def do(input):
    lines = input
    
    total = 0
    total2 = 0
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    nums_2 = {'oneight':'18','nineight':'98','fiveight':'58','threeight':'38','fiveight':'58','twone':'21','sevenine':'79', 'eightwo':'82', 'eighthree':'83', 'eight':'8', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'nine':'9','seven':'7' }



    for line in lines:
    
        for key in nums_2.keys():
            if key in line:
                line = line.replace(key, nums_2[key])

        for c in line:
            if c in nums:
                first = c
                break
        for l in line[::-1]:
            if l in nums:
                last = l
                break
        n = first + last
        total += int(n)
    print(total)
    return

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()