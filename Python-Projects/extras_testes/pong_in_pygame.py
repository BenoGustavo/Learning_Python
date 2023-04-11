import pygame

#Initiating pygame

pygame.init()

#Creating the window

WIDTH, HEIGHT = 700, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

#Naming the game

pygame.display.set_caption("Pong in pygame")

FPS = 60

WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

class Paddle:
    COLOR = WHITE

    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))


def draw(win, paddles):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)

    pygame.display.update()

def main():
    run = True
    clock = pygame.time.Clock() #Make the game run at a limited FPS

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH ,HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)

    # GameLoop and window verification
    while run:
        clock.tick(FPS)
        draw(WIN, [left_paddle , right_paddle])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
    pygame.quit()

#Make the program verificate if it is being imported

if __name__ == '__main__':
    main()