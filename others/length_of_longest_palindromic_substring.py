s=""

def lvs(s,beg,end,count):

    print("c=",count,"b=",beg,"e=",end)

   
    if beg==end:

        count+=1
        
        print('c=',count,'b=',beg,'e=',end)
        return count

    elif beg>end:

        return count

    elif s[beg]==s[end]:

        count= lvs(s,beg+1,end-1,count+2)

        return max(count,max(lvs(s,beg+1,end,0),lvs(s,beg,end-1,0)))


    return max(lvs(s,beg+1,end,count),lvs(s,beg,end-1,count))

print(lvs(s,0,len(s)-1,0))