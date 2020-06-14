from tkinter import*
import insertionsort
import time
import random

global entries
entries=[]
for i in range(10):
    entries.append(random.randrange(0, 100))
global risk
risk = []

global n
n='10'


def insertion():

    class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, **kwargs)

            #Setup Frame
            container = Frame(self)
            container.pack(side="top", fill="both", expand=True)
            container.grid_rowconfigure(0, weight=1)
            container.grid_columnconfigure(0, weight=1)

            self.frames = {}
            for F in (PageThree3, byuser):
                frame = F(container, self)
                self.frames[F] = frame
                frame.grid(row=0, column=0, sticky="nsew")
                frame.config(bg="black")

            self.show_frame(PageThree3)


        def show_frame(self, context):
            frame = self.frames[context]
            frame.tkraise()


    class PageThree3(Frame):
        def __init__(self, parent, controller):
            Frame.__init__(self, parent)

            label = Label(self, text="Which type of inputs you prefer to visualise the algorithm:", bg='black', fg='white', font='Georgia 24 bold', pady=15)
            label.pack(padx=10, pady=15)
            page_two = Button(self, text="Default", font='Times 17 bold', padx=30, pady=10, command=insertionsort.insertionsort)
            page_two.pack(pady=10)
            page_three = Button(self, text="By User", font='Times 17 bold', padx=32, pady=10, command=lambda:controller.show_frame(byuser))
            page_three.pack(pady=10)

    class byuser(Frame):
            def __init__(self, parent, controller):
                Frame.__init__(self, parent)
                label = Label(self, text="Enter the number of inputs in the array:", bg='black', fg='white', font='Georgia 24 bold', pady=30)
                label.grid(row=0, column=0)

                entr = Entry(self, width=5, font=('Times', 28))
                entr.grid(row=1, column=0, padx=5, pady=50)

                def input2():
                    global n
                    n = (int(entr.get()))

                def showbox():
                    for widget in self.winfo_children():
                        widget.destroy()
                    x = int(n)
                    label = Label(self, text="Enter the inputs in the array:", bg='black', fg='white', font='Georgia 24 bold', pady=10)
                    label.grid(row=0, columnspan=x)
                    ent20 = []

                    for i in range(0, x):
                        entry = Entry(self, width=2, font=('Times', 28))
                        entry.grid(row=1, column=i, padx=5, pady=10)
                        ent20.append(entry)

                    def input1():
                        for i in range(0, x):
                            risk.append(int(ent20[i].get()))

                    btn = Button(self, text="SUBMIT", font='Times 17 bold', padx=30, pady=10, command=lambda: [input1(), insertionsort.insertionsort()])
                    btn.grid(row=3, columnspan=x, pady=70)

                btn = Button(self, text="SUBMIT", font='Times 17 bold', padx=30, pady=10, command=lambda: [input2(), showbox()])
                btn.grid(row=3, columnspan=5, pady=70)

    app = App()
    app.title("ALGORITHM SIMULATOR")
    app.geometry("1200x700")
    app.resizable(0, 0)
    app.mainloop()

def list():
        if not risk:
            return entries
        else:
            return risk

def num():
        print(n)
        return n