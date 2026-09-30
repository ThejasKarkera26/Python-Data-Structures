stack=[]

#push
def push():
    ele=input("Enter a element to push:")
    stack.append(ele)
    print(ele,"pushed to stack.")

def pop():
    if len(stack)==0:
        print("Stack underflow")
    else:
        ele=stack.pop()
        print(ele,"popped from the stack.")

#peek
def peek():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Top element:",stack[-1])


#display
def display():
    if len(stack)==0:
        print("Stack is empty")
    else:
        print("Stack elements:",stack)

#menu
while True:
    print("\n-----Stack Menu-----")
    print("1.Push \n2.Pop \n3.peek \n4.display \n5.Exit")

    ch=int(input("Enter your choice (1-5):"))
    if ch==1:
        push()
    elif ch==2:
        pop()
    elif ch==3:
        peek()
    elif ch==4:
        display()
    elif ch==5:
        print("Exiting...")
        break

    else:
        print("Invalid choice...!!!")
