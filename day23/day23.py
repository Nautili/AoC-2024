import sys
from collections import defaultdict


def get_three_cliques(graph):
    seen = set()
    count = 0
    for source, adj in graph.items():
        for i in range(len(adj) - 1):
            if adj[i] not in seen:
                for j in range(i + 1, len(adj)):
                    if adj[j] not in seen and adj[j] in graph[adj[i]]:
                        if source[0] == 't' or adj[i][0] == 't' or adj[j][0] == 't':
                            count += 1
        seen.add(source)
    return count


def get_max_clique(graph):
    max_clique = set()

    def get_max_clique_bk(included, remaining, excluded):
        nonlocal max_clique

        if not remaining and not excluded:
            if len(included) > len(max_clique):
                max_clique = included.copy()
            return

        for start in [*remaining]:
            get_max_clique_bk(included | {start},
                              remaining & set(graph[start]),
                              excluded & set(graph[start]))
            remaining -= {start}
            excluded |= {start}

    get_max_clique_bk(included=set(),
                      remaining=set(graph.keys()),
                      excluded=set())
    return ','.join(sorted(max_clique))


def build_graph(edges):
    graph = defaultdict(list)
    for s, e in edges:
        graph[s].append(e)
        graph[e].append(s)
    return graph


def main():
    with open(sys.argv[1]) as f:
        edges = [line.strip().split('-') for line in f.readlines()]
    graph = build_graph(edges)
    print(get_three_cliques(graph))
    print(get_max_clique(graph))


if __name__ == '__main__':
    main()
