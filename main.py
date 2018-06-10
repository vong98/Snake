import pygame
import time
import Snake

def main():
    pygame.init()

    size = width, height = 400, 600

    snake = Snake

    white = (255, 255, 255)
    black = (0, 0, 0)

    mainScr = pygame.display.set_mode(size)

    while True:
        start = time.time()
        
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.draw.rect(mainScr, white, (snake.getX(), snake.getY(), snake.getSize(), snake.getSize()), 0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                event.type=pygame.QUIT
            if event.key == pygame.K_LEFT:
                snake.face(-1, 0)
            if event.key == pygame.K_RIGHT:
                snake.face(1, 0)
            if event.key == pygame.K_UP:
                snake.face(0, 1)
            if event.key == pygame.K_DOWN:
                snake.face(0, -1)
        snake.move()
        pygame.display.update()



main()
