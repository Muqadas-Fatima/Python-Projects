# Write your code here :-)
from tkinter import *
import tkinter.messagebox as tmsg
from PIL import Image, ImageTk

class User(Tk):

    def __init__(self):
        super().__init__()
# interface
        color="white"
        self.geometry("670x680")
        self.configure(bg="white")
        self.title("USER INFO")

# frame
        self.frm = Frame(self, relief="sunken", bg=color)
        self.frm.pack(side="top", fill="x", padx=10, pady=5,ipady=50)

# name label
        self.name_label = Label(
            self.frm, text="Enter  your  name : ", font=("Helvetica 10 bold"), bg=color
        )
        self.name_label.grid(row=0, column=0, padx=10,ipady=30)

# entry box for name
        self.name = StringVar()
        self.e1 = Entry(self.frm, text=self.name,relief="sunken",borderwidth=2)
        self.e1.grid(row=0, column=1, pady=10, ipadx=25, ipady=10)

# age label
        self.age_label = Label(
            self.frm, text="Choose  your  age  : ", font=("Helvetica 10 bold"), bg=color
        )
        self.age_label.grid(row=3, column=0, pady=15)

# spin box for age
        self.spin_box = Spinbox(self.frm,from_=0, to=100,width=2,borderwidth=2)
        self.spin_box.grid(row=3, column=1, pady=15, ipadx=25, ipady=14)


# gender label
        self.gender_label = Label(
            self.frm, text="Choose  your  gender : ", font=("Helvetica 10 bold"), bg=color
        )
        self.gender_label.grid(row=5, column=0, pady=10)
        self.gender = IntVar()

# check button for gender
        self.choice1 = Checkbutton(self.frm, text="Male",  font=("Helvetica 10 bold"),borderwidth=2,bg=color,variable=self.gender, onvalue=1, offvalue=0)
        self.choice1.grid(row=5, column=1, ipadx=10, ipady=2)
        self.choice2 = Checkbutton(self.frm, text="Female", font=("Helvetica 10 bold"),borderwidth=2, bg=color,variable=self.gender, onvalue=0, offvalue=1)
        self.choice2.grid(row=6, column=1, ipadx=10, ipady=2)

# height label
        self.height_label = Label(
            self.frm, text="Choose  your  height (ft,inches) : ", font=("Helvetica 10 bold"), bg=color
        )
        self.height_label.grid(row=9, column=0, pady=15)

# spin box for height in ft
        self.spin_box1 = Spinbox(self.frm,from_=1 , to=10,borderwidth=2)
        self.spin_box1.grid(row=9, column=1, pady=10, ipadx=25, ipady=14, padx=5)


# spin box for height in inchs
        inch_values = [str(i / 10) for i in range(0, 50)]
        self.spin_box2 = Spinbox(self.frm,values=inch_values,borderwidth=2)
        self.spin_box2.grid(row=9, column=2, pady=6, ipadx=25, ipady=14, padx=5)



# weight label

        self.weight_label = Label(
            self.frm, text="Enter  your  weight (kg) : ", font=("Helvetica 10 bold"), bg=color
        )
        self.weight_label.grid(row=10, column=0, padx=10, pady=20)

# entry box for weight label
        self.weight = DoubleVar()
        self.e2 = Entry(self.frm, textvariable=self.weight,relief="sunken",borderwidth=2)
        self.e2.grid(row=10, column=1, pady=25, ipadx=20, ipady=10,padx=20)


# Button to submit and validate age consent
        self.submit_button = Button(self,text="Submit",font=("Helvetica 10 bold"), command=self.validate_age_consent,bg="#4CAF50",relief="raised")
        self.submit_button.pack(side="bottom", anchor="se",ipady=10,ipadx=15 ,padx=20,pady=5)
        # activity level label
        self.activity=Label(
            self.frm, text="Choose your activity level : ", font=("Helvetica 10 bold"), bg=color
        )
        self.activity.grid(row=11, column=0, padx=10, pady=10)

# radio button for activity level
        self.activity_level = StringVar()
        self.c1 = Radiobutton(self.frm, text="Sedentry",  font=("Helvetica 10 bold"),bg=color,value="Sedentry",variable= self.activity_level,borderwidth=2)
        self.c1.grid(row=11, column=1, ipadx=10, ipady=2)
        self.c2 = Radiobutton(self.frm, text="Lightly active", font=("Helvetica 10 bold"), bg=color,value="Lightly active",variable= self.activity_level,borderwidth=2)
        self.c2.grid(row=12, column=1, ipadx=10, ipady=2)
        self.c3 = Radiobutton(self.frm, text="Moderately Active", font=("Helvetica 10 bold"), bg=color,value="Moderately Active",variable= self.activity_level,borderwidth=2)
        self.c3.grid(row=13, column=1, ipadx=10, ipady=2)
        self.c4 = Radiobutton(self.frm, text="Very Active", font=("Helvetica 10 bold"), bg=color,value="Very Active",variable= self.activity_level,borderwidth=2)
        self.c4.grid(row=14, column=1, ipadx=10, ipady=2)

    def validate_age_consent(self):

        age=int(self.spin_box.get())
        height_ft = int(self.spin_box1.get())
        height_inch =float( self.spin_box2.get())
        weight = int(self.weight.get())
        activity=self.activity_level.get()
        if age < 18:
            tmsg.showinfo("Consent", "Need your parents' consent!")
        else:
            height_m = (height_ft * 0.3048) + (height_inch * 0.0254)
            bmi = weight / (height_m ** 2)

            self.show_bmi_window(bmi,activity)

#creates new window
    def show_bmi_window(self, bmi,activity):
        new_window = BMI(bmi,activity)
        new_window.mainloop()

# class for BMI WINDOW
class BMI(Toplevel):

    def __init__(self,bmi,activity):
        super().__init__()
# interface
        color="white"
        self.geometry("720x680")
        self.configure(bg=color)
        self.title("USER INFO")
# Label for app name
        self.app_name_label = Label(self, text="Balanced Bite", font=("Helvetica 19 bold"), bg=color)
        self.app_name_label.pack(pady=5)
# label for Summary
        self.L1=Label(self,text="Your Summary",font=("Helvetica 19 bold"),bg=color)
        self.L1.pack(pady=3)
        self.scale =Scale(self,from_=0,to=100,orient='horizontal',label="Body Mass Index (BMI)",resolution=2,length=400,width=25,activebackground="lightgreen",bg='light blue',fg='black',font=("Helvetica,15,bold"))
        self.scale.pack(pady=30)
        self.scale.set(bmi)


# showing label according TO BMI
        if bmi < 18.5:
            self.L3=Label(self,text=f'You are under weight!',font=("Helvetica 12 bold"),bg=color,fg="green")
            self.L3.pack(pady=3)
            self.L4=Label(self,text=f'(Focus on increasing muscle mass and strength.',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L4.pack(pady=3)
            self.L5=Label(self,text=f'Ensure a balanced diet to gain healthy weight.)',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L5.pack(pady=3)
        elif 18.5 <= bmi <= 24.9:
            self.L3=Label(self,text=f'You have a normal weight!',font=("Helvetica 12 bold"),bg=color,fg="green")
            self.L3.pack(pady=3)
            self.L4=Label(self,text=f'(Maintain a balanced diet and regular exercise regimen',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L4.pack(pady=3)
            self.L5=Label(self,text=f'to keep your weight stable and stay healthy.)',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L5.pack(pady=3)
        elif 25 <= bmi <= 29.9:
            self.L3=Label(self,text=f'You are over weight!',font=("Helvetica 12 bold"),bg=color,fg="green")
            self.L3.pack(pady=3)
            self.L4=Label(self,text=f'(Focus on losing weight through a combination of diet and ',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L4.pack(pady=3)
            self.L5=Label(self,text=f'exercise to reduce the risk of developing obesity-related conditions.)',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L5.pack(pady=3)
        elif bmi >= 30:
            self.L3=Label(self,text=f'You are obesed!',font=("Helvetica 12 bold"),bg=color,fg="green")
            self.L3.pack(pady=3)
            self.L4=Label(self,text=f'(Seek medical advice for a comprehensive weight-loss program, ',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L4.pack(pad=3)
            self.L5=Label(self,text=f'including diet changes and increased physical activity.)',fg="red",font=("Helvetica 12 bold"),bg=color)
            self.L5.pack(pady=3)
# label for user activity level
        self.L2=Label(self,text=f'Your activity_level is : {activity}',font=("Helvetica 12 bold"),bg=color,fg="Blue")
        self.L2.pack(pady=13)

# button for continue
        self.b=Button(self,text="Continue",font=("Helvetica 12 bold"), command=self.continue_button,bg="#4CAF50",relief="raised")
        self.b.pack(ipady=5, ipadx=50,pady=5)


# function to show message when continue is clicked
    def continue_button(self):
        tmsg.showinfo("Balanced Bite", "Thanks for using us!")
        tmsg.askquestion("Balanced Bite","Do you want diet plans")



if __name__ == "__main__":
    window = User()
    window.mainloop()
