from tkinter import*
import selection
import pygame
import time



def selectionsort():
    a = selection.list()
    pygame.init()
    win = pygame.display.set_mode((900,800))
    pygame.display.set_caption("Selection Sort")
    myFont2 = pygame.font.SysFont("Times New Roman", 30)
    dataLabel = []
    ax=[]
    ay=[]
    ah=[]
    n=int(selection.num())
    width=30
    temp=200
    for i in range(n):
        ax.append(temp)
        temp+=width+10
        ay.append(650)
        ah.append(-5*a[i])

    for i in range(0, n):
     dataLabel.append(myFont2.render(str(int(-0.2*ah[i])), 1, (255, 255, 255)))

    font = pygame.font.SysFont("cambria", 35)
    font2 = pygame.font.SysFont("Times", 20)
    text = font.render('SELECTION SORT', True, (255,255,255))
    text2=font2.render('(Press SPACE-BAR to proceed to visualization of sorting)',True,(255,255,255))
    textRect = text.get_rect()
    textRect.center = (400,50)
    textRect2 = text.get_rect()
    textRect2.center = (300,100)


    run=True

    while run:
        win.blit(text, textRect)
        win.blit(text2, textRect2)
        pygame.time.delay(100)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        for x in range(n):
            pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
            win.blit(dataLabel[x], (ax[x], ay[x] + 30))
        pygame.display.update()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            for i in range(n):
                min_idx = i
                for j in range(i + 1, n):
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            run = False
                    win.fill((0, 0, 0))
                    win.blit(text, textRect)
                    win.blit(text2, textRect2)
                    pygame.time.delay(500)
                    for x in range(n):
                        pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                        win.blit(dataLabel[x], (ax[x], ay[x] + 30))
                    pygame.draw.rect(win, (255, 255, 0), (ax[min_idx], ay[min_idx], width, ah[min_idx]))
                    pygame.draw.rect(win, (255, 255, 0), (ax[j], ay[j], width, ah[j]))
                    pygame.display.update()
                    if ah[min_idx] < ah[j]:
                        min_idx = j
                pygame.time.delay(500)
                win.fill((0, 0, 0))
                win.blit(text, textRect)
                win.blit(text2, textRect2)
                for x in range(n):
                    pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                    win.blit(dataLabel[x], (ax[x], ay[x] + 30))
                pygame.draw.rect(win, (255, 255, 0), (ax[min_idx], ay[min_idx], width, ah[min_idx]))
                pygame.draw.rect(win, (255, 255, 0), (ax[i], ay[i], width, ah[i]))
                pygame.display.update()
                ah[i], ah[min_idx] = ah[min_idx], ah[i]
                pygame.time.delay(500)
                win.fill((0, 0, 0))
                win.blit(text, textRect)
                win.blit(text2, textRect2)
                for x in range(n):
                    pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                    win.blit(dataLabel[x], (ax[x], ay[x] + 30))
                pygame.draw.rect(win, (255, 255, 0), (ax[min_idx], ay[min_idx], width, ah[min_idx]))
                pygame.draw.rect(win, (255, 255, 0), (ax[i], ay[i], width, ah[i]))
                pygame.display.update()

                for i in range(0, n):
                    dataLabel[i] = myFont2.render(str(int(-0.2*ah[i])), 1, (255,255,255))
                pygame.time.delay(500)
                win.fill((0, 0, 0))
                win.blit(text, textRect)
                win.blit(text2, textRect2)
                for x in range(n):
                    pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                    win.blit(dataLabel[x], (ax[x], ay[x] + 30))


            pygame.display.update()


    pygame.display.quit()

