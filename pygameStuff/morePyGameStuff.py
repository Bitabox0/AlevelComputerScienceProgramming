import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
FPS = 60

# Colors (R, G, B)
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
BG_COLOR = (30, 30, 30)

class MovableCircle:
    def __init__(self, x, y, radius, color, speed):
        # Position (using floats for smoother movement)
        self.x = float(x)
        self.y = float(y)
        self.radius = radius
        self.color = color
        self.speed = speed

    def handle_input(self):
        """Check for key presses and update velocity/position."""
        keys = pygame.key.get_pressed()
        
        # Move Up/Down/Left/Right
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x += self.speed
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y += self.speed

    def constrain_to_screen(self, width, height):
        """Keep the circle inside the window boundaries."""
        if self.x - self.radius < 0:
            self.x = self.radius
        elif self.x + self.radius > width:
            self.x = width - self.radius

        if self.y - self.radius < 0:
            self.y = self.radius
        elif self.y + self.radius > height:
            self.y = height - self.radius

    def draw(self, surface):
        """Draw the circle onto the given surface."""
        # pygame.draw.circle requires integer coordinates
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), self.radius)

def main():
    # Setup screen and clock
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Moveable Circle with Classes - Pygame")
    clock = pygame.time.Clock()

    # Instantiate our circle in the middle of the screen
    player_circle = MovableCircle(
        x=SCREEN_WIDTH // 2, 
        y=SCREEN_HEIGHT // 2, 
        radius=25, 
        color=BLUE, 
        speed=5
    )

    # Main game loop
    while True:
        # 1. Event Handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # 2. Update Game State
        player_circle.handle_input()
        player_circle.constrain_to_screen(SCREEN_WIDTH, SCREEN_HEIGHT)

        # 3. Drawing / Rendering
        screen.fill(BG_COLOR)  # Clear screen with background color
        player_circle.draw(screen)

        # 4. Refresh Display
        pygame.display.flip()
        
        # Limit frame rate to 60 FPS
        clock.tick(FPS)

if __name__ == "__main__":
    main()