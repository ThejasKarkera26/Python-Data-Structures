#Write a program to create list with N elements.Find all unique elements in the list then add that element to the unique list.
#Read Number of elements
N=int(input("Enter number of elements:"))
#create List
i=1;
lst=[]
for i in range(N):
    element =input(f"Enter element {i+1}:")
    lst.append(element)
#Find unique element
unique_list=[]
for item in lst:
    if lst.count(item)==1:
            unique_list.append(item)
#display results
print("Original List:",lst)
print("Unique Elements List:",unique_list)
