import tkinter as tk


# Tk objects to remeber
# Label - For text
# Button
# Entry - single line text entry
# CheckButton - turned on or off
# Listbox - displays a list
# Menu

# Tkk features
# Combobox
# Progress Bar


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title = "Enterm GUI"
        self.geometry("1000x1000")
        self.label = tk.Label(self, text="I love you")
        self.button = tk.Button(self, text="Press the button for a surpise", command=self.action)
        self.button.place(relwidth = .1, relheight = .1, relx = 0.0, rely = 0.0)

        ### Mitm
        # Tk elemaents used for mitm window
        ## Arp Poisonx
        

    def action(self):
        self.label.pack()




GUI().mainloop()