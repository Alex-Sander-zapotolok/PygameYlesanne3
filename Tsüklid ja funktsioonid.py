import pygame
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Ruudud Pygameis')

# Function to draw the grid
def draw_grid(square_size, rows, cols, line_color):
    for row in range(rows):
        for col in range(cols):
            # Calculate the position of the square
            x = col * square_size
            y = row * square_size
            # Draw the square
            pygame.draw.rect(screen, line_color, pygame.Rect(x, y, square_size, square_size), 1)

# Main game loop
def main():
    # Parameters
    rows = 24  # Number of rows
    cols = 32  # Number of columns
    square_size = min(screen_width // cols, screen_height // rows)  # Calculate square size to fit the screen
    line_color = (255, 0, 0)  # Line color (red)

    # Main loop to keep the game window running
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the screen with light green
        screen.fill((144, 238, 144))

        # Call the function to draw the grid
        draw_grid(square_size, rows, cols, line_color)

        # Update the display
        pygame.display.flip()

    # Quit Pygame
    pygame.quit()
    sys.exit()

# Start the game
if __name__ == "__main__":
    main()
