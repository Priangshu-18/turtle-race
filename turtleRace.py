from turtle import Turtle, Screen
import random

#Function to set-up the screen
def setup_screen():
    screen = Screen()
    screen.title("Turtle Race Game")
    screen.setup(width=600, height=400)
    return screen

# Function to draw start and finish lines
def draw_track_line(x_pos):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(x=x_pos, y=-150)
    line.setheading(90)
    line.pensize(3)
    line.pendown()
    line.forward(300)

# Function to create turtle racers with different colors and positions
def create_turtles(colors):
    turtles = []
    y_start = -100
    spacing = 40
    for index, color in enumerate(colors):
        racer = Turtle(shape="turtle")
        racer.color(color)
        racer.penup()
        racer.goto(x=-280, y=y_start + index * spacing)
        turtles.append(racer)
    return turtles

def start_race(turtles, user_bet):
    while True:
        for turtle in turtles:
            distance = random.randint(0, 10)
            turtle.forward(distance)
            if turtle.xcor() >= 270:
                return turtle.pencolor()

def main():
    colors = ["red", "yellow", "blue", "green", "purple", "orange", "black"]
    screen = setup_screen()

    draw_track_line(-280)
    draw_track_line(270)

    turtles = create_turtles(colors)

    user_bet = screen.textinput(
        title="Place Your Bet",
        prompt=f"Which turtle will win the race? Choose from: {', '.join(colors)}"
    )

    if user_bet not in colors:
        screen.bye()
        print("Invalid color entered. Please restart and choose a valid turtle color.")
        return

    winner_color = start_race(turtles, user_bet)

    if winner_color == user_bet:
        print(f"🎉 You won! The {winner_color} turtle is the winner!")
    else:
        print(f"😞 You lost. The {winner_color} turtle won the race.")

    screen.exitonclick()

if __name__ == "__main__":
    main()
