# For loop
# Helpful for iterating order a group of values. Setting ahead of time what the upper limit is.

# While loop
# Number of sequence doesn't matter. Carry out functionality until a condition that was set is fulfilled.
# Will continue running until fulfilled. Can run risk of being an infinite loop. Print condition to troubleshoot while loops.


## While Statement Practice

def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:
    jump()

# Part II
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while at_goal() != True:

    while front_is_clear():
        move()

    while not front_is_clear():
        hurdle()

