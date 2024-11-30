import time
import random
import os

game_map = [
    "...............................................",
    "...............................................",
    "...............................................",
    "...............................................",
    "...............................................",
    "...............................................",
    "...............................................",
    "...............................................",
    "..............................................."
]

player_pos = [4, 10]
items = ['@', '#', '&', '%', '$']
item_positions = []
flame_intensity = 27

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def render_map():
    clear_screen()
    for r, row in enumerate(game_map):
        row_str = list(row)
        if r == player_pos[0]:
            row_str[player_pos[1]] = 'i'
        for pos in item_positions:
            if pos[0] == r:
                row_str[pos[1]] = random.choice(items)
        print("".join(row_str))
    
    print(f"\nFlame intensity: {flame_intensity}")
    print("\nMove with W/A/S/D, or Q to quit.\n")

def place_item():
    row = random.randint(0, len(game_map) - 1)
    col = random.randint(0, len(game_map[0]) - 1)
    while [row, col] == player_pos or [row, col] in item_positions:
        row = random.randint(0, len(game_map) - 1)
        col = random.randint(0, len(game_map[0]) - 1)
    item_positions.append([row, col])

def check_flame_status():
    global flame_intensity
    if flame_intensity <= 0:
        print("\nThe flame fades to nothing. The darkness wins.")
        return True
    elif flame_intensity <= 3:
        print("\nThe flame flickers weakly. Is it better to burn out or let the darkness win?")
    return False

for _ in range(7):
    place_item()

while True:
    render_map()

    if check_flame_status():
        break

    move = input("Enter your move: ").lower()

    if move == 'q':
        print("The flame flickers and dies. You have chosen the darkness.")
        break

    new_pos = player_pos[:]
    if move == 'w':
        new_pos[0] -= 1
    elif move == 's':
        new_pos[0] += 1
    elif move == 'a':
        new_pos[1] -= 1
    elif move == 'd':
        new_pos[1] += 1
    else:
        print("Invalid move. Try again.")
        time.sleep(1)
        continue

    if new_pos[0] < 0 or new_pos[0] >= len(game_map) or new_pos[1] < 0 or new_pos[1] >= len(game_map[0]):
        print("The void blocks your path.")
        time.sleep(1)
        continue

    if new_pos in item_positions:
        flame_intensity = 28
        item_positions.remove(new_pos)
        place_item()

    player_pos = new_pos
    flame_intensity -= 1
    time.sleep(0.5)
