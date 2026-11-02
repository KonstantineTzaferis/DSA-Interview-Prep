# In this traversal method first we visit the parent node and then left and right
class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def preOrderRecursive(self, root: TreeNode | None) -> None:
		if not root:
			return

		print(root.val)
		self.preOrderRecursive(root.left)
		self.preOrderRecursive(root.right)
