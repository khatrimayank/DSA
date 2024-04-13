from operator import itemgetter

dict={'rahul':13,'aditya':13,'adi':14,'lokesh':15}


# sort by key

print(sorted(dict.items(),key=lambda x : x[0]))

print(sorted(dict.items(),key=itemgetter(0)))

# sort by value

print(sorted(dict.items(),key=lambda x : (x[1],x[0])))

print(sorted(dict.items(),key=itemgetter(1,0)))