import array as arr

array1=arr.array('i',[1,2,3,4,5])

array2=arr.array('i',[1,4,5])

k=0

for j in range(len(array2)):

   for i in range(len(array1)):

      if array2[j]!=array1[i]:

         continue
         
      else:
         
         k+=1
         break

if k==len(array2):
   print("subset hai")

else:
   print("subset nhi hai")