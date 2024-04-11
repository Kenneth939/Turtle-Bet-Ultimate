from tkinter import *
from standard_objects import StandardFrame, StandardTournamentTreeGUI
import data
import random
import scene_6
import scene_8
import pygame


class Scene5(StandardFrame):
    def __init__(self, window: Tk):
        super().__init__(window)

        self.stop_ingame_music()

        self.print_frame()

        self.frame.after(3000, pygame.mixer_music.load("../background_music/background_music.mp3"))
        pygame.mixer_music.play(loops=-1)

        for participant in self.turtle_object_semi_list:
            participant.turtle.setheading(90)
        for participant in self.turtle_object_final_list:
            participant.turtle.setheading(90)
        for participant in self.turtle_object_champion_list:
            participant.turtle.setheading(90)

        self.tournament_tree_GUI = StandardTournamentTreeGUI(self.frame)
        self.tournament_tree_GUI.semi1_turtles[0] = self.turtle_object_semi_list[data.semi[0][0]]
        self.tournament_tree_GUI.semi1_turtles[1] = self.turtle_object_semi_list[data.semi[0][1]]
        self.tournament_tree_GUI.semi2_turtles[0] = self.turtle_object_semi_list[data.semi[1][0]]
        self.tournament_tree_GUI.semi2_turtles[1] = self.turtle_object_semi_list[data.semi[1][1]]
        self.tournament_tree_GUI.final_turtles[0] = self.turtle_object_final_list[data.final_turtle_indices[0]]
        self.tournament_tree_GUI.final_turtles[1] = self.turtle_object_final_list[data.final_turtle_indices[1]]

        if data.player_choice not in data.final_turtle_indices:
            self.head_label = Label(self.frame, text="RESULT", bg="green", font=("Courier", 30))
            self.press_label = Label(self.frame, text="(Press any key to continue)", bg="green",
                                     font=("Courier", 15))
            data.champion = random.choice(data.final_turtle_indices)
            self.tournament_tree_GUI.champion = self.turtle_object_champion_list[data.champion]
            self.tournament_tree_GUI.print_tree()
            self.head_label.place(x=320, y=0)
            self.press_label.place(x=230, y=50)
            self.frame.focus_set()
            self.frame.bind("<Key>", self.change_to_scene_8)

        else:
            self.head_label = Label(self.frame, text="FINAL", bg="green", font=("Courier", 30))
            self.press_label = Label(self.frame, text="(Press any key to start watching your match)",
                                     bg="green", font=("Courier", 15))
            self.tournament_tree_GUI.print_tree()
            self.head_label.place(x=335, y=0)
            self.press_label.place(x=150, y=50)
            self.frame.focus_set()
            self.frame.bind("<Key>", self.change_to_scene_6)

    def stop_ingame_music(self):
        pygame.mixer_music.fadeout(1000)

    def change_to_scene_6(self, event):
        self.frame.destroy()
        pygame.mixer_music.fadeout(1000)
        new_frame = scene_6.Scene6(self.window).frame
        new_frame.tkraise()

    def change_to_scene_8(self, event):
        self.frame.destroy()
        pygame.mixer_music.fadeout(1000)
        new_frame = scene_8.Scene8(self.window).frame
        new_frame.tkraise()
