import random


player_choice = None
participants_indices = [0, 1, 2, 3]
shuffled_indices = list(participants_indices)
random.shuffle(shuffled_indices)
semi1_turtle_indices = [shuffled_indices[0], shuffled_indices[1]]
semi2_turtle_indices = [shuffled_indices[2], shuffled_indices[3]]
semi = [semi1_turtle_indices, semi2_turtle_indices]
final_turtle_indices = [0, 0]
champion = 0
