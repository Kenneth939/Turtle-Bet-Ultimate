from tkinter import *
from standard_objects import StandardFrame, StandardTurtleObjectGUI
import data
import random
import scene_5
import pygame


class Scene4(StandardFrame):
    def __init__(self, window: Tk):
        super().__init__(window)

        #initialization
        self.print_frame()

        #Setup countdown labels
        self.label_3 = Label(self.frame, text="3", bg="white", font=("Courier", 50))
        self.label_2 = Label(self.frame, text="2", bg="white", font=("Courier", 50))
        self.label_1 = Label(self.frame, text="1", bg="white", font=("Courier", 50))
        self.label_go = Label(self.frame, text="GO!", bg="white", font=("Courier", 50))
        self.label_finished = Label(self.frame, text="FINISHED!", bg="white", font=("Courier", 50))

        # Load stand images and create canvases for displaying these images
        upper_stand = PhotoImage(file="../stand_image/upper_stand.png")
        self.upper_stand = upper_stand
        lower_stand = PhotoImage(file="../stand_image/lower_stand.png")
        self.lower_stand = lower_stand
        self.upper_stand_canvas = Canvas(self.frame, width=800, height=150, bg="green", highlightthickness=0)
        self.lower_stand_canvas = Canvas(self.frame, width=800, height=150, bg="green", highlightthickness=0)
        self.upper_stand_canvas.create_image(0, 111, anchor=NW, image=self.upper_stand)
        self.lower_stand_canvas.create_image(0, 0, anchor=NW, image=self.lower_stand)
        self.upper_stand_canvas.place(x=0, y=0)
        self.lower_stand_canvas.place(x=0, y=350)

        #when the sounds play
        self.frame.after(1500, self.play_3_2_1_sound)
        self.frame.after(6000, self.play_ingame_music)

        # Decide which turtles from the semifinals advance to the final based on player choices and randomness
        for index in range(0, 2):
            if data.player_choice in data.semi[index]:
                m = random.randint(0, 1)
                data.final_turtle_indices[1 - index] = data.semi[1 - index][m]
                self.turtle_object_semi_list[data.semi[index][0]].canvas.config(width=800, height=100)
                self.turtle_object_semi_list[data.semi[index][1]].canvas.config(width=800, height=100)
                self.turtle_object_semi_list[data.semi[index][0]].turtle.setpos(x=0, y=-25)
                self.turtle_object_semi_list[data.semi[index][1]].turtle.setpos(x=0, y=-25)
                self.turtle_object_semi_list[data.semi[index][0]].canvas.place(x=0, y=150)
                self.turtle_object_semi_list[data.semi[index][1]].canvas.place(x=0, y=250)

                # Create visual markers on the turtle race
                for i in range(0, 7):
                    if i % 2 == 0:
                        self.turtle_object_semi_list[data.semi[index][0]].canvas.create_line(700 + 10 * i, -100,
                                                                                             700 + 10 * i, 100,
                                                                                             fill="black", width=10)
                        self.turtle_object_semi_list[data.semi[index][1]].canvas.create_line(700 + 10 * i, -100,
                                                                                             700 + 10 * i, 100,
                                                                                             fill="black", width=10)

                # Start the countdown and race for this pair of turtles
                self.ready_set_go(5, self.turtle_object_semi_list[data.semi[index][0]],
                                  self.turtle_object_semi_list[data.semi[index][1]], index)

    #play the countdown sound 
    def play_3_2_1_sound(self):
        pygame.mixer_music.load("../background_music/3_2_1_go.mp3")
        pygame.mixer_music.play()

    #play the bcakground sound 
    def play_ingame_music(self):
        pygame.mixer_music.load("../background_music/ingame_music.mp3")
        pygame.mixer_music.play()

    #Transition to the next scene after the race is completed
    def change_to_scene_5(self):
        self.frame.destroy()
        new_frame = scene_5.Scene5(self.window).frame
        new_frame.tkraise()

    # Recursively manage the countdown display and initiate turtle movements after "GO!"
    def ready_set_go(self, time, turtle1: StandardTurtleObjectGUI, turtle2: StandardTurtleObjectGUI, i):
        self.frame.after(1000, self.ready_set_go, time - 1, turtle1, turtle2, i)
        if time > 3:
            pass
        elif 2 < time <= 3:
            self.label_3.place(x=375, y=225)
        elif 1 < time <= 2:
            self.label_3.destroy()
            self.label_2.place(x=375, y=225)
        elif 0 < time <= 1:
            self.label_2.destroy()
            self.label_1.place(x=375, y=225)
        elif -1 < time <= 0:
            self.label_1.destroy()
            self.label_go.place(x=350, y=225)
        else:
            self.label_go.destroy()
            
            # Race logic to move turtles randomly forward ,determine the winner when one turtle crosses the finish line
            if turtle1.turtle.xcor() < 700 and turtle2.turtle.xcor() < 700:
                random_move_1 = random.randint(1, 100)
                random_move_2 = random.randint(1, 100)
                turtle1.turtle.forward(random_move_1)
                turtle2.turtle.forward(random_move_2)
                turtle1.turtle.speed("fastest")
                turtle2.turtle.speed("fastest")

            elif turtle1.turtle.xcor() >= 700:
                self.label_finished.place(x=250, y=225)
                data.final_turtle_indices[i] = data.semi[i][0]
                self.frame.after(5000, self.change_to_scene_5)

            else:
                self.label_finished.place(x=250, y=225)
                data.final_turtle_indices[i] = data.semi[i][1]
                self.frame.after(5000, self.change_to_scene_5)
