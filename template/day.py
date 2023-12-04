import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()

def do(input):
    return

def main():
    print("Example: ")
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))

if __name__=="__main__":
    main()