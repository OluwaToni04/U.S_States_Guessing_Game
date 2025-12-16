import turtle as ts
import pandas as pd

image = "blank_states_img.gif"
# Set up the screen
screen = ts.Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
screen.addshape(image)
ts.shape(image)

# Read the states data
data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []
state_number = 50
correct_guesses = 0


while True:
    answer = screen.textinput(title=f"{correct_guesses}/{state_number}Guess the State", prompt="What's another state's name?").title()
    if answer == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer in all_states and answer not in guessed_states:
        guessed_states.append(answer)
        correct_guesses += 1
        state_data = data[data.state == answer]
        ts.penup()
        ts.goto(int(state_data.x), int(state_data.y))
        ts.write(answer, align="center", font=("Arial", 8, "normal"))

    if correct_guesses == state_number:
        ts.penup()
        ts.goto(0, 0)
        ts.write("Congratulations! You guessed all the states!", align="center", font=("Arial", 16, "bold"))
        break







