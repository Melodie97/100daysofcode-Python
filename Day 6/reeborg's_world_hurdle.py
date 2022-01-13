#This is the code for reeborg's world hurdle 4
#Here is the link to the page to play the hurdle 4 -- https://reeborg.ca/reeborg.html

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()
    
    while front_is_clear():
        move()
    turn_left()

while not at_goal():
    if wall_in_front():
        jump()
    else:
        move()
