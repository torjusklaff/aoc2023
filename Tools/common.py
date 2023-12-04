import re
def readlinesfromfile(file):
    with open(file) as f:
        r = f.readlines()
    return r

def s_to_pos_list(s):
    return re.findall(r'\d+', s)
def s_to_int_list(s):
    return re.findall(r'-?\d+', s)
