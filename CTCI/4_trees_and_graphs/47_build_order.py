# Solution 1 with adjacency list
def mount_graph(deps: list[tuple[str, str]]) -> dict:
    adjacency_list = {}
    for dep, dependent in deps:
        if dep not in adjacency_list:
            adjacency_list[dep] = []

        adjacency_list[dep].append(dependent)
    return adjacency_list

def calculate_in_degress(projects: list[str], adjacency_list: dict) -> dict:
    in_degrees = {}
    for key, adjacents in adjacency_list.items():
        for node in adjacents:
            if node not in in_degrees:
                in_degrees[node] = 0
            in_degrees[node] += 1

    for project in projects:
        if project not in in_degrees:
            in_degrees[project] = 0

    return in_degrees


def build_order(projects: list[str], deps: list[tuple[str, str]]) -> list[str]:
    order = []
    queue = []
    adjacency_list = mount_graph(deps)
    in_degress = calculate_in_degress(projects, adjacency_list)
    zero_keys = [k for k, v in in_degress.items() if v == 0]
    queue.extend(zero_keys)

    while len(queue):
        proj = queue.pop(0)
        order.append(proj)
        for neighbor in adjacency_list.get(proj, []):
            in_degress[neighbor] -= 1
            if in_degress[neighbor] == 0:
                queue.append(neighbor)

    if len(order) < len(projects):
        raise Exception("Circular dependency detected")

    return order

def test_build_order():
    # Valid build order test
    projects = ['a', 'b', 'c', 'd', 'e', 'f']
    deps = [
        ('a', 'd'),
        ('f', 'b'),
        ('b', 'd'),
        ('f', 'a'),
        ('d', 'c'),
        ('e', 'a'),
        ('e', 'f'),
    ]

    order = build_order(projects, deps)
    position = {project: idx for idx, project in enumerate(order)}

    assert sorted(order) == sorted(projects), "Not all projects are in the build order"

    for dep, dependent in deps:
        assert position[dep] < position[dependent], f"Dependency order violated: {dep} must come before {dependent}"

    print("✅ test_build_order passed (valid input)")

    # Circular dependency test
    projects = ['a', 'b', 'c']
    circular_deps = [('a', 'b'), ('b', 'c'), ('c', 'a')]

    try:
        build_order(projects, circular_deps)
        assert False, "Should have raised an error due to circular dependency"
    except Exception as e:
        print("✅ test_build_order passed (circular input):", str(e))

if __name__ == '__main__':
    test_build_order()
