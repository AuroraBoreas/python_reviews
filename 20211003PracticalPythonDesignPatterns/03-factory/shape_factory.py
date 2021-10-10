import pygame
import abc

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        pass

    def draw(self):
        raise NotImplementedError()

    def move(self, direction:str):
        if direction == 'up':
            self.y -= 4
        elif direction == 'down':
            self.y += 4
        elif direction == 'right':
            self.x += 4
        elif direction == 'left':
            self.x -= 4

    @classmethod
    def factory(cls, type:str):
        if type == 'circle':
            return Circle(100, 100)
        if type == 'square':
            return Square(100, 100)
        assert 0, 'Bad Shape Request: ' + type


class Square(Shape):
    def draw(self):
        pygame.draw.rect(screen, (255,255,0), pygame.Rect(self.x, self.y, 20, 20))

class Circle(Shape):
    def draw(self):
        pygame.draw.circle(screen, (0,255,255), (self.x, self.y), 10)

class AbstractFactory(metaclass=abc.ABCMeta):
    def make_object(self):
        return

class SquareFactory(AbstractFactory):
    def make_object(self):
        return Square()

class CicleFactory(AbstractFactory):
    def make_object(self):
        return Circle()

if __name__ == '__main__':
    pywin = 800, 600
    screen = pygame.display.set_mode(pywin)
    obj = Shape.factory("square")
    player_quits = False
    while not player_quits:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                player_quits = True
            keystroke = pygame.key.get_pressed()
            if keystroke[pygame.K_UP]: obj.move('up')
            if keystroke[pygame.K_DOWN]: obj.move('down')
            if keystroke[pygame.K_RIGHT]: obj.move('right')
            if keystroke[pygame.K_LEFT]: obj.move('left')
            screen.fill((0,0,0))
            obj.draw()
        pygame.display.flip()
