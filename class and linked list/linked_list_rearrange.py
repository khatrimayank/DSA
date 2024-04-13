class Node:

    def __init__(self,data):

        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):

        self.head=None
        self.odd=None
        self.even=None
        self.evenodd=None

    def push(self,new_data):

        new_node=Node(new_data)

        new_node.next=self.head

        self.head=new_node


    def printlist(self):
        temp=self.head

        while(temp):
            print(temp.data,end="  ")
            print(id(temp))
            temp=temp.next
'''def rearrange(list):

    if list.head==None:
        print("list is empty")

    else:
        odd=list.head

        if list.head.next!=None:

            even=list.head.next
            even_head=even

            while  True:

                if even.next!=None:
                    odd.next=even.next
                    odd=odd.next
                else:
                    break

                if odd.next!=None:
                    even.next=odd.next
                    even=even.next
                else:
                    break

            odd.next=even_head
            even.next=None'''

def rearrange(head):

    main_head=temp=temp_even=temp_odd=head

    head_even=None
    head_odd=None

    #find head of even value series

    while temp_even!=None and temp_even.data%2!=0 :
        temp_even=temp_even.next

    if temp_even!=None:
        head_even=temp_even

    #find head of odd value series

    while temp_odd!=None and temp_odd.data%2==0:
        temp_odd=temp_odd.next
    if temp_odd!=None:
        head_odd=temp_odd

    #make even and odd list

    while temp:

        if (temp.data%2!=0) and (temp_odd!=None) and (temp!=temp_odd):

            temp_odd.next=temp
            temp_odd=temp_odd.next

        if (temp.data%2==0) and (temp_even!=None) and (temp!=temp_even):

            temp_even.next=temp
            temp_even=temp_even.next

        temp=temp.next

    if temp_odd!=None:
        temp_odd.next=None

    if temp_even!=None:
        temp_even.next=head_odd

    temp=main_head

    while temp:

        print(temp.data,end="  ")
        print(id(temp))

        temp=temp.next


list1=linkedlist()

list1.push(1)
list1.push(2)
list1.push(3)
list1.push(4)
list1.push(5)
list1.push(6)
list1.push(7)
list1.push(8)
list1.push(9)
list1.push(10)
list1.push(11)
list1.push(12)


print("list1")
list1.printlist()

print("list after rearrange")

rearrange(list1.head)

