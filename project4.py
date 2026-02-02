import turtle, time, random
from utils import *

# Section 1 - setup
set_background ("Clouds")
s1 = create_sprite("unicorn",-150,-180)
s2 = create_sprite("realcoco")
mylist = []
mylist.append (s2)
realcoco = 0
hunger = 100 

# OPTIONAL: use this invisible alien to say a message
message_sprite = create_sprite("alien", -250,230)
message_sprite.hideturtle()



# Section 2 - controls
def make_realcoco():
    global realcoco
    realcoco += 1
    x = random.randint(-300,300)
    y = random.randint(-300,300)
    s2 = create_sprite ("realcoco",x,y)
    mylist.append (s2)
def talk():
    s1.write("yay")

window.onkeypress(make_realcoco, "c")
window.onkeypress(talk, "t")
# TODO - make a second control




x1=-300
y1=-100
# Section 3 - game loop
window.listen()
for i in range(1000000000):
    
    # TODO - put any automatic actions here
    if i % 15 == 0:
        hunger -= 1


    for s2 in mylist:
        s2.setheading(270)
        s2.forward (2)
        if get_distance(s1,s2)<100:
            hunger += 25
            s2.hideturtle()
    
    x1 += 2
    s1.goto(x1,y1)
    if x1 >= 300:
        x1 = -300
    if 1 % 10 == s2:
        food -=1 
    # OPTIONAL - use the message sprite to say a message
    message_sprite.clear()
    message_sprite.write(f"hunger {hunger}")


    time.sleep(0.01)
    window.update()