from tkinter import *

root = Tk()

count = 0


def counter():
    global count   # defining variable as global to use inside the function
    count += 1
    print(count)


# converting image
image = PhotoImage(file='filepath')

# Mybutton with image
mybtn = Button(root, text="Increment",
               image=image, command=counter,
               font=("Comic Sans", 15),
               fg='green', bg='black',
               state=ACTIVE, compound=BOTTOM)

mybtn.pack
root.mainloop()
