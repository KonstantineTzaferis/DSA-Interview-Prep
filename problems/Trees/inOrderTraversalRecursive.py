from typing import Optional


class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


# Returns list[int] -> The values are added in a list
class Solution:
	def inOrderTraversalRecursive(self, root: Optional[TreeNode]) -> list[int]:
		nodes = []

		def helper(root: Optional[TreeNode]):
			if not root:
				return

			helper(root.left)
			nodes.append(root.val)
			helper(root.right)

		helper(root)
		return nodes


root = TreeNode(8)

root.left = TreeNode(4)
root.right = TreeNode(12)

root.left.left = TreeNode(2)
root.left.right = TreeNode(6)

root.left.right.left = TreeNode(5)

root.right.right = TreeNode(14)

s = Solution()
print(s.inOrderTraversalRecursive(root))
