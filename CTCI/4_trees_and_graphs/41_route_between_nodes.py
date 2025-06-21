from CTCI.helpers.graphs import Graph, GraphNode
from CTCI.helpers.queues import Queue
from CTCI.helpers.stacks import Stack

# Recursive DFS
# def route_exists(graph: Graph, start: GraphNode, end: GraphNode, visited=None):
#     if start is None:
#         return False

#     if visited is None:
#         visited = set()

#     if start == end:
#         return True

#     if start in visited:
#         return False

#     visited.add(start)

#     for neighbor in start.adjacent:
#         if route_exists(graph, neighbor, end, visited):
#             return True

#     return False

# def route_exists(graph: Graph, start: GraphNode, end: GraphNode):
#     if start is None:
#         return False

#     if start == end:
#         return True

#     visited = set()
#     visited.add(start)
#     queue = Queue()
#     queue.push(start)

#     while not queue.is_empty():
#         node = queue.pop()

#         if node == end:
#             return True

#         for neighbor in node.adjacent:
#             if neighbor not in visited:
#                 visited.add(neighbor)
#                 queue.push(neighbor)

#     return False

# Iterative DFS
def route_exists(graph: Graph, start: GraphNode, end: GraphNode):
    if start is None:
        return False

    if start == end:
        return True

    visited = set()
    visited.add(start)
    stack = Stack()
    stack.push(start)

    while not stack.is_empty():
        node = stack.pop()

        if node == end:
            return True

        for neighbor in node.adjacent:
            if neighbor not in visited:
                visited.add(neighbor)
                stack.push(neighbor)

    return False

def test_route_exists():
    # Create nodes
    a = GraphNode("A")
    b = GraphNode("B")
    c = GraphNode("C")
    d = GraphNode("D")
    e = GraphNode("E")
    f = GraphNode("F")

    # Create graph structure
    a.adjacent = [b, c]
    b.adjacent = [d]
    c.adjacent = [e]
    e.adjacent = [f]
    d.adjacent = []  # Leaf
    f.adjacent = []  # Leaf

    graph = Graph()
    graph.nodes.extend([a, b, c, d, e, f])

    # ✅ Positive paths
    assert route_exists(graph, a, f) == True     # A → C → E → F
    assert route_exists(graph, a, d) == True     # A → B → D
    assert route_exists(graph, c, f) == True     # C → E → F
    assert route_exists(graph, b, d) == True     # B → D
    assert route_exists(graph, a, a) == True     # Trivial case

    # ❌ Negative paths
    assert route_exists(graph, d, a) == False    # D has no edges
    assert route_exists(graph, e, b) == False    # No back path
    assert route_exists(graph, f, d) == False    # No forward path from F
    assert route_exists(graph, d, f) == False    # Disconnected

    # 🔁 Cycle detection
    g = GraphNode("G")
    h = GraphNode("H")
    i = GraphNode("I")
    g.adjacent = [h]
    h.adjacent = [i]
    i.adjacent = [g]  # Cycle

    graph.nodes.extend([g, h, i])

    assert route_exists(graph, g, i) == True     # G → H → I
    assert route_exists(graph, i, g) == True     # I → G (cycle)
    assert route_exists(graph, h, g) == True     # H → I → G

    print("✅ All route_exists tests passed.")


if __name__ == '__main__':
    test_route_exists()
