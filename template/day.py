import pathlib
from Tools.common import readlinesfromfile
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