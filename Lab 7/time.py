import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((829, 800))
done = False
bg_image = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\Lab 7\clock.png")
sec_img = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\Lab 7\sec.png")
min_img = pygame.image.load(r"C:\Users\Admin\OneDrive\Рабочий стол\Lab 7\min.png")

rect = bg_image.get_rect(center=(415, 418))

while not done:
    screen.blit(bg_image, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    time = datetime.now().time()

    sec_angle = -(time.second * 6)
    sec_img = pygame.transform.rotate(sec_img, sec_angle)
    sec_rect = sec_img.get_rect(center=rect.center)
    screen.blit(sec_img, sec_rect.topleft)

    min_angle = -(time.minute * 6)
    min_img = pygame.transform.rotate(min_img, min_angle)
    min_rect = min_img.get_rect(center=rect.center)
    screen.blit(min_img, min_rect.topleft)

    pygame.display.flip()