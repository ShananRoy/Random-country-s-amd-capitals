from tkinter import *
import random

root=Tk()
root.title("Your lucky friends wheel")
root.geometry("500x500")

enter_name=Entry(root)
enter_name.place(relx=0.5,rely=0.2,anchor=CENTER)


friend_list=Label(root)
random_number_label=Label(root)
lucky_friend=Label(root)


enter_name1=Entry(root)
enter_name1.place(relx=0.5,rely=0.2,anchor=CENTER)


friend_list1=Label(root)
random_number_label1=Label(root)
lucky_friend1=Label(root)

list1=[]
list2=[]
def add_friend():
    friend_name=enter_name.get()
    list1.append(friend_name)
    friend_list["text"]="Random country" +str(list1)
    
def random_number():
    length=len(list1)
    random_no=random.randint(0, length-1)
    random_number_label["text"]=str(random_no)
    generated_random_number=list1[random_no]
    lucky_friend["text"]="Your random country is: "+str(generated_random_number)
    
    
def add_friend1():
    friend_name1=enter_name.get()
    list2.append(friend_name1)
    friend_list1["text"]="Random city" +str(list2)
    
def random_number1():
    length=len(list2)
    random_no1=random.randint(0, length-1)
    random_number_label1["text"]=str(random_no1)
    generated_random_number1=list1[random_no1]
    lucky_friend1["text"]="Your random city is: "+str(generated_random_number1)
    
btn=Button(root,text="add country",command=add_friend)
btn.place(relx=0.5,rely=0.3,anchor=CENTER)

friend_list.place(relx=0.5,rely=0.4,anchor=CENTER)

btn=Button(root,text="Show country",command=random_number)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)

random_number_label.place(relx=0.5,rely=0.6,anchor=CENTER)
lucky_friend.place(relx=0.5,rely=0.7,anchor=CENTER)

btn1=Button(root,text="add city",command=add_friend1)
btn1.place(relx=0.5,rely=0.4,anchor=CENTER)

friend_list1.place(relx=0.5,rely=0.4,anchor=CENTER)

btn1=Button(root,text="Show country",command=random_number1)
btn1.place(relx=0.5,rely=0.5,anchor=CENTER)

random_number_label1.place(relx=0.5,rely=0.6,anchor=CENTER)
lucky_friend1.place(relx=0.5,rely=0.7,anchor=CENTER)

root.mainloop()


