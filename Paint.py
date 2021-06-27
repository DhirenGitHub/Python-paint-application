import pygame
import sys

WIDTH = 500
HEIGHT = 500
FPS = 120

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Paint!")
clock = pygame.time.Clock()

colors = ((250, 0, 0), (0, 250, 0), (0, 0, 250), (10, 10, 10), (0, 153, 76), (51, 153, 255), (255, 255, 0), (204, 0, 204), (250, 250, 250))
selected_color = (10, 10, 10)
click = False


class Button(pygame.sprite.Sprite):
    def __init__(self, x, y, color, size):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface(size)
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Paint(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(selected_color)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.rect.width / 2
        self.rect.y = y - self.rect.height / 2


paint = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

for i in range(9):
    b = Button(50 * i, HEIGHT - 50, colors[i], (50, 50))
    all_sprites.add(b)

border = Button(0, HEIGHT - 50 - 15, (100, 100, 100), (WIDTH, 15))
all_sprites.add(border)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    mouse_press = pygame.mouse.get_pressed()
    mouse_pos = pygame.mouse.get_pos()

    if mouse_press[0] == 1:
        if 50 >= mouse_pos[0] >= 0 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[0]
            click = True

        elif 50 * 2 >= mouse_pos[0] >= 50 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[1]
            click = True

        elif 50 * 3 >= mouse_pos[0] >= 50 * 2 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[2]
            click = True

        elif 50 * 4 >= mouse_pos[0] >= 50 * 3 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[3]
            click = True

        elif 50 * 5 >= mouse_pos[0] >= 50 * 4 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[4]
            click = True

        elif 50 * 6 >= mouse_pos[0] >= 50 * 5 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[5]
            click = True

        elif 50 * 7 >= mouse_pos[0] >= 50 * 6 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[6]
            click = True

        elif 50 * 8 >= mouse_pos[0] >= 50 * 7 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[7]
            click = True

        elif 50 * 9 >= mouse_pos[0] >= 50 * 8 and mouse_pos[1] >= HEIGHT - 50:
            selected_color = colors[8]
            click = True

        else:
            p = Paint(mouse_pos[0], mouse_pos[1])
            paint.add(p)

    screen.fill((250, 250, 250))
    paint.draw(screen)
    paint.update()
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()
    pygame.display.flip()
