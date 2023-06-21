class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkList:
    def __init__(self,value):
        new_Node = Node(value)
        self.head = new_Node
        self.tail = new_Node
        self.length = 1

    def printList(self):
        temp = self.head

        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    #  append 

    def append(self,value):
        new_Node = Node(value)

        if self.length ==0:
            self.head = new_Node
            self.tail = new_Node
           
        else:
            self.tail.next = new_Node
            self.tail = new_Node
        self.length +=1

        return True
    def pop_lasItems(self):

        if self.length == 0:
            return None
        else:
            pre = self.head
            temp = self.head
            while temp.next is not None:
                pre = temp 
                temp = temp.next
            self.tail = pre
            self.tail.next = None
            self.length -= 1

        return temp
    def prepend(self,value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.length +=1
        return True

    def pop_first(self):
# edge case of when length id null 
        if self.length == 0:
            return None
        # edge case for more then two node 
        else:
            temp = self.head
            self.head = self.head.next
            temp.next = None
            self.length -=1
#     edge case of single node 

            if self.length == 0 :
                self.tail = None
            return temp
    

    def get(self,index):

        if index < 0 or index >= self.length:
            return None
        else:
            temp = self.head
            for _ in range(index):
                temp = temp.next
                

            return temp
        # set value for the particular index
    def set_value(self,index,value):
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    #insert the node for particular index 
    def insertion(self, index, value):
   

        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            return self.prepend(value)

        if  index == self.length:

            return self.append(value)
        new_node = Node(value)
        temp = self.get(index -1)
        new_node.next = temp.next
        temp.next = new_node
        self.length +=1
        return True

    def remove(self, index):
        # case 1
        if index < 0 or index >= self.length:
            return None
        # case 2
        if index == 0 :
            return self.pop_first()
        # case 3
        if index == self.length-1:
            return self.pop_lasItems()
        
        # case 4
        prev = self.get(index -1)
        prev.next = temp.next
        temp = prev.next

        temp.next = None
        self.length -= 1
        return temp
    
    # ** reversing link list

    def reverse(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp

        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after


        



my_linked_list = LinkList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

# print('LL before set_value():')
# my_linked_list.printList()

# my_linked_list.set_value(1,4)

# print('\nLL after set_value():')


my_linked_list.insertion(2,2333)
# my_linked_list.remove(0)
my_linked_list.reverse()
my_linked_list.printList()




