from tkinter.ttk import *
from tkinter import Tk, StringVar  

class prompt():
    def __init__(self):
        self.root = Tk()
        self.address = StringVar()
        self.key = StringVar()

        s = Style().theme_use('vista')

    def confirm(self):
        print(self.address.get())
        print(self.key.get())
        self.root.quit()

    def show(self):
        self.root.geometry('512x128')
        self.root.title('Details prompt')

        addressLabel = Label(self.root, text='Your Address')
        addressLabel.pack()

        addressEntry = Entry(self.root, textvariable=self.address, width=60)
        addressEntry.pack()

        privateKeyLabel = Label(self.root, text='Your Private Key')
        privateKeyLabel.pack()

        privateKeyEntry = Entry(self.root, textvariable=self.key, show='*', width=60)
        privateKeyEntry.pack()

        confirmButton = Button(self.root, text='Confirm', command=self.confirm)
        confirmButton.pack()

        self.root.mainloop()
