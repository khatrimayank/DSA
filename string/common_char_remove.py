def change_char(list1,list2):

    for i in range(len(list1)):

        for j in range(len(list2)):

            if list2[j]==list1[i]:

                c=list2[j]
                list2.remove(c)
                list1.remove(c)

                list3=list1+["*"]+list2
        
                return [list3,True]
    list3=list1+["*"]+list2
    return [list3,False]


p1=input("enter player 1 name=")

p1=p1.lower()

p1_list=list(p1)

p2=input("enter player 2 name=")

p2=p2.lower()

p2_list=list(p2)

proceed=True

while proceed:

    change_char(p1_list,p2_list)

    ret_list=change_char(p1_list,p2_list)

    new_list=ret_list[0]

    proceed=ret_list[1]

    x=new_list.index("*")

    p1_list=new_list[:x]

    p2_list=new_list[x+1:]

list3=p1_list+p2_list

print("".join(list3))

count=len(list3)

print(count)



                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        