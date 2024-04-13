file1=open('aa11.py','r')

books={}
borrowers={}
checkout=[]


l=file1.readlines()
  
books_index=l.index('Books\n')
borrowers_index=l.index("Borrowers\n")
checkout_index=l.index("Checkouts\n")
end=len(l)

print(books_index,borrowers_index,checkout_index,end)

for i in range(end-1):

    if (i>books_index and i<borrowers_index):
        key,value=(l[i]).split('~')
        books[key]=value[:-1]

    if (i>borrowers_index and i<checkout_index):
        key,value=(l[i]).split('~')
        borrowers[key]=value[:-1]

    if i>checkout_index:
        key,value1,vlaue2=l[i].split('~')
        checkout.append([key,value1,vlaue2[:-1]])
        
print(checkout)

res=[]

for i in checkout:
    s=i[2]+'~'+borrowers[i[0]]+'~'+books[i[1]]
    res.append(s)

for i in sorted(res)
:
    print(i)
