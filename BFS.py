from collections import deque

def bfs(graph, start):
    visited = set()  # Create an empty set to keep track of visited nodes
    queue = deque([start])  # Create a deque and add the starting node to it
    
    while queue:  # Loop until the deque is empty
        node = queue.popleft()  # Remove the first node from the deque
        if node not in visited:  # Check if the node has already been visited
            visited.add(node)  # Mark the node as visited
            print(node)  # Print the node to show the BFS traversal
            for neighbor in graph[node]:  # Add all unvisited neighbors of the node to the deque
                if neighbor not in visited:
                    queue.append(neighbor)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

bfs(graph, 'A')  # Start BFS from node 'A'
