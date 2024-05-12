import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width = 400
height = 600

# Цвета
white = (255, 255, 255)

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Тестовый экран мобильного приложения")

# Основной цикл программы
while True:
    # Обработка событий
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Заливка экрана белым цветом
    screen.fill(white)

    # Обновление экрана
    pygame.display.flip()
