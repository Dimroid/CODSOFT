import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import json

class ContactBook(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Contact Book")
        self.geometry("800x1000")

        self.contacts = []

        self.name_label = tk.Label(self, text="Name:")
        self.name_label.pack()
        self.name_entry = tk.Entry(self)
        self.name_entry.pack()

        self.phone_label = tk.Label(self, text="Phone Number:")
        self.phone_label.pack()
        self.phone_entry = tk.Entry(self)
        self.phone_entry.pack()

        self.email_label = tk.Label(self, text="Email:")
        self.email_label.pack()
        self.email_entry = tk.Entry(self)
        self.email_entry.pack()

        self.address_label = tk.Label(self, text="Address:")
        self.address_label.pack()
        self.address_entry = tk.Entry(self)
        self.address_entry.pack()

        self.add_button = tk.Button(self, text="Add Contact", command=self.add_contact)
        self.add_button.pack(pady=10)

        self.contacts_listbox = tk.Listbox(self, width=30)
        self.contacts_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.contacts_listbox.bind("<<ListboxSelect>>", self.display_contact_details)

        self.details_entry = tk.Entry(self, width=50)
        self.details_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.edit_button = tk.Button(self, text="Edit", command=self.edit_contact)
        self.edit_button.pack(pady=5)

        self.delete_button = tk.Button(self, text="Delete", command=self.delete_contact)
        self.delete_button.pack(pady=5)

        self.search_button = tk.Button(self, text="Search", command=self.search_contact)
        self.search_button.pack(pady=5)

        self.save_button = tk.Button(self, text="Save", command=self.save_contacts)
        self.save_button.pack(pady=5)

        self.open_button = tk.Button(self, text="Open", command=self.open_contacts)
        self.open_button.pack(pady=5)
        

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()
        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.update_contacts_listbox()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Name and phone number are required.")

    def update_contacts_listbox(self):
        self.contacts_listbox.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_listbox.insert(tk.END, contact['name'])

    def display_contact_details(self, event):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            details_text = f"Name: {selected_contact['name']}\n"
            details_text += f"Phone Number: {selected_contact['phone']}\n"
            details_text += f"Email: {selected_contact['email']}\n"
            details_text += f"Address: {selected_contact['address']}"
            self.details_entry.delete(0, tk.END)
            self.details_entry.insert(tk.END, details_text)


    def edit_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            selected_contact = self.contacts[selected_index[0]]
            self.name_entry.delete(0, tk.END)
            self.name_entry.insert(tk.END, selected_contact['name'])
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(tk.END, selected_contact['phone'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(tk.END, selected_contact['email'])
            self.address_entry.delete(0, tk.END)
            self.address_entry.insert(tk.END, selected_contact['address'])

    def delete_contact(self):
        selected_index = self.contacts_listbox.curselection()
        if selected_index:
            del self.contacts[selected_index[0]]
            self.update_contacts_listbox()
            self.clear_entries()

    def search_contact(self):
        search_term = self.name_entry.get().lower()
        found_contacts = [contact for contact in self.contacts if search_term in contact['name'].lower()]
        if found_contacts:
            self.contacts_listbox.delete(0, tk.END)
            for contact in found_contacts:
                self.contacts_listbox.insert(tk.END, contact['name'])
        else:
            messagebox.showinfo("Search", "No contacts found.")

    def save_contacts(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'w') as file:
                json.dump(self.contacts, file)
            messagebox.showinfo("Save", "Contacts saved successfully.")

    def open_contacts(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if filename:
            with open(filename, 'r') as file:
                self.contacts = json.load(file)
            self.update_contacts_listbox()
            messagebox.showinfo("Open", "Contacts loaded successfully.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)


if __name__ == "__main__":
    app = ContactBook()
    app.mainloop()
