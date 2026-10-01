#consider atuple           
tp1=(1,2,3,4,5,6,7,8,9,10)
print("\nTuple is:",tp1)
mid=len(tp1)//2
print("After dividing the tuple:")
print("1st half:",tp1[:mid])
print("2nd half",tp1[mid:])
newtp=list()
for i in range(len(tp1)):
    if tp1[1]%2==0:
        newtp.append(tp1[i])
print("Even Numbers in the given Tuple are:",tuple(newtp))
tp2=(11,13,15)
print("\nTuple 2:",tp2)
print("Concatenated tuple is:",tp1+tp2)
print("Maximum number in tuple is",max(tp1))
print("Minimum number in tuple is:",min(tp1))
