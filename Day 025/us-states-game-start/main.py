import pandas as pd
import turtle

# initiate screen
screen = turtle.Screen()
screen.title("U.S. States Game")

image = "/Users/steven.tey/Documents/Python Bootcamp/Day 025/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

answer_df = pd.read_csv("/Users/steven.tey/Documents/Python Bootcamp/Day 025/us-states-game-start/50_states.csv")

is_game_on = True
guess_list = []

while is_game_on:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    # if asnwer state is in answer_df state column, then write the state name on the map
    if answer_state == "Exit":
        # is_game_on = False
        break
    if answer_state in answer_df.state.values and answer_state not in guess_list:
        guess_list.append(answer_state)
        state_data = answer_df[answer_df.state == answer_state]
        state_name = turtle.Turtle()
        state_name.hideturtle()
        state_name.penup()
        state_name.goto(int(state_data.x), int(state_data.y))
        state_name.write(answer_state)
    if len(guess_list) == 50:
        is_game_on = False


new_df = pd.DataFrame([i for i in answer_df.state.values if i not in guess_list]).rename(columns={0: "state"})
new_df.to_csv("states_to_learn.csv")

turtle.mainloop()