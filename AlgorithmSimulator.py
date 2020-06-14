from tkinter import *
import selection
import insertion
import bubble
import traversal
import insert
import deletion

def home():
	class App(Tk):
		def __init__(self, *args, **kwargs):
			Tk.__init__(self, *args, **kwargs)
			container = Frame(self)
			container.pack(side="top", fill="both", expand=True)
			container.grid_rowconfigure(0, weight=1)
			container.grid_columnconfigure(0, weight=1)
			self.frames = {}
			for F in (StartPage, PageOne, PageTwo):
				frame = F(container, self)
				self.frames[F] = frame
				frame.grid(row=0, column=0, sticky="nsew")
				frame.config(bg="black")
			self.show_frame(StartPage)

		def show_frame(self, context):
			frame = self.frames[context]
			frame.tkraise()


	class StartPage(Frame):
		def __init__(self, parent, controller):

				Frame.__init__(self, parent)
				label = Label(self, text="## WELCOME TO ALGORITHM SIMULATOR ##", bg='black', fg='white', font='Georgia 30 bold underline', pady=50)
				label.pack(padx=10, pady=10)
				label1 = Label(self, text="Select the type of algorithms you wanted to simulate", bg='black', fg='white', font='Georgia 24 bold', pady=10)
				label1.pack(padx=10, pady=10)
				page_one = Button(self, text="Sorting Algorithms", padx=50, pady=20, font='Times 19 bold', command=lambda:controller.show_frame(PageOne))
				page_one.pack(pady=20)
				page_two = Button(self, text="Data-Structures", padx=65, pady=20, font='Times 19 bold', command=lambda:controller.show_frame(PageTwo))
				page_two.pack(pady=20)



	class PageOne(Frame):
		def __init__(self, parent, controller):
			Frame.__init__(self, parent)
			label = Label(self, text="Which sorting you wanted to visualize:", bg='black', fg='white', font='Georgia 24 bold', pady=15)
			label.pack(padx=10, pady=20)
			page_two = Button(self, text="Bubble Sort", font='Times 17 bold', padx=30, pady=10, command=bubble.bubble)
			page_two.pack(pady=10)
			start_page = Button(self, text="Selection Sort", font='Times 17 bold', padx=20, pady=10, command=selection.selection)
			start_page.pack(pady=10)
			page_three = Button(self, text="Insertion Sort", font='Times 17 bold', padx=20, pady=10, command=insertion.insertion)
			page_three.pack(pady=10)
			# page_four = Button(self, text="Merge Sort", font='Times 17 bold', padx=30, pady=10, command=merge.merge)
			# page_four.pack(pady=10)
			page_four = Button(self, text="HOME", font='Times 17 bold', padx=50, pady=10, command=lambda:controller.show_frame(StartPage))
			page_four.pack(pady=50)


	class PageTwo(Frame):
		def __init__(self, parent, controller):
			Frame.__init__(self, parent)
			label = Label(self, text="Which operation do you want to perform on Array", bg='black', fg='white', font='Georgia 24 bold', pady=15)
			label.pack(padx=10, pady=15)
			page_two = Button(self, text="Linear Search", font='Times 17 bold', padx=20, pady=10, command=traversal.traversal)
			page_two.pack(pady=10)
			page_three = Button(self, text="Insertion", font='Times 17 bold', padx=46, pady=10, command=insert.insert)
			page_three.pack(pady=10)
			page_four = Button(self, text="Deletion", font='Times 17 bold', padx=50, pady=10, command=deletion.deletion)
			page_four.pack(pady=10)
			page_four = Button(self, text="HOME", font='Times 17 bold', padx=60, pady=10, command=lambda:controller.show_frame(StartPage))
			page_four.pack(pady=50)




	app = App()
	app.title("ALGORITHM SIMULATOR")
	app.geometry("1200x700")
	app.resizable(0, 0)
	app.mainloop()

home()

