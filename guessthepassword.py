import tkinter as tk

class GuessThepasswordGUI:
    def __init__(self, master):
        self.master = master
        master.title("Guess The password!")

        self.password = "password"

        self.password_label = tk.Label(master, text="Enter the password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack()
        self.guess_button = tk.Button(master, text="clickme", command=self.submit)
        self.guess_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def submit(self):
        guess = self.password_entry.get()
        if guess == self.password:
            self.result_label.config(text="You may enter")
        else:
            self.result_label.config(text="wrong password, try again")

root = tk.Tk()
my_gui = GuessThepasswordGUI(root)
root.mainloop()