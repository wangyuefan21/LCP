# Given a reference of a node in a connected undirected graph.
# Return a deep copy (clone) of the graph.
# Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

# Test case format:
# For simplicity, each node's value is the same as the node's index (1-indexed).
# For example, the first node with val == 1, the second node with val == 2, and so on.
# The graph is represented in the test case using an adjacency list.
# An adjacency list is a collection of unordered lists used to represent a finite graph.
# Each list describes the set of neighbors of a node in the graph.
# The given node will always be the first node with val = 1.
# You must return the copy of the given node as a reference to the cloned graph.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Node') -> 'Node':
    if node is None:
        return node
    clone = {}
    q = [node]
    visit = set()
    while q:
        cur = q.pop()
        if cur in visit:
            continue
        visit.add(cur)
        if cur not in clone:
            clone[cur] = Node(cur.val)
        for neighbor in cur.neighbors:
            if neighbor not in clone:
                clone[neighbor] = Node(neighbor.val)
            clone[cur].neighbors.append(clone[neighbor])
            q.append(neighbor)
    return clone[node]