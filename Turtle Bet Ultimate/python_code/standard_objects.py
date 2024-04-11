from tkinter import *
from turtle import RawTurtle


class StandardTurtleObjectGUI:
    def __init__(self, frame: Frame, color="black"):
        self.canvas = Canvas(frame)
        self.canvas.config(width=50, height=50, highlightthickness=0)
        self.turtle = RawTurtle(self.canvas)
        self.turtle.shape("turtle")
        self.turtle.color(color)
        self.turtle.penup()
        self.turtle.setpos(x=0, y=0)


class StandardFrame:
    def __init__(self, window: Tk):
        # Window
        self.window = window
        self.window.config(bg="green")
        self.window.title("Turtle Bet")
        self.window.geometry("800x500")

        # Frame
        self.frame = Frame(self.window, bg="green", width=800, height=500, highlightthickness=0)

        # Red Turtle
        self.red_turtle_object_semi = StandardTurtleObjectGUI(self.frame, color="red")
        self.red_turtle_object_final = StandardTurtleObjectGUI(self.frame, color="red")
        self.red_turtle_object_champion = StandardTurtleObjectGUI(self.frame, color="red")
        # Blue Turtle
        self.blue_turtle_object_semi = StandardTurtleObjectGUI(self.frame, color="blue")
        self.blue_turtle_object_final = StandardTurtleObjectGUI(self.frame, color="blue")
        self.blue_turtle_object_champion = StandardTurtleObjectGUI(self.frame, color="blue")

        # Yellow Turtle
        self.yellow_turtle_object_semi = StandardTurtleObjectGUI(self.frame, color="yellow")
        self.yellow_turtle_object_final = StandardTurtleObjectGUI(self.frame, color="yellow")
        self.yellow_turtle_object_champion = StandardTurtleObjectGUI(self.frame, color="yellow")

        # Green Turtle
        self.green_turtle_object_semi = StandardTurtleObjectGUI(self.frame, color="green")
        self.green_turtle_object_final = StandardTurtleObjectGUI(self.frame, color="green")
        self.green_turtle_object_champion = StandardTurtleObjectGUI(self.frame, color="green")

        # List of Turtle
        self.turtle_object_semi_list = [self.red_turtle_object_semi, self.blue_turtle_object_semi,
                                        self.yellow_turtle_object_semi, self.green_turtle_object_semi]
        self.turtle_object_final_list = [self.red_turtle_object_final, self.blue_turtle_object_final,
                                         self.yellow_turtle_object_final, self.green_turtle_object_final]
        self.turtle_object_champion_list = [self.red_turtle_object_champion, self.blue_turtle_object_champion,
                                            self.yellow_turtle_object_champion, self.green_turtle_object_champion]

    def print_frame(self):
        self.frame.place(x=0, y=0)


class StandardTournamentTreeGUI:
    def __init__(self, frame: Frame):
        self.frame = frame
        self.semi1_canvas = Canvas(self.frame, bg="green", height=100, highlightthickness=0)
        self.semi1_canvas.create_line(25, 100, 25, 50, fill="white")
        self.semi1_canvas.create_line(225, 100, 225, 50, fill="white")
        self.semi1_canvas.create_line(25, 50, 225, 50, fill="white")
        self.semi1_canvas.create_line(125, 50, 125, 0, fill="white")
        self.semi1_turtles = [StandardTurtleObjectGUI(self.frame), StandardTurtleObjectGUI(self.frame)]
        for participant in self.semi1_turtles:
            participant.turtle.setheading(90)

        self.semi2_canvas = Canvas(self.frame, bg="green", height=100, highlightthickness=0)
        self.semi2_canvas.create_line(25, 100, 25, 50, fill="white")
        self.semi2_canvas.create_line(225, 100, 225, 50, fill="white")
        self.semi2_canvas.create_line(25, 50, 225, 50, fill="white")
        self.semi2_canvas.create_line(125, 50, 125, 0, fill="white")
        self.semi2_turtles = [StandardTurtleObjectGUI(self.frame), StandardTurtleObjectGUI(self.frame)]
        for participant in self.semi2_turtles:
            participant.turtle.setheading(90)

        self.final_canvas = Canvas(self.frame, bg="green", height=100, highlightthickness=0)
        self.final_canvas.create_line(25, 100, 25, 50, fill="white")
        self.final_canvas.create_line(375, 100, 375, 50, fill="white")
        self.final_canvas.create_line(25, 50, 375, 50, fill="white")
        self.final_canvas.create_line(200, 50, 200, 0, fill="white")
        self.final_turtles = [StandardTurtleObjectGUI(self.frame), StandardTurtleObjectGUI(self.frame)]

        for participant in self.final_turtles:
            participant.turtle.setheading(90)

        self.champion = StandardTurtleObjectGUI(self.frame)
        self.champion.turtle.setheading(90)

    def print_tree(self):
        self.semi1_canvas.place(x=100, y=300)
        self.semi2_canvas.place(x=450, y=300)
        self.final_canvas.place(x=200, y=150)
        self.semi1_turtles[0].canvas.place(x=100, y=400)
        self.semi1_turtles[1].canvas.place(x=300, y=400)
        self.semi2_turtles[0].canvas.place(x=450, y=400)
        self.semi2_turtles[1].canvas.place(x=650, y=400)
        self.final_turtles[0].canvas.place(x=200, y=250)
        self.final_turtles[1].canvas.place(x=550, y=250)
        self.champion.canvas.place(x=375, y=100)
