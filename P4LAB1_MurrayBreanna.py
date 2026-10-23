# Breanna Murray
# 10/23/2026
#P4 LAB1
# Use Turtle and loops to draw a square and triangle 


#Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
tommy = turtle.Turtle()

# Set turtle options
tommy.pensize(3)
tommy.color("purple")
tommy.shape("turtle")

# Code to draw the shapes
for side in range(4):
    tommy.forward(100)
    tommy.left(90)


# While loop that executes 3 times to draw a triangle
sides = 3
while sides > 0:
    tommy.forward(100)
    tommy.left(120) 
    sides = sides - 1

   


# Wait for user to close window 
win.mainloop()
