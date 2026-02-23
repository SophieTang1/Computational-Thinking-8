import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
set_background ("space")
s1 = create_sprite("dogdog",-150,-180)
s2 = create_sprite("star (1)")
# TODO - set your background
# TODO - set the starting value for your variables
sprite_list = []

# Section 2: Controls
# TODO - define your controls
# TODO - pick keys for each control
def move_up():
    x = s1.xcor()
    y = s1.ycor() + 9
    s1.goto(x,y)
        
def move_down():
    x = s1.xcor()
    y = s1.ycor() - 9
    s1.goto(x,y)
    
def move_left():
    x = s1.xcor() - 9
    y = s1.ycor() 
    s1.goto(x,y)
        
def move_right(): 
    x = s1.xcor() + 9
    y = s1.ycor() 
    s1.goto(x,y)

window.onkeypress(move_up, "w")
window.onkeypress(move_down, "s")
window.onkeypress(move_left, "a")
window.onkeypress(move_right,"d") 



# Section 3: Game Loop
window.listen()
for i in range(10000000000):

    if 1 % 50 == 0: 
        x = random.randint(-300,300)
        item = create_sprite("star(1)", x,200)
        item.setheading(270)
        sprite_list.append(item)
        for item in sprite_list:
            item.forward(5)
    
    # TODO - add code for automatic actions


    # TODO - make an if statement for ending the game

    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")