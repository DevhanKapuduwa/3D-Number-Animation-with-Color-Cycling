import pygame # Importing Pygame module
import random 
import math 
import colorsys 

# Defining the characters and their respective 2D representations
characters = {
    '0': ['1'*15]*5 + ['1'*5 + ' '*5 + '1'*5]*15 + ['1'*15]*5,
    '1': ['1'*5]*25,
    '2': ['1'*15]*5 + [' '*10 + '1'*5]*5 + ['1'*15]*5 + ['1'*5 + ' '*10]*5 + ['1'*15]*5,
    '3': ['1'*15]*5 + [' '*10 + '1'*5]*5 + ['1'*15]*5 + [' '*10 + '1'*5]*5 + ['1'*15]*5,
    '4': ['1'*5 + ' '*10]*5 + ['1'*5 + ' '*5 + '1'*5]*5 + ['1'*15]*5 + [' '*10 + '1'*5]*10,
    '5': ['1'*15]*5 + ['1'*5 + ' '*10]*5 + ['1'*15]*5 + [' '*10 + '1'*5]*5 + ['1'*15]*5,
    '6': ['1'*15]*5 + ['1'*5 + ' '*10]*5 + ['1'*15]*5 + ['1'*5 + ' '*5 + '1'*5]*5 + ['1'*15]*5,
    '7': ['1'*15]*5 + [' '*10 + '1'*5]*20,
    '8': ['1'*15]*5 + ['1'*5 + ' '*5 + '1'*5]*5 + ['1'*15]*5 + ['1'*5 + ' '*5 + '1'*5]*5 + ['1'*15]*5,
    '9': ['1'*15]*5 + ['1'*5 + ' '*5 + '1'*5]*5 + ['1'*15]*5 + [' '*10 + '1'*5]*5 + ['1'*15]*5,
}

# Initialization of pygame
pygame.init()

# Defining the window size
window_w = 600 # Width
window_h = 600 # Height

# Create the window
window = pygame.display.set_mode((window_w, window_h))
pygame.display.set_caption("3D Number Animation")

# Defining the rotation speeds. should adjust to get a smooth flow
r_speed_x = random.uniform(0.005, 0.01) #rotation speed about x axis
r_speed_y = random.uniform(0.005, 0.01) #rotation speed about y axis
r_speed_z = random.uniform(0.005, 0.01) #rotation speed about z axis

# Getting number from user
in_num = input("Enter a numerical value between 0 and 9: ")

# Initialize rotation angles
angle_x = 0
angle_y = 0
angle_z = 0

# Main loop
running = True
paused = False
clock = pygame.time.Clock()

hue = 0.0  # Initial hue value for color changing

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                paused = not paused
            elif event.key == pygame.K_RETURN:
                in_num = in_num
                angle_x = 0
                angle_y = 0
                angle_z = 0
        elif event.type == pygame.MOUSEBUTTONDOWN:
            paused = not paused  # Toggle pausing when mouse is clicked

    if not paused:
        # Clearing the screen
        window.fill((255, 255, 255))

        # Rotate the 2D character and draw the 3D representation
        for i, line in enumerate(characters[in_num]):
            for j, char in enumerate(line):
                if char == '1':
                    # Calculate the 3D coordinates based on the rotation angles
                    x = j - len(line) / 2
                    y = i - len(characters[in_num]) / 2
                    z = 0

                    # Rotating around the x-axis
                    y_rotated = y * math.cos(angle_x) - z * math.sin(angle_x)
                    z_rotated = y * math.sin(angle_x) + z * math.cos(angle_x)

                    # Rotating around the y-axis
                    x_rotated = x * math.cos(angle_y) + z_rotated * math.sin(angle_y)
                    z_rotated = -x * math.sin(angle_y) + z_rotated * math.cos(angle_y)

                    # Rotating around the z-axis
                    x_rotated_final = x_rotated * math.cos(angle_z) - y_rotated * math.sin(angle_z)
                    y_rotated_final = x_rotated * math.sin(angle_z) + y_rotated * math.cos(angle_z)

                    # Converting the 3D coordinates to 2D screen coordinates
                    scale = 10
                    x_screen = int(x_rotated_final * scale + window_w / 2)
                    y_screen = int(y_rotated_final * scale + window_h / 2)

                    # Calculating the color based on hue
                    color = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
                    color = (int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))

                    # Draw the point
                    pygame.draw.line(window, color, (x_screen, y_screen), (x_screen + 20, y_screen + 20))

        # Update the rotation angles
        angle_x += r_speed_x
        angle_y += r_speed_y
        angle_z += r_speed_z

        # Update the hue
        hue += 0.005

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the program
pygame.quit()