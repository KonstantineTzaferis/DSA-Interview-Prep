from problems.NeetCode150.Easy.removeElements import Node
from typing import Optional


class TreeNode:
	def __init__(self, key: int, val: int):
		self.key = key
		self.val = val
		self.left = None
		self.right = None


class TreeMap:
	def __init__(self):
		self.root: Optional[TreeNode] = None

	def insert(self, key: int, val: int) -> None:
		new_node: TreeNode = TreeNode(key, val)

		# if not root(Empty Tree)
		if not self.root:
			self.root = new_node
			return

		# Pointing to the self.root node
		curr: TreeNode = self.root

		while curr:
			if new_node.key > curr.key:
				if not curr.right:
					curr.right = new_node
					return

				curr = curr.right
			elif new_node.key < curr.key:
				if not curr.left:
					curr.left = new_node
					return

				curr = curr.left
			else:
				# Replacing the value when we have duplicate keys
				curr.val = val
				return

	def get(self, key: int) -> int:
		flag = -1

		if not self.root:
			return -1

		curr = self.root

		while curr:
			if key > curr.key:
				if not curr.right:
					return flag

				curr = curr.right

			elif key < curr.key:
				if not curr.left:
					return flag

				curr = curr.left

			else:
				flag = curr.val
				return flag

	def getMin(self) -> int:
		if not self.root:
			return -1

		curr = self.root
		while curr and curr.left:
			curr = curr.left

		return curr.val

	def getMax(self) -> int:
		if not self.root:
			return -1

		curr = self.root
		while curr and curr.right:
			curr = curr.right

		return curr.val

	def remove(self, key: int) -> None:
		curr: Optional[TreeNode] = self.root
		prev: Optional[TreeNode] = None

		while curr:
			if key > curr.key:
				prev = curr
				curr = curr.right
			elif key < curr.key:
				prev = curr
				curr = curr.left
			else:
				# We have found the Node
				break

		if not curr:
			return

		# We have a leaf node(No children)
		if not curr.left and not curr.right:
			if prev is None:
				self.root = None
			elif prev.left is curr:
				prev.left = None
			else:
				prev.right = None

		# We have exactly one child
		if (curr.right and not curr.left) or (not curr.right and curr.left):
			if curr.left:
				child = curr.left
			else:
				child = curr.right

			if prev is None:
				self.root = child
			# Now we put the node into the right or left of the prev
			elif prev.left is curr:
				prev.left = child
			else:
				prev.right = child

		# We have two children
		successor_parent = curr
		successor = curr.right

		while successor.left:
			successor_parent = successor
			successor = successor.left

		curr.val = successor.val
		curr.key = successor.key

		if successor_parent is curr:
			successor_parent.right = successor.right # type: ignore
		else:
			successor_parent.left = successor.right # type: ignore

	def getInorderKeys(self) -> list[Optional[int]]:
		if not self.root:
			return []

		curr = self.root
		stack = []
		nodes_inorder = []

		curr = self.root
		while curr or stack:
			if curr:
				stack.append(curr)
				curr = curr.left
			else:
				curr = stack.pop()
				nodes_inorder.append(curr.key)
				curr = curr.right

		return nodes_inorder
