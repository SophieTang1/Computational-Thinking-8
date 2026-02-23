import turtle, math, time, random
from utils import *

# Section 1: Setup
# TODO - create your player character and any other sprites
set_background ("space")
s1 = create_sprite("dogdog",-150,-180)
health = 500
 
sprite_list = []

# Section 2: Controls

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

    if i % 700 == 0: 
        y = random.randint(-300,300)
        item = create_sprite("star (1)", 300,y)
        item.setheading(180)
        sprite_list.append(item)
    for s2 in sprite_list:
        s2 .forward(2)

        if get_distance(s1,s2)<100:
            health -= (5)
            s2.hideturtle()
        
  
    if health <= 100:
        print (f"You died :( health: {health})")
        break 
    
    time.sleep(0.01)
    window.update()
    

	
print("Game Over")