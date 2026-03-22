import tkinter as tk
import random

# Choices
choices = ["Stone", "Paper", "Scissor"]

# Scores
player_score = 0
computer_score = 0

def play(user_choice):
    global player_score, computer_score

    computer_choice = random.choice(choices)

    result_text.set(f"You chose: {user_choice}\nComputer chose: {computer_choice}")

    if user_choice == computer_choice:
        result = "It's a Draw!"
    elif (user_choice == "Stone" and computer_choice == "Scissor") or \
         (user_choice == "Scissor" and computer_choice == "Paper") or \
         (user_choice == "Paper" and computer_choice == "Stone"):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    score_text.set(f"Score  You: {player_score}  Computer: {computer_score}")
    winner_text.set(result)

# GUI Setup
root = tk.Tk()
root.title("Stone Paper Scissor Game")
root.geometry("400x400")

title = tk.Label(root, text="Stone Paper Scissor", font=("Arial", 20, "bold"))
title.pack(pady=10)

result_text = tk.StringVar()
winner_text = tk.StringVar()
score_text = tk.StringVar()

result_label = tk.Label(root, textvariable=result_text, font=("Arial", 14))
result_label.pack(pady=10)

winner_label = tk.Label(root, textvariable=winner_text, font=("Arial", 16, "bold"))
winner_label.pack(pady=10)

score_label = tk.Label(root, textvariable=score_text, font=("Arial", 14))
score_label.pack(pady=10)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

stone_btn = tk.Button(button_frame, text="Stone", width=10, height=2, command=lambda: play("Stone"))
paper_btn = tk.Button(button_frame, text="Paper", width=10, height=2, command=lambda: play("Paper"))
scissor_btn = tk.Button(button_frame, text="Scissor", width=10, height=2, command=lambda: play("Scissor"))

stone_btn.grid(row=0, column=0, padx=10)
paper_btn.grid(row=0, column=1, padx=10)
scissor_btn.grid(row=0, column=2, padx=10)

root.mainloop()
