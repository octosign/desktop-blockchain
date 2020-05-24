from tkinter.ttk import Style
from tkinter import *

class Prompt():
    """Graphical prompt to retrieve info from the user"""

    def __init__(self):
        self.root = Tk()
        self.name = StringVar()
        self.address = StringVar()
        self.key = StringVar()
        self.confirmed = False
        self.error_label = None

        s = Style().theme_use('vista')

    def confirm(self):
        """Confirms prompt if all fields are filled"""
        if len(self.name.get()) == 0 or len(self.address.get()) == 0 or len(self.key.get()) == 0:
            self.error_label.pack()
        else:
            self.confirmed = True
            self.root.destroy()

    def get_data(self):
        """Get filled in data

        Returns dictionary if filled, otherwise None.
        """

        if self.confirmed == False:
            return None

        return {
            'name': self.name.get(),
            'address': self.address.get(),
            'key': self.key.get(),
        }

    def show(self):
        """Show the prompt"""

        self.root.geometry('512x172')
        self.root.title('Details prompt')

        nameLabel = Label(self.root, text='Your name')
        nameLabel.pack()

        nameEntry = Entry(self.root, textvariable=self.name, width=30)
        nameEntry.pack()

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

        self.error_label = Label(self.root, text='You need to fill all fields', fg='red')
        self.error_label.pack_forget()

        self.root.mainloop()
