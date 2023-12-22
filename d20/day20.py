import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 20
class BroadCaster:
    dest = ()
    op = None
    on = None
    mem = None
    changed = False


def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    modules = {}
    cons = []
    for line in input:
        mod, dest = line.split(' -> ')
        dest = dest.split(', ')
        broad = BroadCaster()
        broad.dest=tuple(dest)
        if mod[0] == '%':
            broad.op = '%'
            broad.on = 'off'
            modules[mod[1:]] = broad
        elif mod[0] == '&':
            broad.op = '&'
            modules[mod[1:]] = broad
            cons.append(mod[1:])
        else:
            modules[mod] = broad

    for key in modules.keys():
        for m, bro in modules.items():
            if key in bro.dest:
                if modules[key].mem is None:
                    modules[key].mem = {}

                modules[key].mem[m] = 0

    low_sigs = 0
    high_sigs = 0
    found_index = [0,0,0,0]
    for p in range(1,9000):
        queue = [[('button','broadcaster', 0)]]
        low_sigs += 1
        if ans2 != 0:
            break
        while queue:
            received = queue.pop(0)
            for rec in received:
                s, d, sig = rec
                if d == 'output' or d == 'rx':
                    if sig == 0:
                        ans2 = p+1
                        break
                    continue
                mod = modules[d]
                ns = None
                if mod.op == '%':
                    if sig == 0:
                        mod.changed = True

                        if mod.on == 'off':
                            ns = 1
                            mod.on = 'on'
                        else:
                            ns = 0
                            mod.on = 'off'
                elif mod.op == '&':
                    mod.mem[s] = sig
                    mod.changed = True
                    if all(mod.mem.values()):

                        ns = 0
                    else:
                        ns = 1
                else:
                    ns = 0
                if ns is not None:
                    nsend = []
                    for nd in mod.dest:
                        nsend.append((d,nd,ns))
                        if ns == 0:
                            low_sigs += 1
                        elif ns == 1:
                            high_sigs += 1
                            if d == 'rr':
                                found_index[0] = p
                            elif d == 'zb':
                                found_index[1] = p
                            elif d == 'js':
                                found_index[2] = p
                            elif d == 'bs':
                                found_index[3] = p
                    queue.append(nsend)


    ans1 = low_sigs*high_sigs
    # Part 2
    for m in modules.values():
        if m.changed:
            if m.op == '%':
                m.on = 'off'
            elif m.op == '&':
                for s in m.mem.keys():
                    m.mem[s] = 0

    ops = {}
    steps = []
    for m, b in modules.items():
        if 'rx' in b.dest:
            steps.append(m)
            break

    while steps:
        step = steps.pop(0)
        b = modules[step]
        op = []
        if step != 'broadcaster' and step not in ops.keys():
            for s in b.mem.keys():
                steps.append(s)
                op.append(s)
            ops[step] = tuple(op)
    import math
    ans2 = math.lcm(*found_index)

    # 2**34 too low 17179869184 11752068000 225639705600000 225872806380073


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
    do(readlinesfromfile(str(filepath)+"/example.txt"))
    print()
    print("Input: ")
    do(readlinesfromfile(str(filepath)+"/input.txt"))
    print()

if __name__=="__main__":
    main()