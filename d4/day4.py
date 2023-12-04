import pathlib
from Tools.common import readlinesfromfile
filepath = pathlib.Path(__file__).parent.resolve()

import re
def do(input):
    total = 0
    num_cards = [1 for x in range(len(input))]
    for c, gcard in enumerate(input):
        win , own = gcard.split('|')

        ra, win = win.split(':') #stupid
        win = re.findall(r'\d+', win)
        own = re.findall(r'\d+', own)
        same = [x for x in own if x in win]
        if len(same) > 0:
            for x in range(c+1,c+1+len(same)):
                num_cards[x] += num_cards[c]
            total += 2**(len(same)-1)
    print("Part 1: ")
    print (total)
    print("Part 2: ")
    print(sum(num_cards))


def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()
