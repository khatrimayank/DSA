class Node:

    def __init__(self,data):

        self.data=data
        self.next=None

class linkedlist:

    def __init__(self):

        self.head=None

    def push(self,new_data):

        new_node=Node(new_data)

        if self.head==None:
            self.head=new_node
            return

        temp=self.head

        while temp:
            prev=temp
            temp=temp.next

        prev.next=new_node


    def reverse(self):

        current=self.head
        prev=None
        nextt=None

        while current:
            nextt=current.next
            current.next=prev
            prev=current
            current=nextt
        self.head=prev

    def printlist(self):
        temp=self.head

        while(temp):
            print(temp.data)
            temp=temp.next

def linked_list_addition(list1,list2):

    list3=linkedlist()

    temp1=list1.head
    temp2=list2.head
    c=0

    while temp1 or temp2:
        if temp1!=None:
            a=int(temp1.data)
        else:
            a=0
        if temp2!=None:
            b=int(temp2.data)
        else:
            b=0
        if a+b+c>10:
            result=a+b+c-10
            c=1
        else:
            result=a+b+c
 
        new_node=Node(result)
        
        if list3.head==None:
            list3.head=new_node

        else:

            temp=list3.head

            while temp:
                prev=temp
                temp=temp.next

            prev.next=new_node

        if temp1!=None:
            temp1=temp1.next
        if temp2!=None:
            temp2=temp2.next

    return list3

list1=linkedlist()

repeat=True
while repeat:
    new_data=input("Enter data for LIST 1 FROM you want to bulid node")
    list1.push(new_data)
    repeat=input("Enter Y/N :")
    if repeat=='Y':
        continue
    else:
        break

list2=linkedlist()

repeat=True
while repeat:
    new_data=input("Enter data for LIST 2 FROM you want to bulid node")
    list2.push(new_data)
    repeat=input("Enter Y/N :")
    if repeat=='Y':
        continue
    else:
        break

print("list1")
list1.printlist()

print("list2")
list2.printlist()

list1.reverse()

list2.reverse()

result=linked_list_addition(list1,list2)
result.reverse()

print("list3")
result.printlist()