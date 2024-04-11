from tkinter import *
from standard_objects import StandardFrame
import data
import scene_9
import pygame


class Scene8(StandardFrame):
    def __init__(self, window: Tk):
        super().__init__(window)

        self.print_frame()

        for index in range(0, 4):
            if data.champion == index:
                self.turtle_object_champion_list[index].canvas.config(width=200, height=200)
                self.turtle_object_champion_list[index].turtle.goto(x=75, y=-75)
                self.turtle_object_champion_list[index].turtle.shapesize(3, 3)
                self.turtle_object_champion_list[index].canvas.place(x=300, y=200)
                self.turtle_object_champion_list[index].turtle.setheading(90)

        self.head_label = Label(self.frame, bg="green", text="TOURNAMENT'S\nCHAMPION", font=("Courier", 50))
        self.press_label = Label(self.frame, text="Press any Key to continue", bg="green", font=("Courier", 15))
        self.head_label.place(x=150, y=0)
        self.press_label.place(x=250, y=450)
        pygame.mixer_music.load("../background_music/victory_background_music.mp3")
        pygame.mixer_music.play()
        self.frame.focus_set()
        self.frame.bind("<Key>", self.change_to_scene_9)

    def change_to_scene_9(self, event):
        self.frame.destroy()
        new_frame = scene_9.Scene9(self.window).frame
        new_frame.tkraise()
