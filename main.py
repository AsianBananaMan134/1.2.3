#   a123_apple_1.py
import turtle as trtl

#-----setup-----
apple_image = "apple.gif" # Store the file name of your shape
pear_image = "pear.gif"

wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file
wn.addshape(pear_image) 
wn.bgpic("background.gif")

apple = trtl.Turtle()
letter = trtl.Turtle()

#----- turtle stuff
letter.hideturtle()
letter.penup()
letter.color("white")

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

#-----functions-----
def falling_apples():
  letter.clear()
  apple.penup()
  wn.tracer(True)
  apple.goto(apple.xcor(), -200)
  wn.tracer(False)

def write_letter():
  letter.goto(apple.xcor()-18, apple.ycor()-40)
  letter.write("A", font=("Arial", 55, "bold"))

#-----function calls-----
draw_apple(apple)
write_letter()
wn.onkeypress(falling_apples, "a")
wn.listen()

wn.mainloop()