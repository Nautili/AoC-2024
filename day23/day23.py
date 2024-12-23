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


def get_max_clique_bk(graph, included, remaining, excluded):
    if not remaining and not excluded:
        return included

    best_set = set()
    for start in [*remaining]:
        next_set = get_max_clique_bk(graph,
                                     included | {start},
                                     remaining & set(graph[start]),
                                     excluded & set(graph[start]))
        if len(next_set) > len(best_set):
            best_set = next_set
        remaining -= {start}
        excluded |= {start}
    return best_set


def get_max_clique(graph):
    max_clique = get_max_clique_bk(graph, set(), set(graph.keys()), set())
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
