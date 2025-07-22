import turtle  
import random  
import time  

delay = 0.1  
score = 0  
highestscore = 0  

# Creating the body of the snake  
bodies = []  

# Creating the screen  
s1 = turtle.Screen()  
s1.title("Snake Game")  
s1.bgcolor("sky blue")  
s1.setup(width=600, height=600)  

# Create head  
head = turtle.Turtle()  
head.speed(0)  
head.shape("circle")  
head.color("red")  
head.fillcolor("yellow")  
head.penup()  
head.goto(0, 0)  
head.direction = "stop"  

# Create snake food  
food = turtle.Turtle()  
food.speed(0)  
food.shape("circle")  
food.color("brown")  
food.fillcolor("white")  
food.penup()  
food.ht()  # hide turtle  
food.goto(250, 260)  
food.st()  # show turtle  

# Scoreboard  
sb = turtle.Turtle()  
sb.fillcolor("white")  
sb.penup()  
sb.ht()  
sb.goto(-250, 250)  
sb.write(f"score:0 | highest score:0")  

# Movement functions  
def moveup():  
    if head.direction != "down":  
        head.direction = "up"  

def movedown():  
    if head.direction != "up":  
        head.direction = "down"  

def moveleft():  
    if head.direction != "right":  
        head.direction = "left"  

def moveright():  
    if head.direction != "left":  
        head.direction = "right"  

def move():  
    if head.direction == "up":  
        y = head.ycor()  
        head.sety(y + 20)  
    if head.direction == "down":  
        y = head.ycor()  
        head.sety(y - 20)  
    if head.direction == "left":  
        x = head.xcor()  
        head.setx(x - 20)  
    if head.direction == "right":  
        x = head.xcor()  
        head.setx(x + 20)  

# Event handling  
s1.listen()  
s1.onkey(movedown, "Down")  
s1.onkey(moveleft, "Left")  
s1.onkey(moveright, "Right")  
s1.onkey(moveup, "Up")  

# Main loop
try:
  while True:  
    s1.update()  # Update the screen  

    # Check collision with border  
    if head.xcor() > 290:  
        head.setx(-290)  
    if head.xcor() < -290:  
        head.setx(290)  
    if head.ycor() > 290:  
        head.sety(-290)  
    if head.ycor() < -290:  
        head.sety(290)  

    # Check food collision  
    if head.distance(food) < 20:  
        x = random.randint(-290, 290)  
        y = random.randint(-290, 290)  
        food.goto(x, y)  

        # Increase snake size  
        body = turtle.Turtle()  
        body.speed(0)  
        body.penup()  
        body.shape("square")  
        body.color("red")  
        body.fillcolor("black")  
        bodies.append(body)  

        # Increase score  
        score += 10  
        delay -= 0.001  # Decrease delay  

        # Update highest score  
        if score > highestscore:  
            highestscore = score  
        sb.clear()  
        sb.write("score:{} | highestscore:{}".format(score,highestscore))  

    # Move snake body  
    for index in range(len(bodies) - 1, 0, -1):  
        x = bodies[index - 1].xcor()  
        y = bodies[index - 1].ycor()  
        bodies[index].goto(x, y)  

    if len(bodies) > 0:  
        x = head.xcor()  
        y = head.ycor()  
        bodies[0].goto(x, y)  

    move()  

    # Collision with snake body  
    for body in bodies:  
        if body.distance(head) < 20:
            game_over=turtle.Turtle()
            game_over.color("red")
            game_over.penup()
            game_over.ht()
            game_over.goto(0,0)
            game_over.write("GAME OVER",align="center",font=("Arial",24,"bold"))
            time.sleep(1)  
            head.goto(0, 0)  
            head.direction = "stop"  
            # Hide all the body parts  
            for body in bodies:  
                body.ht()  
            bodies.clear()  
            score = 0  
            delay = 0.1  
            sb.clear()  
            sb.write("score:{} | highest score:{}".format(score,highestscore))
            game_over.clear()
    time.sleep(delay)
except turtle.Terminator:
        print("Turtle window closed")


