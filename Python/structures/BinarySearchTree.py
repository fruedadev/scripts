from __future__ import annotations

class Node:
	value: int
	left: Node
	right: Node

	def __init__(self, value) -> None:
		self.value = value
		self.left = None
		self.right = None

class BinarySearchTree:
	root: Node

	def __init__(self, value: int = None) -> None:
		self.root = Node(value) if value else None

	def insert(self, value: int) -> bool:
		new_node = Node(value)

		if not self.root:
			self.root = new_node
			return True

		temp = self.root	
		while True:
			if value == temp.value:
				return False
			
			if value < temp.value:
				if not temp.left:
					temp.left = new_node
					return True
				temp = temp.left
			else:
				if not temp.right:
					temp.right = new_node
					return True
				temp = temp.right

	def contains(self, value: int) -> bool:
		temp = self.root
		while temp:
			if value < temp.value:
				temp = temp.left
			elif value > temp.value:
				temp = temp.right
			else:
				return True
			
		return False

# ----------- TEST CODE ------------

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Contains on Empty Tree -----\n")
bst = BinarySearchTree()
result = bst.contains(5)
check(False, result, "Check if 5 exists in an empty tree:")

print("\n----- Test: Contains Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.contains(10)
check(True, result, "Check if 10 exists:")
result = bst.contains(5)
check(True, result, "Check if 5 exists:")
result = bst.contains(15)
check(True, result, "Check if 15 exists:")

print("\n----- Test: Contains Not Existing Value -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
result = bst.contains(15)
check(False, result, "Check if 15 exists:")

print("\n----- Test: Contains with Duplicate Inserts -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(10)
result = bst.contains(10)
check(True, result, "Check if 10 exists with duplicate inserts:")

print("\n----- Test: Contains with Left and Right -----\n")
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
bst.insert(1)
bst.insert(8)
bst.insert(12)
bst.insert(20)
result = bst.contains(1)
check(True, result, "Check if 1 exists:")
result = bst.contains(8)
check(True, result, "Check if 8 exists:")
result = bst.contains(12)
check(True, result, "Check if 12 exists:")
result = bst.contains(20)
check(True, result, "Check if 20 exists:")
