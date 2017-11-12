import tkinter as tk
import tkinter.filedialog, tkinter.messagebox
import os, io

class FixSubs(tk.Frame):
	def __init__(self, master = None):
		super().__init__(master)
		self.master.title("FixSubs")
		self.master.resizable(width = False, height = False)
		self.master.eval('tk::PlaceWindow %s center' % root.winfo_pathname(root.winfo_id()))

		self.createWidgets()

	def createWidgets(self):
		self.menubar = tk.Menu(self.master)

		self.menuFile = tk.Menu(self.menubar, tearoff = 0)
		self.menuFile.add_command(label = "Exit", command = self.master.destroy, font = (None, 10))
		self.menubar.add_cascade(label = "File", menu = self.menuFile, font = (None, 10))

		self.menuHelp = tk.Menu(self.menubar, tearoff = 0)
		self.menuHelp.add_command(label = "About...", command = self.aboutMessage, font = (None, 10))
		self.menubar.add_cascade(label = "Help", menu = self.menuHelp, font = (None, 10))

		self.master.config(menu = self.menubar)

		self.subsLabel = tk.Label(self.master, text = "Choose\nstr file", font = (None, 10))
		self.subsLabel.grid(row = 1, column = 0, padx = 10, pady = 10)
		self.subsValue = tk.StringVar(root, value = 'myFile.str')
		self.subsEntry = tk.Entry(self.master, bd = 2, textvariable = self.subsValue, width = 30, font = (None, 10))
		self.subsEntry.grid(row = 1, column = 1, columnspan = 2, padx = 10, pady = 10)
		self.subsButton = tk.Button(self.master, bd = 2, text = 'Browse', command = self.chooseFile, font = (None, 10))
		self.subsButton.grid(row = 1, column = 3, padx = 10, pady = 10)

		self.master.update()
		self.line1 = tk.Frame(self.master, height = 3, width = self.master.winfo_width(),bg = "grey")
		self.line1.grid(row = 2, columnspan = 4)

		self.fixButton = tk.Button(self.master, bd = 2, text = 'Fix Encoding', command = self.fixEncoding, font = (None, 10))
		self.fixButton.grid(row = 3, column = 1, sticky = tk.E, pady = 10, padx = 5)

		self.exitButon = tk.Button(self.master, bd = 2, text = 'Exit', command = self.master.destroy, font = (None, 10))
		
		self.exitButon.grid(row = 3, column = 2, sticky = tk.W, pady = 10, padx = 5)

	def chooseFile(self):
		self.subsEntry.config(fg = 'black')
		self.subsValue.set(tk.filedialog.askopenfilename(parent = self.master, title = 'Choose a file', filetypes = (("Subs files", "*.srt;*.sub") ,("All files", "*.*") )))
		self.subsEntry.config(fg = 'red')
		

	def aboutMessage(self):
		tk.messagebox.showinfo("About...", "This program lets you fix the\nencoding of cyrillic subtitles.")

	def fixEncoding(self):
		try:
			with io.open(self.subsValue.get(), "r", encoding = "cp1251") as f:
				s = f.read().encode("utf-8")
			if s:
				with open(self.subsValue.get(), "wb") as f:
					f.write(s)
		except UnicodeDecodeError:
			pass
		except FileNotFoundError:
			tk.messagebox.showinfo("Error", "There is no such file.")
			return	
		tk.messagebox.showinfo("Status", "The encoding was set correctly.")
		self.subsEntry.config(fg = 'green')

root = tk.Tk()
app = FixSubs(master = root)
app.mainloop()