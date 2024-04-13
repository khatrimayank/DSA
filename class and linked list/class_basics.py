class myclass:
    #class varible
    x=5

#object define rohan ansd sohan have all properties of class myclass
rohan=myclass()
sohan=myclass()

print(rohan.x)
print(sohan.x)
print(myclass.x)

#it will change variable x only for rohan
rohan.x=6
print(rohan.x)
print(sohan.x)
print(myclass.x)

#it will change variable x for sohan,class not for rohan
myclass.x=8
print(rohan.x)
print(sohan.x)
print(myclass.x)


#it will change variable x for rohan,sohan,class
myclass.x=8
rohan=myclass()
sohan=myclass()
print(rohan.x)
print(sohan.x)
print(myclass.x)