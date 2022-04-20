import turtle
import pandas
screen = turtle.Screen()

screen.title("U.S. States Game")

t = turtle.Turtle()
t.color("red")
t.hideturtle()
t.penup()

score = 0
data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
image = "blank_states_img.gif"
screen.bgpic(image)
# turtle.shape(image)
while score < 50:
    answer_state = screen.textinput(title=f"Guess the State{score}/{len(all_states)}",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
        score += 1
        all_states.remove(answer_state)

    if answer_state == "Exit":
        new_data = pandas.DataFrame(all_states)
        new_data.to_csv("to_learn_states.csv")
        break


t.color("green")
t.goto(x=-365, y=250)
t.write("You guessed all 50 U.S. States!", font=("Courier", 30, "bold"))









