def longestPalindrome(s):
    ss=[]
    sss=[]
    if len(s)==1:
        return s
    else:
        l=0
        z=len(s)

        while l<z:
            for i in range(l,z-1):
                
                ss=list(s[i:z])
                j=0
                k=len(ss)-1
                
                while j<k:
                    if ss[j]!=ss[k]:
                        del ss[:]
                        break
                        
                    else:
                        j+=1
                        k-=1
                if len(sss)<len(ss):
                    sss=ss
                
            for i in range(z-1,l+1,-1):
                
                ss=list(s[l:i])
                j=0
                k=len(ss)-1
                
                while j<k:
                    
                    if ss[j]!=ss[k]:
                        del ss[:]
                        break
                        
                    else:
                        j+=1
                        k-=1
                if len(sss)<len(ss):
                    sss=ss

            l+=1
            z-=1

        if len(sss)==0:
            print(s[0])
        else:
            print("".join(sss))

s="sajdkfhskjlsdakjskdajksdajsdpkanak"
longestPalindrome(s)
