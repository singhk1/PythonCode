from collections import defaultdict, deque

def find_order(graph):
    graph = {c: set(p) for c, p in graph.items()}
    to_do = deque([c for c, p in graph.items() if not p])

    new_graph = defaultdict(list)

    for course, pre_reqs in graph.items():
        for pre_req in pre_reqs:
            new_graph[pre_req].append(course)

    result = []

    while to_do:
        pre_req = to_do.popleft()
        result.append(pre_req)

        for c in graph[pre_req]:
            graph[c].remove(pre_req)
            if not graph[c]:
                to_do.append(c)

    if len(result) < len(graph):
        return None

    return result

graph = {
    'CSC300': ['CSC100', 'CSC200'],
    'CSC200' :['CSC100'],
    'CSC100': []
}

print(find_order(graph))
