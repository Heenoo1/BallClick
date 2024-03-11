from threading import Thread
import turtle
import random

sc = turtle.Screen()
sc.setup(width=1000, height=1000)
sc.bgcolor("light blue")



turtle.hideturtle()


def draw_border():
    border = turtle.Turtle()
    border.penup()
    border.speed("fastest")
    border.color("white")
    border.goto(-sc.window_width() / 2, -sc.window_height() / 2)
    border.pendown()    
    border.pensize(3)
    for _ in range(4):
        border.forward(sc.window_width() if _ % 2 == 0 else sc.window_height())
        border.left(90)

draw_border()


class Circle:
    def __init__(self):
        self.circle = turtle.Turtle()
        self.circle.penup()
        self.circle.speed(0)
        self.circle.shape("circle")
        self.circle.color("black")
        self.circle.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.move_to_random_position()
        self.circle.onclick(self.hide)

        
    
        

    def move_to_random_position(self):
        self.circle.goto(random.randint(-sc.window_width() // 2 + 50, sc.window_width() // 2 - 50),
                         random.randint(-sc.window_height() // 2 + 50, sc.window_height() // 2 - 50))

    def hide(self, x, y):
        self.circle.hideturtle()
        circles.remove(self)
        if not circles:
            add_new_circles()  
            if not timer_started:
                start_timer()




def add_new_circles():
    global circles
    circles = [Circle() for _ in range(3)]


def play_time(time_left):
    turtle.clear()
    turtle.penup()
    turtle.goto(0, sc.window_height() // 2 - 50)  
    turtle.write(time_left, align="center", font=("Arial", 20, "normal"))
    if time_left > 0:
        turtle.ontimer(lambda: play_time(time_left - 1), 1000)

        
def one_more_time():
    global play_more
    if play_more == "y":
        add_new_circles()
        start_timer()
        on_screen_click()
    


      
def start_timer():
    global timer_started
    timer_started = True
    play_time(20) 
    

# Event handler for clicking on the screen
def on_screen_click(x, y):
    for circle in circles:
        if circle.circle.distance(x, y) < 20:
            circle.hide(x, y)
            break


            
        



sc.listen()
turtle.onkeypress(one_more_time, "y")
turtle.onscreenclick(on_screen_click)

timer_started = False
# Initialize circles
circles = [Circle() for _ in range(3)]




turtle.mainloop()
