import pygame

# Initialize Pygame
pygame.init()

# Define the screen size
width = 500
height = 500

# Create the screen
screen = pygame.display.set_mode((width, height))

# Set the caption for the window
pygame.display.set_caption("Moving Ball")

# Define the colors
white = (255, 255, 255)
red = (255, 0, 0)

# Set the initial position and velocity of the ball
x = width // 2
y = height // 2
velocity = 20

# Define the function to draw the ball
def draw_ball(x, y):
    pygame.draw.circle(screen, red, (x, y), 25)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                y -= velocity
            elif event.key == pygame.K_DOWN:
                y += velocity
            elif event.key == pygame.K_LEFT:
                x -= velocity
            elif event.key == pygame.K_RIGHT:
                x += velocity

    if x < 25:
        x = 25
    elif x > width - 25:
        x = width - 25

    if y < 25:
        y = 25
    elif y > height - 25:
        y = height - 25


    screen.fill(white)

    draw_ball(x, y)

    pygame.display.update()

pygame.quit()