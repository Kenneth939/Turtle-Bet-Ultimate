import data
from standard_objects import StandardFrame
from tkinter import *
import scene_2
import pygame


pygame.mixer.init()
pygame.mixer_music.load("../background_music/background_music.mp3")
pygame.mixer_music.play(loops=-1)


class Scene1(StandardFrame):

    def __init__(self, window: Tk):
        super().__init__(window)
        self.print_frame()

        for index in range(0, 4):
            if index < 2:
                self.turtle_object_semi_list[index].canvas.place(x=100, y=100 * (index + 1))
            else:
                self.turtle_object_semi_list[index].canvas.place(x=650, y=100 * (index - 1))

            self.turtle_object_semi_list[index].turtle.setheading(90)

        self.welcome_label = Label(self.frame, text="Welcome to\nTURTLE BET", bg="green", font=("Courier", 50))
        self.welcome_label.place(x=200, y=100)

        self.press_space_label = Label(self.frame, text="Press any Key to continue", bg="green", font=("Courier", 20))
        self.press_space_label.place(x=200, y=400)

        self.frame.focus_set()
        self.frame.bind("<Key>", self.change_to_scene_2)

    def change_to_scene_2(self, event):
        self.frame.destroy()
        new_frame = scene_2.Scene2(self.window).frame
        new_frame.tkraise()
