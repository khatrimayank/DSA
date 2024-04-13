'''def longestCommonPrefix(strs):
        
    length=len(strs)
    minimum_length=len(strs[0])
    for i in range(length):
        
        llength=len(strs[i])
        
        if llength<minimum_length:
            minimum_length=llength
        
    arr=[]
    if length>1:
        for j in range(minimum_length):
            i=0
            
            for i in range(length-1):
                
                
                if strs[i][j]==strs[i+1][j]:

                    print(j)
                    
                    if i==(length-2):
                        (arr.append(strs[i][j]))
                        break
                        
                    else:
                        continue
                else:
                   
                    break
                
            if strs[i][j]!=strs[i+1][j]:
                break    
        if not arr:
            print(" "" ")
        else:
            print("".join(arr))

    else:
        print("".join(strs))

strs=['cir','car']

longestCommonPrefix(strs)'''

strs = ["dog","racecar","car"]

l=len(strs)

s=""

min_l=len(min(strs))

min_strs=min(strs)

for i in range(min_l):#i=[0,1,2,3]

    count=0

    for j in range(l-1):#j=[0,1]

        if strs[j][i]==strs[j+1][i]:

            count+=1

            continue

        else:
            break

    if count==l-1:
        s=s+min_strs[i]

    else:
        break

print(s)






           
     
