# class Cookie:
#     def __init__(self, color):
#         self.color = color

#     def get_color(self):
#         return self.color
#     def set_color(self, color):
#         self.color = color

# cookie_one = Cookie('green')
# cookie_two = Cookie('blue')

# print('cookie one is ', cookie_one.get_color())
# print('cookie two is ', cookie_two.get_color())

# cookie_one.set_color('yellow')

# print('cookie one color is set to ', cookie_one.get_color())


# POINTERS 

# num1 = 11
# num2 = 22

# print ( 'num one address',id(num1))
# print( 'num two address',id(num2))


# dict1 = {
#     "value":11
# }

# dict2 = dict1

# print('before value is updated')
# print('dict1 = ', dict1)
# print('dict2 = ', dict2)

# print('\ndict1 points to :', id(dict1))
# print('\ndict2 points to :', id(dict2))


# dict2['value'] = 22
# print('after value is updated')
# print('dict1 = ', dict1)
# print('dict2 = ', dict2)
# print('\ndict1 points to :', id(dict1))
# print('\ndict2 points to :', id(dict2))



# create a new node 

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.next = None

# class LinkList:
#     def __init__(self,value):
#         new_Node = Node(value)
#         self.head = new_Node
#         self.tail = new_Node
#         self.lenght = 1

#     def print_linkList(self):
#         temp = self.head

#         while temp is not None:
#             print(temp.value)
#             temp = temp.next

#     # append tail in link list 

#     def append(self, value):

#         new_Node = Node(value)
       
#         if self.lenght == 0:
#             self.head = new_Node
#             self.tail = new_Node
#         else:
#             self.tail.next = new_Node
#             self.tail = new_Node
#             self.lenght += 1
#         return True

# my_Linklist = LinkList(1)
# my_Linklist.append(3)
# my_Linklist.append(23)
# my_Linklist.print_linkList()
    

class Node:
    def __init__(self , value):
        self.value = value
        self.next = None

class LinkList:

    def __init__(self, value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.lenght = 1

    def print_linkList(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next


    def append(self, value):

        new_Node = Node(value)
        if self.lenght ==0:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail  = new_Node
            self.lenght += 1
            return True
        
        
        
myLinklist = LinkList(2)
myLinklist.append(11)
myLinklist.append(23)
myLinklist.print_linkList()


