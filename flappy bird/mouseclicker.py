import pygame as p
import sys

# Initialize Pygame
p.init()

# Constants
screen_width = 800
screen_height = 600

# Create the screen
screen = p.display.set_mode((screen_width, screen_height))
p.display.set_caption("Mouse Click Detection")

# Main game loop
running = True
clock = p.time.Clock()

while running:
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False
        elif event.type == p.MOUSEBUTTONDOWN:
            # Print mouse click coordinates
            print(f"Mouse Click at ({event.pos[0]}, {event.pos[1]})")

    screen.fill((0, 0, 0))

    p.display.flip()
    clock.tick(60)

# Quit pygame properly
p.quit()
sys.exit()
