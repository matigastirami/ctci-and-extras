class GraphNode:
    def __init__(self, data) -> None:
        self.data = data
        self.adjacent = []

    def __hash__(self) -> int:
        return id(self)


class Graph:
    def __init__(self) -> None:
        self.nodes = []

    def add_edge(self, from_node: GraphNode, to_node: GraphNode):
        from_node.adjacent.append(to_node)
