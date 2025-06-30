# There are 3 towers
# The first one has N disks sorted by size increasingly
# Only one disk can be moved at a time
# A disk cannot be placed on top of a smaller disk
# Move the disks from the first tower to the last following the constraints

# DEFAULT_TOWERS_SIZE = 7

# def init_towers(size: int) -> list[list[int]]:
#     towers = [
#         [],
#         [],
#         [],
#     ]

#     for n in range(size, 1, -1):
#         towers[0].append(n)

#     return towers

# def is_solved(towers: list[list[int]], size: int):
#     is_tower_3_ok = True
#     for i in range(len(towers[2]), 1, -1):
#         if towers[2][i] != towers[2][i - 1]:
#             return False

#     return len(towers[0]) == 0 and len(towers[2]) == size and is_tower_3_ok

def move_tower(n, source, target, helper, moves=None):
    if moves is None:
        moves = []

    if n == 1:
        moves.append(f'Move disk 1 from {source} to {target}')
    else:
        move_tower(n - 1, source, helper, target, moves)
        moves.append(f'Move disk {n} from {source} to {target}')
        move_tower(n - 1, helper, target, source, moves)

    return moves

def test_move_tower():
    moves = move_tower(3, "A", "C", "B")
    assert len(moves) == 7  # 2^3 - 1
    assert moves[0] == "Move disk 1 from A to C"
    assert moves[-1] == "Move disk 1 from A to C"
    print(moves)
    print("✅ Passed simple tower of hanoi test")

if __name__ == "__main__":
    test_move_tower()
