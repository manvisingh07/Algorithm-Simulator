from tkinter import*
import bubble
import pygame
import time

def bubblesort():
    a = bubble.list()
    pygame.init()
    win = pygame.display.set_mode((900, 800))
    pygame.display.set_caption("Bubble Sort")
    colour2 = (255, 255, 255)
    myFont2 = pygame.font.SysFont("Times New Roman", 30)
    dataLabel = []
    ax = []
    ay = []
    ah = []
    n = int(bubble.num())
    width = 30
    temp = 200
    for i in range(n):
        ax.append(temp)
        temp += width + 10
        ay.append(700)
        ah.append(-5 * a[i])

    for i in range(0, n):
        dataLabel.append(myFont2.render(str(int(-0.2 * ah[i])), 1, colour2))

    font = pygame.font.SysFont("cambria", 35)
    font2 = pygame.font.SysFont("Times", 20)
    text = font.render('BUBBLE SORT', True, (255,255,255))
    text2=font2.render('(Press SPACE-BAR to proceed to visualization of sorting)',True,(255,255,255))
    textRect = text.get_rect()
    textRect.center = (400,50)
    textRect2 = text.get_rect()
    textRect2.center = (300,100)

    run=True

    while run:
        win.blit(text, textRect)
        win.blit(text2, textRect2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False
        for x in range(0, n):
            pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
            win.blit(dataLabel[x], (ax[x], ay[x] + 30))
        pygame.display.update()
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for i in range(n):
                for j in range(n-i-1):
                    pygame.time.delay(500)
                    win.fill((0,0,0))
                    win.blit(text, textRect)
                    win.blit(text2, textRect2)
                    pygame.time.delay(500)
                    if ah[j] < ah[j + 1]:
                        ah[j], ah[j + 1] = ah[j + 1], ah[j]
                        pygame.time.delay(1000)
                    for i in range(0, n):
                         dataLabel[i] = myFont2.render(str(int(-0.2 * ah[i])), 1, colour2)
                    for x in range(0, n):
                        pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                        win.blit(dataLabel[x], (ax[x], ay[x] + 30))
                    pygame.draw.rect(win, (255, 255, 0), (ax[j], ay[j], width, ah[j]))
                    pygame.draw.rect(win, (255, 255, 0), (ax[j + 1], ay[j + 1], width, ah[j + 1]))
                    pygame.display.update()
            pygame.display.update()

    pygame.display.quit()


