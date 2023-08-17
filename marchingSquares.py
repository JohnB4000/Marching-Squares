import random, pygame, util


class MarchingSquares():
    def __init__(self, screen: pygame.Surface , font: pygame.font.Font) -> None:
        self.grid = [[random.randint(0, 4) for _ in range(20)] for _ in range(20)]
        self.screen = screen
        self.font = font

    def displayPoints(self) -> None:
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                self.screen.blit(self.font.render(str(self.grid[x][y]), True, (0, 0, 0)), (y*35-15, x*35-15))

    def displayLinesV1(self) -> None:
        for x in range(len(self.grid) - 1):
            for y in range(len(self.grid[x]) - 1):
                topLeft = util.getCoordinate(x, y)
                topRight = util.getCoordinate(x, y+1)
                bottomLeft = util.getCoordinate(x+1, y)
                bottomRight = util.getCoordinate(x+1, y+1)

                a = util.calculateMidpoint(topLeft, topRight)
                b = util.calculateMidpoint(topRight, bottomRight)
                c = util.calculateMidpoint(bottomLeft, bottomRight)
                d = util.calculateMidpoint(topLeft, bottomLeft)

                bitString = [self.grid[x+1][y], self.grid[x+1][y+1], self.grid[x][y+1], self.grid[x][y]]
                value = util.bitString4ToDecimal(bitString)
                
                match value:
                    case 1:
                        util.drawLine(a, d)
                    case 2:
                        util.drawLine(a, b)
                    case 3:
                        util.drawLine(b, d)
                    case 4:
                        util.drawLine(b, c)
                    case 5:
                        util.drawLine(a, b)
                        util.drawLine(d, c)
                    case 6:
                        util.drawLine(a, c)
                    case 7:
                        util.drawLine(d, c)
                    case 8:
                        util.drawLine(d, c)
                    case 9:
                        util.drawLine(a, c)
                    case 10:
                        util.drawLine(a, d)
                        util.drawLine(b, c)
                    case 11:
                        util.drawLine(b, c)
                    case 12:
                        util.drawLine(d, b)
                    case 13:
                        util.drawLine(a, b)
                    case 14:
                        util.drawLine(a, d)
  
    def displayLinesV2(self) -> None:
        for x in range(len(self.grid) - 1):
            for y in range(len(self.grid[x]) - 1):
                topLeft = util.getCoordinate(x, y)
                topRight = util.getCoordinate(x, y+1)
                bottomLeft = util.getCoordinate(x+1, y)
                bottomRight = util.getCoordinate(x+1, y+1)

                a = util.calculateMidpoint(topLeft, topRight)
                b = util.calculateMidpoint(topRight, bottomRight)
                c = util.calculateMidpoint(bottomLeft, bottomRight)
                d = util.calculateMidpoint(topLeft, bottomLeft)

                coords = []

                aPoints = util.calculatePoints(self.grid, (x, y), (x, y+1))
                aMultiCoords = util.calculateMultiLineCoords(aPoints)
                for i in range(len(aMultiCoords)):
                    coords.append((a[0]+aMultiCoords[i], a[1]))
                
                bPoints = util.calculatePoints(self.grid, (x, y+1), (x+1, y+1))
                bMultiCoords = util.calculateMultiLineCoords(bPoints)
                for i in range(len(bMultiCoords)):
                    coords.append((b[0], b[1]+bMultiCoords[i]))

                cPoints = util.calculatePoints(self.grid, (x+1, y), (x+1, y+1))
                cMultiCoords = util.calculateMultiLineCoords(cPoints)
                for i in range(len(cMultiCoords)):
                    coords.append((c[0]+cMultiCoords[i], c[1]))

                dPoints = util.calculatePoints(self.grid, (x, y), (x+1, y))
                dMultiCoords = util.calculateMultiLineCoords(dPoints)
                for i in range(len(dMultiCoords)):
                    coords.append((d[0], d[1]+dMultiCoords[i]))

                points = aPoints + bPoints + cPoints + dPoints
            
                while len(points) > 0:
                    distances = []
                    for k in range(len(points)):
                        if k > 0 and points[0] == points[k]:
                            distances.append(util.calculateDistanceBetweenPoints(coords[0], coords[k]))
                        else:
                            distances.append(9999)
                    min = 9999
                    minIndex = -1
                    for k in range(len(distances)):
                        if distances[k] < min:
                            min = distances[k]
                            minIndex = k
                    util.drawCurve(self.screen, coords[0], coords[minIndex], util.calculateMidpoint(a,c))
                    # util.drawLine(self.screen, coords[0], coords[minIndex])
                    points.pop(0)
                    points.pop(minIndex-1)
                    coords.pop(0)
                    coords.pop(minIndex-1)