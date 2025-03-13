import pygame
import sys


pygame.init()


screen_width, screen_height = 640, 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hajutamine")


background_image = pygame.image.load("bg_shop.jpg")
poem_image = pygame.image.load("seller.png")
speech_bubble_image = pygame.image.load("chat.png")


background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
poem_image = pygame.transform.scale(poem_image, (250, 250))
speech_bubble_image = pygame.transform.scale(speech_bubble_image, (200, 150))


font = pygame.font.Font(None, 16)


name = "Alex-Sander Zapotõlok"
text = font.render(f"Tere, olen {name}", True, (255, 255, 255))


background_pos = (0, 0)
poem_pos = (50, 170)
speech_bubble_pos = (300, 150)
text_pos = (309, 200)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    screen.blit(background_image, background_pos)


    screen.blit(poem_image, poem_pos)


    screen.blit(speech_bubble_image, speech_bubble_pos)


    screen.blit(text, text_pos)


    pygame.display.flip()
