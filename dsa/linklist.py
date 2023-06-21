# head = {
#     'value': 1,
#     'next':{
#     'value':2,
#     'next':{
#     'value':3,
#     'next':{
#     'value':4,
#     'next':None
#     }
#     }
#     }
# }

# print(head['next']['next']['value'])

# LINK LIST CREATING A FIRST NODE
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self, value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1
# my_LinkList = LinkList(2)
# print(my_LinkList.head.value)

    def print_list(self):
        temp = self.head # points to the head of the linklist
        while temp is not None:
            print(temp.value)
            temp = temp.next # point to the next address of the link list

    def append_list(self, value):
        new_Node = Node(value)
        
        if self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length +=1
        return True
    
    # pop the link list

    def pop_Items(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head

        while(temp.next):
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -=1

        if self.length ==0:
            self.head = None
            self.tail = None
        return temp.value
# prepend to the list
    def prepend(self, value):
        new_Node = Node(value)
        if  self.length == 0:
            self.head = new_Node
            self.tail = new_Node
        else:
            new_Node.next = self.head
            self.head = new_Node
        self.length +=1
        return True
    # pop first item in list
    def pop_first(self):

        if self.length == 0:
            return None
        
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -= 1
        if self.length == 0 :
            self.tail = None
        return temp

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
            return temp

    
my_linklilst = LinkList(1)
my_linklilst.append_list(2)
# my_linklilst.append_list(2)
# my_linklilst.append_list(2)
# my_linklilst.append_list(3)
my_linklilst.prepend(1)
# my_linklilst.pop_first()
my_linklilst.get(0)
my_linklilst.print_list()

# print(my_linklilst.pop_Items())

