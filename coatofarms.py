# Section 1 - Your code
from utils import *
set_background("amsterdam")

s1 = create_sprite("corgi", -260, -100)
s2 = create_sprite("CHINA", -255, 100)
s3 = create_sprite("waterbottle", -100, -100)
s4 = create_sprite("flowers", 100, -150)

message1 = create_sprite("alien",-200,200)
message1.color("blue")
message1.write("Sophie",font = ("Arial", 40, "normal"))
message1.hideturtle()

message2 = create_sprite("alien",-200,-250)
message2.color("black")
message2.write("Your motto",font = ("Arial", 40, "normal"))
message2.hideturtle()


######################################################################


# Section 2 - Keeping the window open (DON'T CHANGE!!)
window.update()
turtle.exitonclick()