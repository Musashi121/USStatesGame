import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

scoreboard = turtle.Turtle()
scoreboard.penup()
scoreboard.hideturtle()


state_data = pandas.read_csv("50_states.csv")
state_names = state_data["state"].to_list()

turtle.shape(image)

correct_answers = 0
correct_states = []


def write_state_name(state):
    guess = state_data[state_data.state == state]
    coor_x = int(guess["x"])
    coor_y = int(guess["y"])
    scoreboard.goto(coor_x, coor_y)
    scoreboard.write(f"{state}")


while correct_answers < 50:
    answer_state = screen.textinput(f"{correct_answers}/50 States Correct", "What's another State? ")
    answer_state = answer_state.title()
    if answer_state == "Exit":
        new_data = pandas.DataFrame(state_names)
        new_data.to_csv("States to Learn.csv")
        break
    elif answer_state in state_names:
        state_names.remove(answer_state)
        correct_states.append(answer_state)
        write_state_name(answer_state)
        correct_answers += 1



