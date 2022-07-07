import pygame
import random
import math
import pandas as pd

pygame.init()


class draw_information:
    black = 0, 0, 0
    white = 255, 255, 255
    green = 0, 255, 0
    red = 255, 0, 0
    background_color = white

    gradients = [(128, 128, 128), (160, 160, 160), (192, 192, 192)]

    font = pygame.font.SysFont('Helvetica', 30)
    large_font = pygame.font.SysFont('Helvetica', 40)

    side_pad = 100
    top_pad = 150

    def __init__(self, width, height, lst):
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Project")
        self.set_list(lst)

    def set_list(self, lst):
        self.lst = lst
        self.min_val = min(lst)
        self.max_val = max(lst)

        self.block_width = round((self.width - self.side_pad)/len(lst))
        self.block_height = round(
            (self.height - self.top_pad) / (self.max_val - self.min_val))
        self.start_x = self.side_pad // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.background_color)

    controls = draw_info.font.render(
        "R - Reset | Space - Start Sorting | A - Ascending | D -Desscending", 1, draw_info.black)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 5))

    controls = draw_info.font.render(
        "I- Insertion Sort | B - Bubble Sort", 1, draw_info.black)
    draw_info.window.blit(
        controls, (draw_info.width/2 - controls.get_width()/2, 35))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * \
            draw_info.block_height

        color = draw_info.gradients[i % 3]

        pygame.draw.rect(draw_info.window, color,
                         (x, y, draw_info.block_width, draw_info.height))


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = draw_information(800, 600, lst)
    sorting = True
    ascending = True

    while run:
        clock.tick(60)

        draw(draw_info)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type != pygame.KEYDOWN:
                continue

            if event.key == pygame.K_r:
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False:
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False

    pygame.quit()


if __name__ == "__main__":
    main()
