import os
import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

class TodoList(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Dimzy -- To-Do List")
        self.geometry("570x570")
        self.config(bg='#e5eb34')

        # Create a folder for saving files in the home directory
        self.save_folder = os.path.join(os.path.expanduser("~"), "DimzyToDoList")
        os.makedirs(self.save_folder, exist_ok=True)

        self.tasks = []

        tk.Label(text='Dimzy TODO-LIST', pady=5, font=("Helvetica 20 bold"), borderwidth=2, relief='raised', fg='black', bg='#eb9b34').pack(pady=17)

        self.task_entry = tk.Entry(self, width=50)
        self.task_entry.place(x=100, y=70)

        tk.Label(text='Task: ', pady=3, padx=5, font=("Helvetica 13 bold"), borderwidth=2, relief='ridge', fg='black', bg='#eb9b34').place(y=67, x=25)


        add_button = tk.Button(self, text="Add Task", command=self.add_task)
        add_button.place(x=20, y=110)

        delete_button = tk.Button(self, text="Delete Task", command=self.delete_task)
        delete_button.place(y=110, x=120)

        delete_all_button = tk.Button(self, text="Delete All", command=self.confirm_delete_all_task)
        delete_all_button.place(y=110, x=240)

        save_button = tk.Button(self, text="Save Tasks", command=self.save_tasks)
        save_button.place(y=110, x=350)

        open_button = tk.Button(self, text="Open Tasks", command=self.open_tasks)
        open_button.place(y=110, x=460)

        self.task_list = tk.Listbox(self, height=20, width=65, highlightthickness=1)
        self.task_list.place(y=150, x=15)

        self.total_task_label = tk.Label(self, text="Total Tasks: 0", font=("Helvetica", 12), fg="black", bg='#e5eb34')
        self.total_task_label.place(x=20, y=520)

        self.check_button = tk.Button(self, text="Check Task", command=self.check_task)
        self.check_button.place(y=520, x=435)

        self.update_tasks()

    def confirm_delete_all_task(self):
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete all tasks?"):
            self.delete_all_task()

    def delete_all_task(self):
        self.tasks.clear()
        self.update_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.update_tasks()
            self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            task_index = self.task_list.curselection()[0]
            del self.tasks[task_index]
            self.update_tasks()
        except IndexError:
            pass

    def update_tasks(self):
        self.task_list.delete(0, tk.END)
        for i, task_info in enumerate(self.tasks):
            task = task_info["task"]
            completed = task_info["completed"]
            check_text = "✔️" if completed else ""
            self.task_list.insert(tk.END, f"{i+1}. {task} {check_text}")

        total_tasks = len(self.tasks)
        self.total_task_label.config(text=f"Total Tasks: {total_tasks}")

    def save_tasks(self):
        file_path = filedialog.asksaveasfilename(initialdir=self.save_folder, defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for task_info in self.tasks:
                    task = task_info["task"]
                    completed = task_info["completed"]
                    file.write(f"{task},{completed}\n")
            messagebox.showinfo("Save", "Tasks saved successfully.")

    def open_tasks(self):
        file_path = filedialog.askopenfilename(initialdir=self.save_folder, filetypes=[("Text files", "*.txt")])
        if file_path:
            self.tasks.clear()
            with open(file_path, "r") as file:
                for line in file:
                    task, completed_str = line.strip().split(",")
                    completed = completed_str == "True"
                    self.tasks.append({"task": task, "completed": completed})
            self.update_tasks()

    def check_task(self):
        task_number = simpledialog.askinteger("Check Task", "Enter the task number to mark as completed:")
        if task_number and 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.update_tasks()

if __name__ == "__main__":
    app = TodoList()
    app.mainloop()
