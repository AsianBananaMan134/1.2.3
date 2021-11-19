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

#-----the five apples-----
apple_list = []
apple_list_letters = []

letter_list = ["w","a","s","d"]
random_letter = ""

#----- some stuff to know-----
for i in range(5): 
    apple_list.append(trtl.Turtle())
    apple_list_letters.append(rand.choice(letter_list))
#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def draw_apple(i):
  apple_list[(i)].penup() 
  apple_list[i].shape(apple_image) 
  wn.tracer(False) 
  apple_list[i].setx(rand.randint(-175,175))
  apple_list[i].sety(rand.randint(-25,100)) 
  apple_list[i].sety(apple_list[i].ycor()-35) 
  apple_list[i].color("white") 
  apple_list[i].write(apple_list_letters[i],align="center",font=("Arial", 40, "bold")) 
  apple_list[i].sety(apple_list[i].ycor()+35) 
  apple_list[i].showturtle() 
  wn.tracer(True) 

#-----functions-----
def falling_apples(i):
  apple_list[i].penup() 
  apple_list[i].clear() 
  apple_list[i].sety(-150) 
  apple_list[i].hideturtle() 
  draw_apple(i)

def press_w():
  for i in range(5):
    if apple_list_letters[i]:
      falling_apples(i)

def press_a():
  for i in range(5):
    if apple_list_letters[i]:
      falling_apples(i)

def press_s():
  for i in range(5):
    if apple_list_letters[i]:
      falling_apples(i)

def press_d():
  for i in range(5):
    if apple_list_letters[i]:
      falling_apples(i)

for i in range(5):
  draw_apple(i)

#-----function calls-----
wn.onkeypress(press_w, "w")
wn.onkeypress(press_a, "a")
wn.onkeypress(press_s, "s")
wn.onkeypress(press_d, "d")

wn.listen()
wn.mainloop()
