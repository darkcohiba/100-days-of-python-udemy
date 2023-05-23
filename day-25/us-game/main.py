import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S States Guessing Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
state_data = pandas.read_csv('50_states.csv')


# my solution
# list_of_states = list(state_data.state)
# while len(list_of_states) > 0:
#
#     # state_data[state_data.state == f"{answer_state}"]
#     # print(list(state_data.state))
#     if answer_state in list_of_states:
#         print(state_data[state_data.state == f"{answer_state}"])
#         list_of_states.remove(answer_state)
#     else:
#         print(f"No State matchs {answer_state}")
#     print(list_of_states)

# angela solution
all_states = state_data.state.to_list()
guessed_states = []
while len(all_states) > 0:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?")
    answer_state = answer_state.title()

    if answer_state in all_states:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state = state_data[state_data.state == f"{answer_state}"]
        t.goto(int(state.x), int(state.y))
        # t.write(answer_state)
        t.write(state.state.item())
        guessed_states.append(answer_state)
        all_states.remove(answer_state)


# def get_mouse_click_coor(x, y):
#     print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
# screen.exitonclick()