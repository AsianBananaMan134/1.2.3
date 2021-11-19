#   a123_apple_1.py
import turtle as trtl
import random as rand

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

letter_list = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
random_letter = ""

#-----turtle stuff-----
letter.hideturtle()
letter.penup()
apple.penup()
letter.color("white")

#----- some stuff to know-----
new_x = rand.randint(-180,180)
new_y = rand.randint(0,200)
falling = False

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(active_apple):
  active_apple.shape(apple_image)
  wn.update()

#-----functions-----
def falling_apples():
  global falling
  if falling == False:
    falling = True
    letter.clear()
    apple.penup()
    wn.tracer(True)
    apple.goto(apple.xcor(), -200)
    wn.tracer(False)
    apple.hideturtle()
    apple.goto(new_x,new_y)
    apple.showturtle()
    draw_apple(apple)
    write_letter()
    wn.onkeypress(falling_apples, random_letter)
    falling = False

def write_letter():
  global random_letter
  random_letter = letter_list.pop(rand.randint(0, len(letter_list)-1))
  random_letter = rand.choice(letter_list)
  letter.goto(apple.xcor()-18, apple.ycor()-40)
  letter.write(random_letter, font=("Arial", 55, "bold"))

#-----function calls-----
draw_apple(apple)
apple.goto(new_x,new_y)
write_letter()
wn.listen()
wn.onkeypress(falling_apples, random_letter)
wn.mainloop()
