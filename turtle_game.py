# Turtle game using the package 'turtle'

# Import relevant modules
import turtle
import random
import time

# Setting up a nice screen for our game
screen = turtle.Screen()
screen.bgcolor('pink') # Background colour

# We want two players and that whoever gets to the other sinde wins.

# Player one set up
player_one = turtle.Turtle()
# Colour of player one
player_one.color('red')
# Make this player a turtle
player_one.shape('turtle')

# Player two set up
player_two = player_one.clone()
player_two.color('green')

# Let's position our players
player_one.penup()     # line will be removed
player_one.goto(-300,200)
player_two.penup()
player_two.goto(-300,-200)

# Let's draw a finish line
player_one.goto(300,-250)
player_one.left(90)
player_one.pendown()
player_one.color('black')
player_one.forward(500)
player_one.write('Finish', font=24)

# go back to the first place
player_one.penup()
player_one.color('red')
player_one.goto(-300,200)
player_one.right(90)

# We need to make sure both players have their pens down
player_one.pendown()
player_two.pendown()

# Let's create values for the die
die = [1,2,3,4,5,6]

# Create the game

for i in range(30):  # put number high enough so turtle reach the finish line
    if player_one.pos() >= (300,250):
        print("Player One wins the race!")
        break
    elif player_two.pos() >= (300, -250):
        print("Player Two wins the race!")
        break
    else:
        die_roll = random.choice(die)
        player_one.forward(30*die_roll)
        time.sleep(1)  #player moves and sleep for one second
                        #to make it a bit slower
        die_roll2 = random.choice(die)
        player_two.forward(30 * die_roll2)
        time.sleep(1)


# this keeps the turtle drawing on the screen
turtle.done()