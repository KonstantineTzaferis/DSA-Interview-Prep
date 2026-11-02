class TreeNode:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def postOrderRecursive(self, root: TreeNode | None) -> None:
		if not root:
			return

		self.postOrderRecursive(root.left)
		self.postOrderRecursive(root.right)
		print(root.val)
