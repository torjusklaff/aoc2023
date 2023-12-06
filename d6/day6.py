import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()

def do(input):
    import time as tim
    st = tim.time()

    time = input[0]
    dist = input[1]
    times = s_to_pos_list(time)
    times2 = ''
    for x in times: times2 += x
    times2 = int(times2)
    times = [int(x) for x in times]

    dis = s_to_pos_list(dist)
    dis2 = ''
    for x in dis: dis2 += x
    dis2 = int(dis2)
    dis = [int(x) for x in dis]
    total = 1
    for i, x in enumerate(times):
        wins = 0
        for s in range(x+1):
            if s*(x-s) > dis[i]:
                wins += 1
        total *= wins
    print(total)
    wins = 0

    for s in range(times2 + 1):
        if s*(times2-s) > dis2:
            wins += 1
    print(tim.time() - st)
    print(wins)

    return

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()