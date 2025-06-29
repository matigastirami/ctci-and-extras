from typing import Optional

def find_path(grid: list[list[int]], c: int, r: int, path: list[list[int]]) -> Optional[list[list[int]]]:
    m = len(grid)
    n = len(grid[0])

    if r >= m or c >= n or grid[r][c] == 1:
        return None

    if r == m - 1 and c == n - 1:
       return path + [[c, r]]

    right = find_path(grid, r, c + 1, path)
    down = find_path(grid, r + 1, c, path)

    if right is None and down is None:
        return None

    return path + (right if right is not None else down)

def test_find_path():
    # Test 1: Simple open grid
    grid1 = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]
    path = find_path(grid1, 0, 0, [])
    assert path is not None
    assert path[-1] == [2,2], f"Expected to reach goal, got path ending at {path[-1]}"

    # Test 2: Grid with a block forcing detour
    grid2 = [
        [0,0,0],
        [0,1,0],
        [0,0,0]
    ]
    path = find_path(grid2, 0, 0, [])
    assert path is not None
    assert path[-1] == [2,2]

    # Test 3: Grid with no possible path
    grid3 = [
        [0,1,0],
        [1,1,0],
        [0,0,0]
    ]
    path = find_path(grid3, 0, 0, [])
    assert path is None, f"Expected None, got {path}"

    # Test 4: Start is blocked
    grid4 = [
        [1,0,0],
        [0,0,0],
        [0,0,0]
    ]
    path = find_path(grid4, 0, 0, [])
    assert path is None

    # Test 5: Goal is blocked
    grid5 = [
        [0,0,0],
        [0,0,0],
        [0,0,1]
    ]
    path = find_path(grid5, 0, 0, [])
    assert path is None

    print("✅ All find_path tests passed!")

if __name__ == '__main__':
    test_find_path()
