# The main file to handle everything
from Map import Map
from Player import Player
import pygame as pg

def draw(win: pg.Surface, map: Map, player: Player):
    map.draw(win),
    player.draw(win)
    pg.display.update()

def main():
    win_size = 400
    win = pg.display.set_mode((win_size, win_size))
    pg.display.set_caption("RayCaster in Python")
    
    fps = 60

    show_main_menu = True
    # draw_call = draw_main_menu

    prog_run = True
    prog_clock = pg.time.Clock()
    map = Map(5, win_size, 5, (0, 0, 0), (255, 255, 255), (128, 128, 128))
    map.map = [
        1, 1, 1, 1, 1,
        1, 0, 0, 0, 1,
        1, 0, 1, 1, 1,
        1, 1, 0, 0, 1,
        1, 1, 1, 1, 1
    ]
    player = Player(win_size, (win_size // 2, win_size // 2), (win_size, win_size), 100, 8, 45, (255, 0, 0), 5)

    last_time = 0

    while prog_run:
        for events in pg.event.get():
            if events.type == pg.QUIT:
                # Exit the loop
                prog_run = False
                break

        # Calculate delta time
        current_time = pg.time.get_ticks()
        delta_time = current_time - last_time
        last_time = current_time

        # if show_main_menu:
        #     draw_main_menu(win)
        # else:
        # Update the player
        player.update(delta_time / 1000) # To convert delta time into seconds

        # Draw the screen
        draw(win, map, player)

        # Limit the fps
        # prog_clock.tick(fps)

if __name__ == "__main__":
    # Initialize pygame
    pg.init()

    # Run the application
    main()

    # Terminate the application
    pg.quit()