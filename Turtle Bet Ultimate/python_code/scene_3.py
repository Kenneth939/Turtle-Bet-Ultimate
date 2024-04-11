from standard_objects import StandardFrame, StandardTournamentTreeGUI
from tkinter import *
import scene_4
import data
import pygame


class Scene3(StandardFrame):
    def __init__(self, window: Tk):
        super().__init__(window)

        self.print_frame()

        for participant in self.turtle_object_semi_list:
            participant.turtle.setheading(90)

        self.tournament_tree_GUI = StandardTournamentTreeGUI(self.frame)
        self.tournament_tree_GUI.semi1_turtles[0] = self.turtle_object_semi_list[data.semi1_turtle_indices[0]]
        self.tournament_tree_GUI.semi1_turtles[1] = self.turtle_object_semi_list[data.semi1_turtle_indices[1]]
        self.tournament_tree_GUI.semi2_turtles[0] = self.turtle_object_semi_list[data.semi2_turtle_indices[0]]
        self.tournament_tree_GUI.semi2_turtles[1] = self.turtle_object_semi_list[data.semi2_turtle_indices[1]]
        self.head_label = Label(self.frame, text="SEMI FINAL", bg="green", font=("Courier", 30))
        self.press_label = Label(self.frame, text="(Press any key to start watching your match)", bg="green", font=("Courier", 15))
        self.tournament_tree_GUI.print_tree()
        self.head_label.place(x=280, y=0)
        self.press_label.place(x=150, y=50)

        self.frame.focus_set()
        self.frame.bind("<Key>", self.change_to_scene_4)

    def change_to_scene_4(self, event):
        self.frame.destroy()
        pygame.mixer_music.fadeout(1000)
        new_frame = scene_4.Scene4(self.window).frame
        new_frame.tkraise()
