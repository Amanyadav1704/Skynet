# here we have define a function named as tkinter. here * has special meaning,
# it means that import everything which are present in tkinter.
from tkinter import *
# here we have imported messagebox from tkinter.
# Now you think that why we need to import messagebox because you have said that
# we have imported everything. So the easiest answer is that the author of 
# tkinter decided that importing "*" wouldn't import messagebox, or some of the
# other packages(ttk is another example).
from tkinter import messagebox
# we simply use this to display the root window and manages all the other components 
# of the tkinter application.
root = Tk()
# here we have given the title of our root window.
root.title('Welcome to Skynet')
# Now simply we change the preset colour system of tkinter application.
text = Text(root,bg='yellow', fg='green')
# Here we have bind our Widget upto column occupied by our widget.
# Now you will ask what is Widget??
# Wiget is an element of a graphical user interface that displays information 
# or provides a specific way for a user to interact with the operating system
# or an application.
# Here is another defination of Widget: Widgets are something like elements in
# HTML(HyperText Markup Language).You will find different type of widgets to the 
# different type of HTML in tkinter.
text.grid(row=0,column=0,columnspan=3)
# This is another widget.we use this widget in our proceding code.
e = Entry(root,width=80)
# Now we have bind our Entry widget.
e.grid(row=4,column=0)

# Now we have made an send function.Now we perform our next thing under this function.
def send():
    # Now we input something in our predefined Button widget .
    send = "You:"+ e.get()
    text.insert(END,"\n" + send)
    # Now we check different different possible permutations which can be possible.
    # for example in this line we simply start simple coversation with out GUI.
    # If we say hi or we gives "hi" input, we get "Hello,how may i help you" as
    # an output. 
    if(e.get()=='hi'):
        text.insert(END, "\n" + "Skynet: hello, how may I help you?")
    # I don't think i have to explain this line. Simply here we check different 
    # type i which a men can say hello.
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Skynet: hi there, what can I do for you?")
    # Same think is happening in this line as done in previous line.
    elif(e.get()=='hey'):
        text.insert(END, "\n" + "Skynet: hey there, what can I do for you?")
    # Again the same thing.
    elif(e.get()=='hello'):
        text.insert(END, "\n" + "Skynet: hi")
    # Now we come to our main point,we only treat 2 main point or question 
    # which is generally asked by people before buying any car.
    # First question is that "What is the value of car", and second one is 
    # "What is the average".
    # Now this is the obvious question that is asked by user that i want to buy a car.
    elif(e.get()=='i want to buy a car'):
        # Here we define another widget named as Label Widget.It only enter the 
        # text which we entered in this widget.
        label=Label(root,text="Enter your budget")
        # Here we define its position on the screen.
        label.grid(column=0,row=0)
        # Now we define again an Entry widget. In simple worlds the use of it is only
        # to make a blank box in which our user input his budget.
        # So we will take input in which we ask the our user to input the budget,
        # so that we can fetch the our result and make the list of only those cars
        # which comes in that range or we say that whose price is less than or equal
        # to the budget of our user in last.
        a=Entry(root)
        # This line is used here to define the position of a.
        a.grid(column=1,row=0) 
        # Now we made another Label widget to ask our 2nd question.
        # So our next question is that "What should be the milage of the car you
        # want".So from the list which we made by using the 1st question, we suggest 
        # our user the best car for him/her in last.
        label1=Label(root,text="Enter your preffered milage")
        # Again here we define the postion of our label1 variable.
        # it should we remeber that we made label,label1 variable using the Label
        # Widget.
        label1.grid(column=0,row=1)
        # Again we define another variable using the Entry widget who takes the 
        # input for milage.
        b=Entry(root)
        # in this line we define the position of variable b.
        b.grid(column=1,row=1)        
        
        # Now we made another function inside the previous function as well as in
        # the above defined elif condition because we want that this all thing 
        # happen only when user ask our skynet that he/she wants to buy a car.
        # we use this function so that now we check the input given by our user.
        def clicked():
            # Now the very main thing is come, the a and b whoom we defined earlier
            # is in string form and we have to convert it into integer form because
            # we can't use < or > or = condition between string and integer.  
            t1=int(a.get())
            t2=int(b.get())
            # Now we check different different pemutations with the user input.
            # fro example if user give the buget less than 5lakh and milage less
            # than 20 then our softwear give him result as "Maruti Eeco".
            if t1<=500000 and t2<=20:
                # Here message is another type of widget which only print or show our
                # result in seeperate window.
                messagebox.showinfo('Your match','Maruti Eeco')
            # Same thing...
            elif t1<=500000 and t2>20:
                messagebox.showinfo('Your match','Renault Kwid')
            # Same thing...
            elif t1<=500000 and t2>30:
                messagebox.showinfo('Your match','Bajaj Qute')
            # Same thing...
            elif t1<=1000000 and t2<=20:
                messagebox.showinfo('Your match','Tata Nexon')
            # Same thing...
            elif t1<=1000000 and t2>20:
                messagebox.showinfo('Your match','Maruti Swift')
            # Same thing...
            elif t1<=1500000 and t2<=16:
                messagebox.showinfo('Your match','Mahindra Thar')
            # Same thing...
            elif t1<=1500000 and t2>16:
                messagebox.showinfo('Your match','Hyundai creata')
            # Same thing...
            elif t1<=2000000 and t2<=15:
                messagebox.showinfo('Your match','Mahindra XUV700')
            # Same thing...
            elif t1<=2000000 and t2>15:
                messagebox.showinfo('Your match','Tata Harrier')
            # Sme thing...
            elif t1<=3500000 and t2<=15:
                messagebox.showinfo('Your match','Innova Crysta')
            # Same thing...
            elif t1<=3500000 and t2>15:
                messagebox.showinfo('Your match','Hyundai alcazar')
            # Sme thing...
            elif t1<=5000000 and t2<=15:
                messagebox.showinfo('Your match','Toyota Fortuner')
            # Same thing...
            elif t1<=5000000 and t2>15:
                messagebox.showinfo('Your match','Mercedes Benz GLA200')
            
        # Now as we know when user gives the input, he has to confirm that yes 
        # i finalize my input.
        # So to do so, we made a button using the Button widget, so that when he/she 
        # click on that button he/she got his result.
        mybutton=Button(root,text="Search", command=clicked)
        # In this line we only define the position of our search button.
        mybutton.grid(row=3,column=3)

    # These are another type of question which may be asked by our user or we 
    # use these lines of code to only increase the interection between and user
    # and GUI.
    elif(e.get()=='100000'):
        text.insert(END, "\n" + "Skynet: buy a maruti")
    elif (e.get() == 'how are you?'):
        text.insert(END, "\n" + "Skynet: i'm fine and you?")
    elif (e.get() == "i'm fine too"):
        text.insert(END, "\n" + "Skynet: nice to hear that")
    elif(e.get()=='bye'):
        text.insert(END, "\n" + "Skynet: bye, have a nice day")  
    elif(e.get()=='thanks'):
        text.insert(END, "\n" + "Skynet: glad I could help you") 
    elif(e.get()=='tell me a joke'):
        text.insert(END, "\n" + "Skynet: what kind of car does yoda drive?  a toyoda")
    else:
        text.insert(END, "\n" + "Skynet: Sorry I didnt get it.")
# we have another button whose use is to take input means when user ask the question's 
# for example "Hello",then user have to fanilize that his question is finished, so have to 
# click on that button so that our skynet can answer his question.
#  Here we have little modify it changing the background as wll as forgroud colour.
send = Button(root,text='Send',bg='deeppink', fg='white', width=20,command=send).grid(row=4,column=1)
# Now we fanilize our code by puting it into mainloop.This line simply means
# that we want that our skynet to run the tkinter event loop.
root.mainloop()