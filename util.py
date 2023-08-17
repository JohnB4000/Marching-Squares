import pygame, math
from typing import Tuple, List


def drawLine(screen: pygame.Surface, point1: Tuple[int, int], point2: Tuple[int, int]) -> None:
    pygame.draw.line(screen, (0, 0, 0), point1, point2)

def decimal_range(start, stop, increment):
    while start < stop:
        yield start
        start += increment

def drawCurve(screen: pygame.Surface, p0: Tuple[int, int], p2: Tuple[int, int], p1: Tuple[int, int]) -> None:
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

def getCoordinate(x: int, y: int) -> Tuple[int, int]:
    return y*35-10, x*35-10

def calculateMidpoint(point1: Tuple[int, int], point2: Tuple[int, int]) -> Tuple[int, int]:
    return (point1[0] + point2[0])/2, (point1[1] + point2[1])/2

def bitString4ToDecimal(string: str) -> int:
    return string[0] * 8 + string[1] * 4 + string[2] * 2 + string[3]

def calculateMultiLineCoords(lines: List[int]) -> List[int]:
    total = len(lines)
    spacing = 5
    coords = []
    numberEachSide = math.floor(total / 2)
    for x in range(numberEachSide):
        middleIndex = int(math.floor(len(coords) / 2))
        coords.insert(middleIndex, spacing if total % 2 != 0 else spacing/2)
        coords.insert(middleIndex, -spacing if total % 2 != 0 else -spacing/2)
        if x != 0:
            leftToAdd = int(len(coords) / 2 - 1)
            for y in range(leftToAdd):
                coords[y] -= spacing
                coords[-y-1] += spacing
    if total % 2 != 0:
        coords.insert(int(math.floor(len(coords) / 2)), 0)
    return coords

def calculateDistanceBetweenPoints(point1: Tuple[int, int], point2: Tuple[int, int]) -> int:
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

def calculatePoints(grid: List[List[int]], point1: Tuple[int, int], point2: Tuple[int, int]) -> List[int]:
    points = []
    for i in range(grid[point1[0]][point1[1]], grid[point2[0]][point2[1]] + 1 if grid[point1[0]][point1[1]] < grid[point2[0]][point2[1]] else -1, 1 if grid[point1[0]][point1[1]] < grid[point2[0]][point2[1]] else -1):
        if i > grid[point2[0]][point2[1]] and grid[point1[0]][point1[1]] > grid[point2[0]][point2[1]]:
            points.append(i-0.5)
        elif i < grid[point2[0]][point2[1]] and grid[point1[0]][point1[1]] < grid[point2[0]][point2[1]]:
            points.append(i+0.5)
        
    return points