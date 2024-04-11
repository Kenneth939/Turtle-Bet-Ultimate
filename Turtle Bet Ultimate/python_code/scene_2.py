from standard_objects import StandardFrame
from tkinter import *
import data
import scene_3
import pygame


class Scene2(StandardFrame):
    def __init__(self, window: Tk):
        super().__init__(window)

        self.print_frame()

        self.red_turtle_image = PhotoImage(file="../turtle_images/red_turtle.png")
        self.red_button = Button(self.frame, image=self.red_turtle_image, command=self.first_choice)
        self.red_button.place(x=50, y=250)

        self.blue_turtle_image = PhotoImage(file="../turtle_images/blue_turtle.png")
        self.blue_button = Button(self.frame, image=self.blue_turtle_image, command=self.second_choice)
        self.blue_button.place(x=50+550/3, y=250)

        self.yellow_turtle_image = PhotoImage(file="../turtle_images/yellow_turtle.png")
        self.yellow_button = Button(self.frame, image=self.yellow_turtle_image, command=self.third_choice)
        self.yellow_button.place(x=50+1100/3, y=250)

        self.green_turtle_image = PhotoImage(file="../turtle_images/green_turtle.png")
        self.green_button = Button(self.frame, image=self.green_turtle_image, command=self.fourth_choice)
        self.green_button.place(x=600, y=250)

        self.choose_label = Label(self.frame, text="Choose your turtle!", bg="green", font=("Courier", 30))
        self.choose_label.place(x=175, y=100)

        self.notice_label = Label(self.frame, text="(Click on the turtle you want to bet)",
                                  bg="green", font=("Courier", 15))
        self.notice_label.place(x=180, y=150)

    def change_to_scene_3(self):
        self.frame.destroy()
        new_frame = scene_3.Scene3(self.window).frame
        new_frame.tkraise()

    def first_choice(self):
        data.player_choice = 0
        self.change_to_scene_3()

    def second_choice(self):
        data.player_choice = 1
        self.change_to_scene_3()

    def third_choice(self):
        data.player_choice = 2
        self.change_to_scene_3()

    def fourth_choice(self):
        data.player_choice = 3
        self.change_to_scene_3()
