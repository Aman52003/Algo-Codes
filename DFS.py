def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()  # Create an empty set to keep track of visited nodes
    visited.add(start)  # Mark the current node as visited
    print(start)  # Print the current node to show the DFS traversal
    
    for neighbor in graph[start]:  # Recur for all unvisited neighbors of the current node
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

dfs(graph, 'A')  # Start DFS from node 'A'
