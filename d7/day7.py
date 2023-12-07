import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time
import copy
def do(input):
    code_start_time = time.time()

    ans1 = 0
    ans2 = 0

    # Part 1
    classes = {}
    card_types = "23456789TJQKA"
    ranks = ["high", "pair", "tpair", "three", "house", "four", "five"]
    for line in input:
        card, bet = line.split()
        if len(set(card)) == 5:
            key = "high"
        elif len(set(card)) == 4:
            key = "pair"
        elif len(set(card)) == 3:
            for a in card:
                if card.count(a) == 2:
                    key = "tpair"
                    break
                elif card.count(a) == 3:
                    key = "three"
                    break
        elif len(set(card)) == 1:
            key = "five"
        elif len(set(card)) == 2:
            key = "house"
            for a in card:
                if card.count(a) == 4:
                    key = "four"
                    break
        if key not in classes.keys():
            classes[key] = [(card, int(bet))]
        else:
            classes[key].append((card, int(bet)))

    rate = 1
    for rank in ranks:
        if rank in classes.keys():
            rcards = copy.deepcopy(classes[rank])

            for n in range(1, len(rcards)):
                s = copy.deepcopy(rcards[n])
                for m in range(n-1, -1, -1):
                    c = copy.deepcopy(rcards[m])
                    for i in range(5):
                        if card_types.index(s[0][i]) < card_types.index(c[0][i]):
                            rcards[m + 1] = c
                            rcards[m] = s
                            break
                        elif card_types.index(s[0][i]) > card_types.index(c[0][i]):
                            break
                        
            for c, b in rcards:
                ans1 += b*rate
                rate += 1




    # Part 2
    card_types = "J23456789TQKA"
    classes = {}
    ranks = ["high", "pair", "tpair", "three", "house", "four", "five"]
    for line in input:
        card, bet = line.split()
        if len(set(card)) == 5:
            key = "high"
            if "J" in card:
                key = "pair"
        elif len(set(card)) == 4:
            key = "pair"
            if "J" in card:
                key = "three"
        elif len(set(card)) == 3:
            for a in card:
                if card.count(a) == 3:
                    if "J" in card:
                        key = "four"
                    else:
                        key = "three"
                    break
                
                if card.count(a) == 2:
                    if "J" in card:
                        if card.count("J") == 1:
                            key = "house"
                        else:
                            key = "four"
                    else:
                        key = "tpair"
                    break

        elif len(set(card)) == 1:
            key = "five"
        elif len(set(card)) == 2:
            key = "house"
            for a in card:
                if card.count(a) == 4:
                    key = "four"
                    break
            if "J" in card:
                key = "five"
        if key not in classes.keys():
            classes[key] = [(card, int(bet))]
        else:
            classes[key].append((card, int(bet)))

    rate = 1
    for rank in ranks:
        if rank in classes.keys():
            rcards = copy.deepcopy(classes[rank])

            # Stupid ass insertion sort, oh well
            for n in range(1, len(rcards)):
                s = copy.deepcopy(rcards[n])
                for m in range(n-1, -1, -1):
                    c = copy.deepcopy(rcards[m])
                    for i in range(5):
                        if card_types.index(s[0][i]) < card_types.index(c[0][i]):
                            rcards[m + 1] = c
                            rcards[m] = s
                            break
                        elif card_types.index(s[0][i]) > card_types.index(c[0][i]):
                            break
                        
            for c, b in rcards:
                ans2 += b*rate
                rate += 1




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