import pygame, sys, marchingSquares
pygame.init()

width = 600
height = 600
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Marching Squares')

clock = pygame.time.Clock()

marchingSquares = marchingSquares.MarchingSquares(screen, pygame.font.Font(None, 16))

screen.fill((255, 255, 255))
marchingSquares.displayPoints()
marchingSquares.displayLinesV2()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    pygame.display.flip()
    clock.tick(fps)