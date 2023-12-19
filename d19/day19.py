import pathlib
from Tools.common import readfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 19

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    x,m,s,a = 0,0,0,0
    # Part 1
    execs, values = input.split('\n\n')
    execs = execs.splitlines()
    values = values.splitlines()
    exes = {}
    for ex in execs:
        n, line = ex.strip('}').split('{')
        aops = {}
        ops = line.split(',')
        for o in ops[0:-1]:
            d,b = o.split(':')
            aops[d] = b
        aops['True'] = ops[-1]
        exes[n] = aops

    for value in values:
        v = value[1:-1]
        v = v.split(',')
        x,m,a,s = (int(x[2:]) for x in v)
            
        conf = exes['in']
        ind = 'in'
        while ind not in ('A','R'):
            conf = exes[ind]
            for op in conf.keys():
                if op == 'True':
                    ind = conf[op]
                    break

                var = op[0]
                opr = op[1]
                value = int(op[2:])
                if var == 'x':
                    var = x
                elif var == 'm':
                    var = m
                elif var == 's':
                    var = s
                else:
                    var = a
                if opr == '<':
                    ans = var<value
                else:
                    ans = var>value
                if ans:
                    ind = conf[op]
                    break
                    print('yay')
        if ind == 'A':
            ans1 += x + m + a + s
    # Part 2
    accepted = []
    ind = 'in'
    x = (1,4000)
    m = (1,4000)
    a = (1,4000)
    s = (1,4000)
    ranges = [(x,m,a,s, ind)]
    while ranges:
        x,m,a,s,ind = ranges.pop()
        while ind not in ('A','R'):
            conf = exes[ind]
            for op in conf.keys():
                if op == 'True':
                    ind = conf[op]
                    break
                var = op[0]
                opr = op[1]
                value = int(op[2:])
                if var == 'x':
                    c1,c2 = x
                elif var == 'm':
                    c1,c2 = m
                elif var == 's':
                    c1,c2 = s
                else:
                    c1,c2 = a
                if opr == '<':
                    if c2 < value:
                        ind = conf[op]
                        break
                    elif c1 >= value:
                        continue
                    else:
                        d1 = c1
                        d2 = value - 1
                        n1 = value
                        n2 = c2
                else:
                    if c1 > value:
                        ind = conf[op]
                        break
                    elif c2 <= value:
                        continue
                    else:
                        d1 = value + 1
                        d2 = c2
                        n1 = c1
                        n2 = value

                if var == 'x':
                    x = (d1,d2)
                    ranges.append(((n1,n2),m,a,s,ind))
                elif var == 'm':
                    m = (d1,d2)
                    ranges.append((x,(n1,n2),a,s,ind))
                elif var == 's':                    
                    s = (d1,d2)
                    ranges.append((x,m,a,(n1,n2),ind))
                else:
                    a = (d1,d2)
                    ranges.append((x,m,(n1,n2),s,ind))
                
                ind = conf[op]
                break


        if ind == 'A':
            accepted.append((x,m,a,s))
    for acc in accepted:
        ans = 1
        for a in acc:
            s, e = a
            ans *= e-s + 1
        ans2 += ans




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
    do(readfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()