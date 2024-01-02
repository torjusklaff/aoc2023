import pathlib
from Tools.common import readlinesfromfile, s_to_pos_list, s_to_int_list
filepath = pathlib.Path(__file__).parent.resolve()
import time

day = 25

def do(input):
    code_start_time = time.time()


    ans1 = 0
    ans2 = 0

    # Part 1
    connections = {}
    edges = set()
    vertices = set()
    for line in input:
        ind, conns = line.split(':')
        conns = conns.split()
        vertices.add(ind)
        for conn in conns:
            vertices.add(conn)
            if (conn, ind) not in edges:
                edges.add((ind,conn))
        connections[ind] = set(conns)
    
    import random
    edges_worker = []
    singles = True
    while len(edges_worker) == 0 or len(edges_worker) > 3:
        edges_worker = list(edges)
        vertices_worker = set()
        for v in vertices:
            vertices_worker.add(v)
        singles = True

        while len(vertices_worker) > 2:
            ind = -1
            if len(edges_worker) > 1:
                if singles:
                    for i in range(len(edges_worker)):
                        ind = random.randint(0, len(edges_worker)-1)

                        if len(edges_worker[ind][0]) == 3 or len(edges_worker[ind][1]) == 3:
                            
                            break
                    if i == len(edges_worker)-1:
                        singles = False
                        ind = random.randint(0, len(edges_worker)-1)

                else:
                    ind = random.randint(0, len(edges_worker)-1)
                
            elif len(edges_worker) == 1:
                ind = 0
            else:
                break
            a,b = edges_worker.pop(ind)
            new_edges = []
            for i, e in enumerate(edges_worker):
                c,d = e
                if c == a or c == b:
                    c = a + b
                if d == a or d == b:
                    d = a + b
                if c != d:
                    new_edges.append((c,d))
            edges_worker = new_edges
            vertices_worker.add(a+b)
            vertices_worker.remove(a)
            vertices_worker.remove(b)

    v = [a for a in vertices_worker]
    ans1 = len(v[0])//3 * len(v[1])//3

    # hfx/pzl bvb/cmg nvd/jqt
    
    # Part 2

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