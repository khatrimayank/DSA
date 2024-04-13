list_to_be_sort=[]

import math

def validate(validate_check_for_no_of_integer):

    validate_check_for_no_of_integer=str(validate_check_for_no_of_integer)

    length_of_input_integer=len(validate_check_for_no_of_integer)

    for i in range(length_of_input_integer):
        if validate_check_for_no_of_integer[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
            return False

    return True    
    

def validate1(validate_check_of_integer):


    length_of_input_integer=len(validate_check_of_integer)

    validate_check_of_integer=str(validate_check_of_integer)

    for i in range(length_of_input_integer):
            if validate_check_of_integer[i] not in ["0","1","2","3","4","5","6","7","8","9"]:
                return False
            
    return True

a=True

count=0

while a:

    no_of_input_integers=input("how many numbers U want to add:")

    is_valid_input_of_no_of_integers=validate(no_of_input_integers)

    if is_valid_input_of_no_of_integers!=True:
        print("please enter valid input")
        continue

    no_of_input_integers=int(no_of_input_integers)

    while count<no_of_input_integers:

        input_integer=input("please enter no : ")

        is_valid_input_integer=validate1(input_integer)

        if is_valid_input_integer!=True:

            print("please enter valid input")
            continue

        else:
            count+=1

        list_to_be_sort.append(input_integer)

    print("list of numbers before sorting:",list_to_be_sort)

    for j in range(len(list_to_be_sort)):

        for i in range(len(list_to_be_sort)):

            if int(list_to_be_sort[j])< int(list_to_be_sort[i]):
                c=list_to_be_sort[j]
                list_to_be_sort[j]=list_to_be_sort[i]
                list_to_be_sort[i]=c

    print("list of numbers after sorting:",list_to_be_sort)

    y=input("enter 1 to continue:")

    if y=="1":
        count=0
        list_to_be_sort.clear()
        continue
    else:
        break
