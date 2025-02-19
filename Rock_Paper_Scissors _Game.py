import tkinter as tk
import random

player_score = 0
computer_score = 0
wins_required = 3  
total_series = 3  
player_series_wins = 0
computer_series_wins = 0

def determine_winner(player_choice):
    global player_score, computer_score, player_series_wins, computer_series_wins
    choices = ["Rock", "Paper", "Scissors"]
    computer_choice = random.choice(choices)
    
    result = ""
    if player_choice == computer_choice:
        result = "It's a Tie!"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Paper" and computer_choice == "Rock") or \
         (player_choice == "Scissors" and computer_choice == "Paper"):
        result = "You Win!"
        player_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1
    
    result_label.config(text=f"Computer chose: \n\n**{computer_choice}**\n\n{result}")
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")
    
    if player_score == wins_required:
        player_series_wins += 1
        player_score, computer_score = 0, 0
        result_label.config(text="Congratulations! You won this series!")
    elif computer_score == wins_required:
        computer_series_wins += 1
        player_score, computer_score = 0, 0
        result_label.config(text="Computer won this series! Try again.")
    
    series_score_label.config(text=f"Series Wins - Player: {player_series_wins} | Computer: {computer_series_wins}")
    
    if player_series_wins == total_series:
        result_label.config(text="You won the entire match series!")
    elif computer_series_wins == total_series:
        result_label.config(text="Computer won the entire match series!")

def new_game():
    global player_score, computer_score, player_series_wins, computer_series_wins
    player_score = 0
    computer_score = 0
    player_series_wins = 0
    computer_series_wins = 0
    result_label.config(text="")
    score_label.config(text=f"Player: {player_score} | Computer: {computer_score}")
    series_score_label.config(text=f"Series Wins - Player: {player_series_wins} | Computer: {computer_series_wins}")


root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("400x400")


heading_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16, "bold"))
heading_label.pack(pady=10)


series_label = tk.Label(root, text=f"First to {wins_required} wins a series! First to {total_series} series wins the match!", font=("Arial", 12))
series_label.pack()


frame = tk.Frame(root)
frame.pack(pady=10)

rock_button = tk.Button(frame, text="Rock", font=("Arial", 12), command=lambda: determine_winner("Rock"))
paper_button = tk.Button(frame, text="Paper", font=("Arial", 12), command=lambda: determine_winner("Paper"))
scissors_button = tk.Button(frame, text="Scissors", font=("Arial", 12), command=lambda: determine_winner("Scissors"))

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

result_label = tk.Label(root, text="", font=("Arial", 14), fg="blue")
result_label.pack(pady=10)

score_label = tk.Label(root, text=f"Player: {player_score} | Computer: {computer_score}", font=("Arial", 12, "bold"))
score_label.pack()


series_score_label = tk.Label(root, text=f"Series Wins - Player: {player_series_wins} | Computer: {computer_series_wins}", font=("Arial", 12, "bold"))
series_score_label.pack()


new_game_button = tk.Button(root, text="New Game", font=("Arial", 12), command=new_game)
new_game_button.pack(pady=10)

root.mainloop()
