import sys

def get_path():
    sys.setrecursionlimit(10 ** 9)
    string= sys.stdin.read().splitlines()
    n, m = map(int, string[0].split())
    task = string[1:]
    graph = dict()
    
    for e in task:
        f, s = e.split()
        if f not in graph:
            graph[f] = set()
        if s not in graph:
            graph[s] = set()
        graph[f].add(s)
    paths = 0
    for i in graph:
        nodes = set()
        def walk(node):
            nodes.add(node)
            for v in graph[node]:
                if v not in nodes:
                    walk(v)
        walk(i)
        paths += len(nodes)

    paths += n - len(graph)
    return paths

if __name__=='__main__':
    string = '''
    4 3
1 2
2 3
1 4'''
    print(get_path())