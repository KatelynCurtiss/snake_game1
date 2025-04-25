# Katelyn Curtiss
# Snake Game
import pygame
import sys
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TITLE = "Snake Game"
CELL_SIZE = 10 
BG = (255, 200, 150) 
RED = (255, 0, 0) 
BLACK = (0, 0, 0) 
BODY_INNER = (50, 175, 25) 
BODY_OUTER = (100, 100, 200) 
APPLE_COLOR = (255, 0, 0)

FPS = 10 

def draw_snake(screen, snake_pos):
    """
    Draw the snake on the screen using the positions stored in snake_pos.
    Each segment of the snake is represented by a rectangle.
    The head of the snake is drawn in RED to distinguish it from the green body.
    """
    index = 0 
    for segment in snake_pos:

        pygame.draw.rect(screen, BODY_OUTER, (segment[0], segment[1], CELL_SIZE, CELL_SIZE))
        if index == 0:

        pygame.draw.rect(screen, RED, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))
32 else: # Body of the snake
33 # Draw the inner rectangle with the body color (green)
34 pygame.draw.rect(screen, BODY_INNER, (segment[0] + 1, segment[1] + 1, CELL_SIZE - 2, CELL_SIZE - 2))

35 index += 1
36
37 # Function to draw the apple on the screen
38 def draw_apple(screen, apple_pos):
39 # The apple is a small rectangle placed at its position on the grid
40 pygame.draw.rect(screen, APPLE_COLOR, (apple_pos[0], apple_pos[1], CELL_SIZE, CELL_SIZE))
41
42 # Function to draw the current score on the screen
43 def draw_score(screen, score, font):
44 # Render the score text
45 score_text = font.render(f"Score: {score}", True, BLACK)
46 # Draw the score text at the top-left corner of the screen
47 screen.blit(score_text, [10, 10])
48
49 # Main function to run the Snake game
50 def run_snake_game():
51 # Initialize the game window
52 screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
53 pygame.display.set_caption(TITLE) # Set the title of the game window
54 clock = pygame.time.Clock() # Create a clock object to control the frame rate
55
56 direction = 1 # Initial direction of the snake (1=Up, 2=Right, 3=Down, 4=Left)
57 score = 0 # Initialize the score
58 snake_pos = [[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2)]] # Initial position of the snake's head
59 # Add body segments to the snake
60 snake_pos.extend([[int(SCREEN_WIDTH / 2), int(SCREEN_HEIGHT / 2) + CELL_SIZE * i] for i in range(1, 4)])
61 apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
62 random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE] # Random position for the apple
63 font = pygame.font.SysFont(None, 35) # Font used for displaying the score
64
65 try:
66 # Attempt to load and play background music
67 pygame.mixer.music.load('background_music.mp3')
68 pygame.mixer.music.set_volume(0.5) # Set the music volume
69 pygame.mixer.music.play(-1) # Play the music in a loop
70 except pygame.error as e:
71 # Handle the error if the background music file is not found or cannot be played

72 print(f"Error loading or playing music in Snake game: {e}")
73
74 running_game = True # Variable to control the main game loop
75 while running_game:
76 screen.fill(BG) # Fill the screen with the background color
77 draw_apple(screen, apple_pos) # Draw the apple
78 draw_score(screen, score, font) # Draw the score
79 draw_snake(screen, snake_pos) # Draw the snake
80
81 # Handle user input (keyboard events)
82 for event in pygame.event.get():
83 if event.type == pygame.QUIT:
84 running_game = False # Exit the game if the user closes the window
85 elif event.type == pygame.KEYDOWN:
86 # Change the direction of the snake based on user input
87 new_direction = direction
88 if event.key == pygame.K_UP and direction != 3: new_direction = 1
89 elif event.key == pygame.K_RIGHT and direction != 4: new_direction = 2
90 elif event.key == pygame.K_DOWN and direction != 1: new_direction = 3
91 elif event.key == pygame.K_LEFT and direction != 2: new_direction = 4
92 direction = new_direction
93
94 # Update the snake's position
95 head_x, head_y = snake_pos[0] # Get the current position of the snake's head
96 if direction == 1: head_y -= CELL_SIZE # Move up
97 elif direction == 2: head_x += CELL_SIZE # Move right
98 elif direction == 3: head_y += CELL_SIZE # Move down
99 elif direction == 4: head_x -= CELL_SIZE # Move left
100
101 snake_pos.insert(0, [head_x, head_y]) # Add the new head position to the snake
102
103 # Check for collision between snake and apple
104 if snake_pos[0] == apple_pos:
105 while apple_pos in snake_pos:
106 # Reposition the apple to a random location that is not inside the snake
107 apple_pos = [random.randint(0, SCREEN_WIDTH // CELL_SIZE - 1) * CELL_SIZE,
108 random.randint(0, SCREEN_HEIGHT // CELL_SIZE - 1) * CELL_SIZE]

109 score += 1 # Increment the score
110 else:
111 snake_pos.pop() # Remove the last segment of the snake
112
113 # If the snake's head collides with the walls or itself, end the game
114 if head_x < 0 or head_x >= SCREEN_WIDTH or head_y < 0 or head_y >= SCREEN_HEIGHT or snake_pos[0] in
snake_pos[1:]:
115 running_game = False # Exit the game loop
116
117 pygame.display.flip() # Update the display
118 clock.tick(FPS) # Limit frame rate to 10 updates per second
119
120 pygame.mixer.music.stop() # Stop the background music
121
122 def main_menu():
123 # Initialize the menu window
124 screen_width = 800
125 screen_height = 600
126 screen = pygame.display.set_mode((screen_width, screen_height))
127 pygame.display.set_caption("Main Menu")
128 font = pygame.font.SysFont("Arial", 40)
129 button_color = (100, 100, 200)
130 text_color = (255, 255, 255)
131
132 # Define the "PLAY" button
133 play_button_rect = pygame.Rect(0, screen_height // 3, 200, 50)
134 play_button_rect.centerx = screen_width // 2 # Center the button horizontally
135 play_text = font.render("PLAY", True, text_color) # Create the button text
136 play_text_rect = play_text.get_rect(center=play_button_rect.center) # Center the text inside the button
137
138 # Define the "EXIT" button
139 exit_button_rect = pygame.Rect(0, screen_height // 2, 200, 50)
140 exit_button_rect.centerx = screen_width // 2 # Center the button horizontally
141 exit_button_rect.y = screen_height // 2 + 20 # Adjust vertical position
142 exit_text = font.render("EXIT", True, text_color) # Create the button text
143 exit_text_rect = exit_text.get_rect(center=exit_button_rect.center) # Center the text inside the button
144

145 running_menu = True # Variable to control the menu loop
146 while running_menu:
147 screen.fill((50, 50, 50)) # Fill the screen with a dark background
148
149 pygame.draw.rect(screen, button_color, play_button_rect) # Draw the "PLAY" button
150 screen.blit(play_text, play_text_rect) # Draw the "PLAY" button text
151
152 pygame.draw.rect(screen, button_color, exit_button_rect) # Draw the "EXIT" button
153 screen.blit(exit_text, exit_text_rect) # Draw the "EXIT" button text
154
155 for event in pygame.event.get():
156 if event.type == pygame.QUIT:
157 running_menu = False # Exit the menu if the user closes the window
158 if event.type == pygame.MOUSEBUTTONDOWN:
159 if event.button == 1: # Check for left mouse button click
160 mouse_pos = pygame.mouse.get_pos() # Get the position of the mouse click
161 if play_button_rect.collidepoint(mouse_pos): # Check if "PLAY" button was clicked
162 run_snake_game() # Start the Snake game
163 elif exit_button_rect.collidepoint(mouse_pos): # Check if "EXIT" button was clicked
164 running_menu = False # Exit the menu
165
166 pygame.display.flip() # Update the display
167
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    pygame.init() 
    pygame.mixer.init() 
    main_menu()