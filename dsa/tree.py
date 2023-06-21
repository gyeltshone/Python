class Node:
     def __init__(self, value):
          self.value = value
          self.right = None
          self.left = None
class BinarySearchTree:
     def __init__(self):
          self.root = None


     def insert(self, value):
          
          node =  Node(value)

          if self.root is None:
               self.root = node
               return True
               
          temp = self.root
          
          while (True):
               if node.value == temp.value:
                    return False
               if node.value < temp.value:
                    if temp.left is None:
                         temp.left = node
                         return True
                    temp = temp.left
               else:
                    if temp.right is None:
                         temp.right = node
                         return True
                    temp = temp.right
    # is contain or search


     def contains(self, value):
          if self.root is None:
               return False
          temp = self.root
          while temp is not None:
               if value < temp.value:
                    temp = temp.left

               elif value > temp.value:
                    temp = temp.right

               else:
                    return True
               
          return False

tree = BinarySearchTree()

tree.insert(3)
tree.insert(1)
tree.insert(6) 





print(tree.root.value)
print(tree.root.left.value)
print(tree.root.right.value)
print(tree.contains(6))


          