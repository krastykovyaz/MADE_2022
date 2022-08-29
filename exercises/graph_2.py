import sys
import threading

def read_data():
    sys.setrecursionlimit(10 ** 9)

    string = sys.stdin.read().splitlines()

    n, m = map(int, string[0].split())
    from collections import Counter, defaultdict
    graph = defaultdict(set)

    for e in string[1:]:
        i, j = e.split()

        graph[i].add(j)
        graph[j].add(i)
    del string
    return n, m, graph

def dfs():
    n, m, graph = read_data()
    collector = {}
    def walk(vertex, collector, stage):
        collector[vertex] = stage
        for u in graph[vertex]:
            if u not in collector:
                walk(u, collector, stage)
    count = 0
    for vertex in graph:
        if vertex not in collector:
            count += 1
            walk(vertex, collector, count)
    paths = n - len(graph)
    del graph
    counter_dict = {}
    for val in collector.values():
        if val not in counter_dict:
            counter_dict[val] = 1
        else:
            counter_dict[val] += 1
    for _, i in counter_dict.items():
        paths += i ** 2
    print(paths)



if __name__=='__main__':
    threading.stack_size(2 ** 26)
    thread = threading.Thread(target=dfs)
    thread.start()