import turtle
# import csv
import pandas


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


# print(answer_state)
# with open("50_states.csv", "r") as cf:
#     data = csv.reader(cf)
#     datas = []
#     lists = []
#     for i in (data):
#         datas.append(i)
#     for i in range(1, len(datas)):
#         lists.append(datas[i])
#     print(lists)

#     for state in lists:
#         if answer_state == state[0]:
#             print(answer_state)

states = pandas.read_csv("50_states.csv")
all_states = states["state"].to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title = f"Guess the State {len(guessed_states)}/ States Correct", prompt = "What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    # if answer_state is one of the states:
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        # if right
        state_data = states[states.state == answer_state]
        t.goto(int(state_data["x"]), int(state_data["y"]))
        # create a turrtle write
        t.write(answer_state)
