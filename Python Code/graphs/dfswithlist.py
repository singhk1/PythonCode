def dfswithlist(graph, start, visited = []):
    #visited = []
    #start = 0
    visited.append(start)
    for i in graph[start]:
        if i not in visited:
            dfswithlist(graph, i, visited)
    return visited

graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]}
print(dfswithlist(graph, 0))
