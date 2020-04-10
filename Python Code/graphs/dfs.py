def dfsgraph(graph, start, visited = set()):
    visited.add(start)
    print(start)
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfsgraph(graph, neighbor, visited)

    return visitied
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}
dfsgraph(graph, '0')
