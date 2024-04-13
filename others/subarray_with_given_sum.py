arr=[15,2,4,8,9,5,10,23]

s=23

ss=[]

for i in range(len(arr)):

    ss.append(arr[i])

    print(ss)

    if sum(ss)<s:
        continue

    elif sum(ss)==s:
        print(arr.index(ss[0]),i)

    elif sum(ss)>s:
        ss.pop(0)

