import tkinter as tk
from tkinter import messagebox

#Student form
root=tk.Tk()
root.title("Student Registration Form")
root.geometry("600x650")
root.configure(bg="gray")

menu=tk.Menu(root)
root.config(menu=menu)

#title
tk.Label(root,text="Student Registration",font=("Arial",16)).grid(row=0,column=0,columnspan=2,pady=10)


#Name
tk.Label(root,text="Name").grid(row=1,column=0,sticky="w",padx=10)
name=tk.Entry(root)
name.grid(row=1,column=1,padx=10)

#Gender
tk.Label(root,text="Gender").grid(row=2,column=0,sticky="w",padx=10)
gender=tk.StringVar(value="Male")
tk.Radiobutton(root,text="Male",variable=gender,value="Male").grid(row=2,column=1,sticky="w")
tk.Radiobutton(root,text="Female",variable=gender,value="Female").grid(row=3,column=1,sticky="w")

#course(Listbox)
tk.Label(root,text="Course").grid(row=4,column=0,sticky="w",padx=10)
course_list=tk.Listbox(root,height=4)
course_list.grid(row=4,column=1)

for c in["BCA","BSc","BA","BCom"]:
    course_list.insert(tk.END,c)

#year(spinbox)
tk.Label(root,text="Year").grid(row=5,column=0,sticky="w",padx=10)
year=tk.Spinbox(root,from_=1, to=4)
year.grid(row=5,column=1)


#Skills
tk.Label(root,text="Skills",).grid(row=6,column=0,sticky="w",padx=10)
python_var=tk.IntVar()
java_var=tk.IntVar()
tk.Checkbutton(root,text="Python",variable=python_var).grid(row=6,column=1,sticky="w")
tk.Checkbutton(root,text="Java",variable=java_var).grid(row=7,column=1,sticky="w")

#Adress(Text+Scrollbar)
tk.Label(root,text="Address").grid(row=8,column=0,sticky="nw",padx=10)

frame=tk.Frame(root)
frame.grid(row=8,column=1)

scrollbar=tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT,fill=tk.Y)

address=tk.Text(frame,height=4,width=30,yscrollcommand=scrollbar.set)
address.pack()
scrollbar.config(command=address.yview)

#message
msg=tk.Message(root,text="Fill all details carefully",width=200)
msg.grid(row=9,column=0,columnspan=2,pady=10)

#submit
def submit():
    selected_course=course_list.get(tk.ACTIVE)
    skills=[]

    if python_var.get():
         skills.append("Python")
    if java_var.get():
        skills.append("Java")
    info=f"""
            Name:{name.get()}
            Gender:{gender.get()}
            Course:{selected_course}
            Year:{year.get()}
            Skills:{','.join(skills)}
            Address:{address.get("1.0",tk.END)}
    """
            

    messagebox.showinfo("Student Data",info)
    stk.Button(root,text="Submit",command=submit).grid(row=10,column=0,columnspan=2,pady=10)

#menu
file_menu=tk.Menu(menu,tearoff=0)
menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="Exit",command=root.quit)
root.mainloop()













        


                                                

                        
