d=dict()

n=int(input("Enter number of elements to the dictionary:"))
for i in range(n):
    key=input("Enter key:")
    value=input("Enter value:")
    d[key]=value
print("Dictionary:",d)

ukey=input("Enter key to update:")
uvalue=input("Enter new value:")
d[ukey]=uvalue
print("After update:",d)

akey=input("Enter key to access:")
print("Using key:",d[akey])
print("Using get()method:",d.get(akey))

dkey=input("Enter key to delete :")
del d[dkey]
print("After deletion:",d)

    
