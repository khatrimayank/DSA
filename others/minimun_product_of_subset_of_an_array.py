a=[2,3,5]

n=len(a)

def min_product(a,n):

    neg_count=0
    max_neg=float('-inf')
    zero_count=0
    product=1

    for i in range(n):
        
        if a[i]==0:
            zero_count+=1
            continue

        if a[i]<0:
            neg_count+=1
            max_neg=max(max_neg,a[i])

        product=product*a[i]


    if neg_count!=0:
        if neg_count%2!=0:
            return product
        else:
            return int(product/(max_neg))

    return min(a)

output=min_product(a,n)

print(output)