from typing import Optional


class TreeNode:
    def __init__(self, data) -> None:
        self.data = data
        self.left: Optional[TreeNode] = None
        self.right: Optional[TreeNode] = None
        self.parent = None # For specific exercises like 4.6
