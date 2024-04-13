class Node:

    def __init__(self,data):

        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):

        self.head=None


    def push(self,new_data):

        new_node=Node(new_data)

        new_node.next=self.head

        self.head=new_node

    def insert_after_node(self,prev_node,new_data):

        new_node=Node(new_data)

        if prev_node==None:

            print("prev node must be in linked list")
            return

        new_node.next=prev_node.next

        prev_node.next=new_node



    def insert_at_end(self,new_data):

        new_node=Node(new_data)

        if self.head==None:

            self.head=new_node

        temp=self.head

        while(temp.next):
            temp=temp.next

        temp.next=new_node

        '''while(temp!=None):
            prev=temp
            temp=temp.next

        prev.next=new_node'''

    def deletion(self,key):

        temp=self.head

        if temp!=None:

            if temp.data==key:
                self.head=temp.next
                temp=None 
                return

            while temp!=None:
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next

            if temp==None:
                print("key is not available in linked list")
                return -1

            '''while (temp.next):
                if temp.data==key:
                    break
                prev=temp
                temp=temp.next

            if temp.next==None:
                print("key is not available in linked list")
                return -1'''

            prev.next=temp.next

            temp=None

        else:
            print("list is empty") 


    def deletion_position_given(self,position):

        temp=self.head

        index=0

        if temp!=None:

            if position==index:
                self.head=temp.next
                return

            while position!=index and temp!=None:
                if index==position:
                    break

                index+=1
                prev=temp
                temp=temp.next

            if temp==None:
                print("given position not available in linkedlist")
                return -1

            prev.next=temp.next

        else:
            print("linked list is empty")

    def reverse_list(self):
        
        prev=None
        current=self.head
        Next=None

        while (current.next):
            Next=current.next
            current.next=prev
            prev=current
            current=Next

        current.next=prev
     
        self.head=current

        '''while current:
            Next=current.next
            current.next=prev
            prev=current
            current=Next

        self.head=prev'''


    '''def reverse_list_recursive(self,prev,current):

        if current!=None:

            Next=current.next
            current.next=prev
            prev=current
            current=Next

        else:
            self.head=prev
            return

        self.reverse_list_recursive(prev,current)'''


    def printlist(self):

        temp=self.head

        while(temp):
            print(temp.data)
            temp=temp.next



list1=linkedlist()

list1.push(5)

list1.push(7)

list1.insert_at_end(9)

list1.insert_after_node(list1.head,2)

result=list1.deletion(9)

if result!=-1:
    list1.printlist()