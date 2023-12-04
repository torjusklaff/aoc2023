import pathlib
from Tools.common import readlinesfromfile
filepath = pathlib.Path(__file__).parent.resolve()

def do(input):    
    nred = 12
    nblue = 14
    ngreen = 13

    total = 0
    for line in input:
        game, rest = line.split(':')
        e, num = game.split()
        num = int(num)
        # total += num
        games = rest.split(';')
        max_red = 0
        max_blue = 0
        max_green = 0
        for game in games:
            game.strip()
            col = game.split(',')
            breaks = False
            for color in col:
                ncol, colo = color.split()
                ncol = int(ncol)
                if colo == 'red' and ncol > max_red:
                    max_red = ncol
                elif colo == 'green' and ncol > max_green:
                    max_green = ncol
                elif colo == 'blue' and ncol > max_blue:
                    max_blue = ncol

            #     if colo == 'red' and ncol > 12 or colo == 'blue' and ncol > 14 or colo =='green' and ncol > 13:
            #         breaks = True
            #         break
            # if breaks:
            #     total -= num
            #     break
        total += max_red * max_green * max_blue

    print(total)
    return

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()