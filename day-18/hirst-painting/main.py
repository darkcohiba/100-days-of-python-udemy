import colorgram
#
# colors = colorgram.extract('~/desto', 10)
new_colors = colorgram.extract("image.jpg", 100)

print(new_colors)
colors_arr = []
for color in new_colors:
    color_tup = (color.rgb[0], color.rgb[1], color.rgb[2])
    print(color_tup)
    colors_arr.append(color_tup)

print (colors_arr)
# import random
# import turtle as turtle_module

# tim = turtle_module.Turtle()
# turtle_module.colormode(255)
# color_list = [(61, 48, 52), (60, 54, 47), (11, 112, 170), (214, 230, 80), (98, 93, 53), (179, 36, 136), (162, 175, 29), (36, 127, 58), (28, 193, 72), (2, 178, 228)]
# position = tim.position()
# tim.speed("fastest")
# tim.ht()
# tim.penup()
# tim.setheading(225)
# tim.forward(250)
# tim.setheading(0)
# for _ in range(10):
#     for _ in range(10):
#         tim.dot(20, random.choice(color_list))
#         tim.forward(50)
#         position = tim.position()
#         print(position)
#     tim.setposition(position[0] - 500, position[1] + 40)
#     # 347.19

# screen = turtle_module.Screen()
# screen.exitonclick()