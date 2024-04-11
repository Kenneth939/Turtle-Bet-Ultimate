from tkinter import *
import data
from standard_objects import StandardFrame
import scene_2
import pygame


class Scene9(StandardFrame):
    def __init__(self, window: Tk):
        super().__init__(window)
        self.print_frame()
        if data.champion != data.player_choice:
            self.lose_label = Label(self.frame, bg="green", text="YOU LOSE!", font=("Courier", 100))
            self.lose_label.place(x=75, y=150)
        else:
            self.lose_label = Label(self.frame, bg="green", text="YOU WIN!", font=("Courier", 100))
            self.lose_label.place(x=100, y=150)

        self.play_again_label = Label(self.frame, bg="green", text="Do you want to play again?", font=("Courier", 20))
        self.play_again_label.place(x=200, y=300)
        self.yes_image = PhotoImage(file="../yes_no_images/yes.png")
        self.no_image = PhotoImage(file="../yes_no_images/no.png")
        self.yes_button = Button(self.frame, image=self.yes_image, highlightthickness=0, command=self.change_to_scene_2)
        self.no_button = Button(self.frame, image=self.no_image, highlightthickness=0, command=self.end_program)
        self.yes_button.place(x=200, y=350)
        self.no_button.place(x=515, y=350)

    def end_program(self):
        self.window.destroy()

    def change_to_scene_2(self):
        self.frame.destroy()
        pygame.mixer_music.fadeout(1000)
        self.frame.after(1000, pygame.mixer_music.load("../background_music/background_music.mp3"))
        pygame.mixer_music.play()
        new_frame = scene_2.Scene2(self.window).frame
        new_frame.tkraise()
