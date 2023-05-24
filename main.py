import time
import turtle
import pandas
from scoreboard import ScoreBoard
from highscore import HighScore

# SETTINGS.
FONT = ("Arial", 10, "bold")

# Screen setup.
screen = turtle.Screen()
screen.title("Ghiceste judetul!")
image = "romap_img.gif"
screen.addshape(image)
turtle.shape(image)

# Scoreboard display.
scoreboard = ScoreBoard()

# High score display.
high_score = HighScore()

# CSV edit.
data = pandas.read_csv("judete.csv")
all_data = data.state.to_list()
guess_state = []

# Game.
while len(guess_state) < 41:
    # Display score on the screen.
    scoreboard.clear()
    scoreboard.write(f"Score: \n{len(guess_state)}", font=FONT)

    # Display high score on the screen.
    #score_update = 0
    #if len(guess_state) > score_update:
    #    score_update = len(guess_state)
    #high_score.clear()
    #high_score.write(f"HighScore: \n{score_update}", font=FONT)


    # Display high score.

    # Take user input and display the entry box.
    guess = screen.textinput(title=f"{len(guess_state)}/41",
                             prompt="Ghiceste un judet din Romania:").title()

    # Check if the user input Exit and reveal all the answers.
    if guess == "Exit":
        missing_states = []
        for state in all_data:
            if state not in guess_state:
                missing_states.append(missing_states)
                t = turtle.Turtle()
                t.hideturtle()
                t.penup()
                state_data = data[data.state == state]
                t.goto(int(state_data.x), int(state_data.y))
                t.color("red")
                t.write(state)

        time.sleep(1)
        # Ask user if he wants to play again.
        exit_on = screen.textinput(title="Iesi din aplicatie ?", prompt="Raspunde cu DA sau Nu").lower()
        if exit_on == "da":
            break
        else:
            screen.reset()

    # Check if guess is correct and write it on the map.
    if guess in all_data:
        guess_state.append(guess)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == guess]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(guess)
