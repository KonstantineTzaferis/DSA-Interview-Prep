class TreeNode:
	def __init__(self, val) -> None:
		self.val = val
		self.right = None
		self.left = None


class Solution:
	def preOrderIterative(self, root: TreeNode | None) -> list[int | None]:
		if not root:
			return []

		curr = root
		stack = []
		nodes_preorder = []

		while stack or curr:
			while curr:
				nodes_preorder.append(curr.val)
				stack.append(curr)
				curr = curr.left

			curr = stack.pop()
			curr = curr.right

		return nodes_preorder
