from collections import deque

def bfs(graph, root):
    visited = set()
    queue =deque([root])
    #visitied.add(root)

    while queue:
        vertex = queue.popleft()
        visited.add(vertex)
        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
    return visited

if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1,2]}
    graph2 = [[1, 2], [2], [3], [1, 2]]
    print(bfs(graph, 0))
    print(bfs(graph2, 0))
