#Coded By Dimzy (Ukwedje Taiwo Goodness, give credit when modifying)
#Contact me: Ukwedjedimeji@gmail.com
import tkinter as tk
from tkinter import messagebox, simpledialog
from random import randint, choice, shuffle
import pyperclip

class PasswordManager(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dimroid -- Password Manager")
        self.geometry('500x500+500+100')
        self.config(padx=30, pady=20)
        self.resizable(False, False)

        self.canvas = tk.Canvas(height=200, width=200)
        self.logo_img = tk.PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_img)
        self.canvas.pack()

        # Labels
        tk.Label(self, text="Website").place(x=10, y=230)
        tk.Label(self, text="Email/Username").place(x=10, y=265)
        tk.Label(self, text="Password").place(x=10, y=300)

        # Entry
        self.website_entry = tk.Entry(width=35)
        self.website_entry.place(x=135, y=230)
        self.email_entry = tk.Entry(width=35)
        self.email_entry.place(x=135, y=265)
        self.password_entry = tk.Entry(width=35, show="*")
        self.password_entry.place(x=135, y=300)

        # Buttons
        tk.Button(self, relief=tk.RAISED, bd=2, text="Generate Password", font=("Arial 10 bold"), command=self.generate_password).place(x=230, y=365)
        tk.Button(self, relief=tk.RAISED, bd=2, text="Add", width=12, font=("Arial 8 bold"), command=self.save).place(x=80, y=365)
        tk.Button(self, relief=tk.RAISED, bd=2, text="Copy Password", font=("Arial 10 bold"), command=self.copy_password).place(x=295, y=330)
        tk.Button(self, relief=tk.RAISED, bd=2, text="View Details", width=12, font=("Arial 10 bold"), command=self.view_details).place(x=330, y=25)

        self.pin = "1234"  # Set your PIN here

        self.mainloop()

    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_letters = [choice(letters) for _ in range(randint(8, 10))]
        password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
        password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

        password_list = password_letters + password_symbols + password_numbers
        shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.delete(0, tk.END)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if not website or not email or not password:
            messagebox.showerror("Error", "Please fill in all fields.")
            return

        with open("data.txt", 'a') as data_file:
            data_file.write(f"{website} | {email} | {password}\n")

        self.website_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Password saved successfully.")

    def copy_password(self):
        pin = simpledialog.askstring("Input", "Enter PIN to copy password:")
        if pin == self.pin:
            password = self.password_entry.get()
            messagebox.showinfo("Success", f"Password copied to clipboard.")
            pyperclip.copy(password)
        else:
            messagebox.showerror("Error", "Incorrect PIN.")

    def view_details(self):
        pin = simpledialog.askstring("Input", "Enter PIN to copy password:")
        if pin == self.pin:
            website_name = simpledialog.askstring("Input", "Enter website name to view details:")
            with open("data.txt", 'r') as data_file:
                for line in data_file:
                    if website_name in line:
                        details = line.strip().split(" | ")
                        self.website_entry.delete(0, tk.END)
                        self.website_entry.insert(0, details[0])
                        self.email_entry.delete(0, tk.END)
                        self.email_entry.insert(0, details[1])
                        self.password_entry.delete(0, tk.END)
                        self.password_entry.insert(0, details[2])
                        messagebox.showinfo("Details", f"Website: {details[0]}\nEmail/Username: {details[1]}\nPassword: {details[2]}")
                        return
            messagebox.showerror("Error", "Website not found.")
            
        else:
            messagebox.showerror("Error", "Incorrect PIN.")


if __name__ == "__main__":
    app = PasswordManager()
