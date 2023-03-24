import pygame
import random
import colorswatch as cs
import pyautogui

SCREEN_X = 640
SCREEN_Y = 480
SCREEN = (SCREEN_X, SCREEN_Y)
FPS = 60
BG_COLOR = cs.black["pygame"]
ROOT = pygame.display.set_mode(SCREEN)
CLOCK = pygame.time.Clock()

pygame.display.set_caption("Burger Chef")

class Sprite(object):
    def __init__(self, posX, posY):
        self.surface = ROOT
        self.color = None
        self.SIZE_W = 0
        self.SIZE_H = 0
        self.speed = 5
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)

    def draw(self):
        pygame.draw.rect(self.surface, self.color, self.rect)


class Player(Sprite):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.gold["pygame"]
        self.SIZE_W = 100
        self.SIZE_H = 20
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)
        self.burger = []

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= SCREEN_X - self.SIZE_W:
            self.rect.x = SCREEN_X - self.SIZE_W

    def draw(self):
        super().draw()
        if len(self.burger) > 0:
            for topping in self.burger:
                topping.draw()


class Topping(Sprite):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.SIZE_W = 100
        self.SIZE_H = 20
        self.speed = random.randrange(2, 5)
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)

    def set_new_speed(self):
        self.speed = random.randrange(2, 5)

    def update(self):
        self.rect.y += self.speed
        if self.rect.y >= SCREEN_Y + self.SIZE_H:
            self.rect.y = 20
            self.rect.x = random.randrange(0, SCREEN_X - self.SIZE_W)
            self.set_new_speed()



class Meat(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.brown["pygame"]
        self.SIZE_H = 50
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)

class Mustard(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.mustard["pygame"]
        self.SIZE_H = 5
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)

class Cheese(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.yellow["pygame"]
        self.SIZE_H = 5
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)


class Ketchup(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.red["pygame"]
        self.SIZE_H = 5
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)


class Tomato(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.red["pygame"]
        self.SIZE_H = 20
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)


class Lettuce(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.green["pygame"]
        self.SIZE_H = 5
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)


class Onion(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.gray["pygame"]
        self.SIZE_H = 15
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)

class Crown(Topping):
    def __init__(self, posX, posY):
        super().__init__(posX, posY)
        self.color = cs.gold["pygame"]
        self.SIZE_H = 50
        self.rect = pygame.Rect(posX, posY, self.SIZE_W, self.SIZE_H)


player = Player(SCREEN_X /2, 440)
onion = Onion(random.randrange(0, SCREEN_X -100), 20)
cheese = Cheese((random.randrange(0, SCREEN_X - 100)), 20)
ketchup = Ketchup((random.randrange(0, SCREEN_X - 100)),20)
meat = Meat((random.randrange(0, SCREEN_X - 100)),20)
lettuce = Lettuce((random.randrange(0, SCREEN_X - 100)),20)
mustard = Mustard((random.randrange(0, SCREEN_X - 100)),20)
crown = Crown((random.randrange(0, SCREEN_X - 100)),20)

toppings = [onion, cheese, ketchup, meat, lettuce, mustard, crown]

burger_top = player.rect.y




def update():
    global burger_top
    for topping in toppings:
        topping.update()
        if topping.rect.colliderect(player.rect):
            if topping.rect.y + topping.SIZE_H >= burger_top and topping.rect.y > burger_top:
                topping.rect.y = burger_top - topping.SIZE_H
                topping.rect.x = player.rect.x
                burger_top = topping.rect.y


    player.update()






def draw():
    for topping in toppings:
        topping.draw()

    player.draw()



def run():
    inPlay = True

    while inPlay:
        CLOCK.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                inPlay = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            inPlay = False

        update()
        draw()

        pygame.display.update()
        ROOT.fill(BG_COLOR)


if __name__=='__main__':
    run()