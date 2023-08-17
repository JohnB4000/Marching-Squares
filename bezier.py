import pygame, sys
pygame.init()

width = 600
height = 600
fps = 60

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Bezier')

clock = pygame.time.Clock()

screen.fill((255, 255, 255))

p0 = (0, 300)
p1 = (300, 0)
p2 = (600, 300)

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        points = []
        for t in decimal_range(0, 1, 0.01):
            x1 = pygame.math.lerp(p0[0], p1[0], t)
            y1 = pygame.math.lerp(p0[1], p1[1], t)
            x2 = pygame.math.lerp(p1[0], p2[0], t)
            y2 = pygame.math.lerp(p2[1], p2[1], t)
            x = pygame.math.lerp(x1, x2, t)
            y = pygame.math.lerp(y1, y2, t)
            points.append((x, y))
            
        for x in range(len(points) - 1):
            pygame.draw.line(screen, (0, 0, 0), (points[x][0], points[x][1]), (points[x+1][0], points[x+1][1]))

            
    pygame.display.flip()
    clock.tick(fps)