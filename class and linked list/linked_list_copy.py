class Node:

    def __init__(self,data):

        self.data=data
        self.next=None


class linkedlist:

    def __init__(self):

        self.head=None
        self.odd=None


    def push(self,new_data):

        new_node=Node(new_data)

        new_node.next=self.head

        self.head=new_node

    '''def push_back(self, new_data):
        if self.head==None:
            new_node = Node(new_data)
            self.head = new_node
            return

        head=temp=self.head

        while temp.next:
            temp=temp.next

        new_node=Node(new_data)

        temp.next=new_node'''


        #need to maintain tail as well to push at the back of linked list otherwise need to iterate till last node everytime

    def printlist(self):
        temp=self.head

        while(temp):
            print(temp.data)
            temp=temp.next 


def copy_linked_list(list):

    new_list=linkedlist()

    new_list.head=Node(list.head.data)

    old_list_iter=list.head.next

    new_list_iter=new_list.head

    while old_list_iter:

        new_list_iter.next=Node(old_list_iter.data)

        old_list_iter=old_list_iter.next

        new_list_iter=new_list_iter.next

    temp=new_list.head

    while temp:

        print(temp.data)

        temp=temp.next


list1=linkedlist()

list1.push_back(3)
list1.push_back(1)
list1.push_back(4)
list1.push_back(2)
list1.push_back(5)
list1.push_back(6)
list1.push_back(7)

print("list1")
list1.printlist()

#list2=copy_linked_list(list1)
print("list2")
copy_linked_list(list1)
