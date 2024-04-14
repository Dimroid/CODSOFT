import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random

class RockPaperScissors(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rock-Paper-Scissors Game")
        self.geometry("450x450+100+50")
        self.result_label = tk.Label(self, text="Enter Your Choice", font=("Helvetica", 12))
        self.result_label.place(y=200, x = 160)
        self.resizable(False, False)
        self.user_score = 0
        self.computer_score = 0
        
        #1
        self.pic = PhotoImage(file='Paper_fist.png')
        self.small_pic = self.pic.subsample(3,3)
        
        self.image_width = Label(image=self.small_pic).place(x=130, y = 110)
         #2
        self.pic2 = PhotoImage(file='Scissors_Fist.png')
        self.small_pic2 = self.pic2.subsample(3,3)
        
        self.image_width2 = Label(image=self.small_pic2).place(x=180, y=10)
        
        #3
        self.pic3 = PhotoImage(file='Folded_Fist.png')
        self.small_pic3 = self.pic3.subsample(3,3)
        
        self.image_width3 = Label(image=self.small_pic3).place(y=130, x = 270)

        self.computer_choice_label = tk.Label(self, text="Computer's Choice:", font=("Helvetica", 10))
        self.computer_choice_label.place(y=250, x=140)
        self.computer_choice_var = tk.StringVar()
        self.computer_choice_entry = tk.Entry(self, textvariable=self.computer_choice_var, state="readonly")
        self.computer_choice_entry.place(y=270, x=140)

        self.user_choice_label = tk.Label(self, text="Your Choice:", font=("Helvetica", 10))
        self.user_choice_label.place(y=320, x=140)
        self.user_choice_var = tk.StringVar()
        self.user_choice_entry = tk.Entry(self, textvariable=self.user_choice_var)
        self.user_choice_entry.place(y=335, x=140)

        self.play_button = tk.Button(self, text="Play", command=self.play_game)
        self.play_button.place(y=370, x = 190)

        self.score_label = tk.Label(self, text="Score: 0", font=("Helvetica", 10))
        self.score_label.place(y=430, x = 140)

    def play_game(self):
        choices = ["rock", "paper", "scissors"]
        computer_choice = random.choice(choices)
        self.computer_choice_var.set(computer_choice)

        user_choice = self.user_choice_var.get().lower()

        if user_choice not in choices:
            self.result_label.config(text="Invalid choice. Please choose rock, paper, or scissors.")
            return

        self.result_label.config(text=f"Computer chose: {computer_choice}. You chose: {user_choice}")

        if user_choice == computer_choice:
            self.result_label.config(text="It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "scissors" and computer_choice == "paper") or \
             (user_choice == "paper" and computer_choice == "rock"):
            self.result_label.config(text="You win!")
            self.user_score += 1
        else:
            self.result_label.config(text="Computer wins!")
            self.computer_score += 1
        
        self.score_label.config(text=f"Score: {self.user_score}")
        
        # Schedule the message box after 2000 milliseconds (2 seconds)
        self.after(300, self.show_message_box)

    def show_message_box(self):
        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if not play_again:
            self.play_button.config(state=tk.DISABLED)
            self.user_choice_entry.config(state=tk.DISABLED)
        if play_again:
            self.user_choice_var.set("")  # Clear the user's choice
            self.computer_choice_var.set("")  # Clear the computer's choice
            

if __name__ == "__main__":
    app = RockPaperScissors()
    app.mainloop()
