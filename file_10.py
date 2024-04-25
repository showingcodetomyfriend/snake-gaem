import pygame
import random
#supercool gaem#
# Initialize pygame
pygame.init()

# Set up the screen
screen_width = 600
screen_height = 400
cell_size = 20
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Define directions
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

# Snake class
class Snake:
    def __init__(self):
        self.length = 1
        self.positions = [(screen_width // 2, screen_height // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def move(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = (((cur[0] + (x * cell_size)) % screen_width), (cur[1] + (y * cell_size)) % screen_height)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()

    def reset(self):
        self.length = 1
        self.positions = [(screen_width // 2, screen_height // 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0], p[1]), (cell_size, cell_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, BLACK, r, 1)

# Food class
class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()

    def randomize_position(self):
        self.position = (random.randint(0, screen_width - cell_size) // cell_size * cell_size,
                         random.randint(0, screen_height - cell_size) // cell_size * cell_size)

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (cell_size, cell_size))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, BLACK, r, 1)

# Main function
def main():
    running = True
    snake = Snake()
    food = Food()

    clock = pygame.time.Clock()

    while running:
        screen.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    snake.turn(UP)
                elif event.key == pygame.K_DOWN:
                    snake.turn(DOWN)
                elif event.key == pygame.K_LEFT:
                    snake.turn(LEFT)
                elif event.key == pygame.K_RIGHT:
                    snake.turn(RIGHT)

        snake.move()
        if snake.get_head_position() == food.position:
            snake.length += 1
            food.randomize_position()

        snake.draw(screen)
        food.draw(screen)

        pygame.display.flip()
        clock.tick(10)

    pygame.quit()

if __name__ == "__main__":
    main()
