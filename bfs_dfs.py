graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B','F'],
    'F': ['C','E']
}

def bfs(graph, queue, visited):
    if not queue:
        return visited
    node = queue.pop(0)
    visited.append(node)
    for neighbor in graph[node]:
        if neighbor not in queue and neighbor not in visited:
            queue.append(neighbor)
    return bfs(graph, queue, visited)

print("BFS : ", bfs(graph, ['A'], []))

def dfs(graph, node, visited):
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, neighbor, visited)
    return visited


print("DFS : ", dfs(graph, 'A', []))
