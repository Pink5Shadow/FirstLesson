import pygame

pygame.init()

# Инциализируем рудате

HEIGHT = 300
WIDTH = 300

WINDOW_SIZE = (HEIGHT, WIDTH)

# Создаём окно
screen = pygame.display.set_mode(WINDOW_SIZE)

# Называем окно
pygame.display.set_caption('Моё первое окно в PyGame')

color_list = [
    pygame.Color("#FF0000"), #красный
    pygame.Color("#00FF00"), #зелёный
]

current_color = 0

#Создаём кнопку
button_font = pygame.font.SysFont("Times New Roman", 15)
button_font_color = pygame.Color("black")
button_color = pygame.Color("gray")
button_rect = pygame.Rect(100, 115, 100, 50)
button_text = button_font.render("Нажми меня!", True, button_font_color)

# Определить фоновый элемент
backround = pygame.Surface(WINDOW_SIZE)
backround.fill(pygame.Color("#000000"))

# Обновляем экран
pygame.display.flip()

# Загружаем фото
image = pygame.image.load("japan.jpg")

# Изменяем размер фото
image = pygame.transform.scale(image, WINDOW_SIZE)

# Накладываем изображение
screen.blit(image, (0, 0))

# Обновляем экран
pygame.display.flip()

# Определяем цвет
#backround = (190, 56, 19)

# заполняем фон
# screen.fill(backround)


# Обновляем экран
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if button_rect.collidepoint(event.pos):
                current_color = (current_color + 1) % len(color_list)
                backround.fill(color_list[current_color])
    screen.blit(backround, (0,0))
    pygame.draw.rect(screen, button_color, button_rect)

    button_rect_center = button_text.get_rect(center=button_rect.center)
    screen.blit(button_text, button_rect_center)

    pygame.display.update()