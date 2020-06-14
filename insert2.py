from tkinter import*
import insert
import pygame
import time



def insert2():
    a = insert.list()
    pygame.init()
    win = pygame.display.set_mode((1200, 750))
    pygame.display.set_caption("Insertion")
    myFont2 = pygame.font.SysFont("Times New Roman", 30)
    dataLabel = []
    data=[]
    ax = []
    ay = []
    ah = []
    index=insert.retindex();
    n = int(insert.num())
    d=int(insert.returnd())
    data.append(myFont2.render(str(int(d)),1,(255,255,255)))
    width = 30
    temp = 200
    for i in range(n):
        ax.append(temp)
        temp += width + 10
        ay.append(650)
        ah.append(-5 * a[i])
    ax.append(temp)

    for i in range(0, n):
        dataLabel.append(myFont2.render(str(int(-0.2 * ah[i])), 1, (255, 255, 255)))

    font = pygame.font.SysFont("cambria", 30)
    font2 = pygame.font.SysFont("Times", 20)
    text = font.render('Insertion', True, (255, 255, 255))
    text2 = font2.render('(Press SPACE-BAR to proceed to visualization of insertion process)', True, (255, 255, 255))
    state1=myFont2.render('Cannot insert at this index!!',1,(255,255,255))
    textRect = text.get_rect()
    textRect.center = (400, 50)
    textRect2 = text.get_rect()
    textRect2.center = (300, 100)
    textRect3 = text.get_rect()
    textRect3.center = (800, 500)
    run = True
    flag=-1

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
            pygame.draw.rect(win, (255, 0, 0), (750, ay[0], width, d * -5))
            win.blit(data[0], (750, ay[0] + 30))
            for i in range(n):
                pygame.time.delay(500)
                win.fill((0, 0, 0))
                win.blit(text, textRect)
                win.blit(text2, textRect2)
                for x in range(n):
                    pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                    win.blit(dataLabel[x], (ax[x], ay[x] + 30))
                pygame.draw.rect(win, (255, 0, 0), (750, ay[0], width, d * -5))
                win.blit(data[0], (750, ay[0] + 30))
                pygame.draw.rect(win, (255, 255, 0), (ax[i], ay[i], width, ah[i]))
                pygame.display.update()
                if i==index:
                    pygame.time.delay(500)
                    e=[]
                    e.append(myFont2.render(str(int(d)), 1, (255, 255, 255)))
                    dataLabel.insert(index,e[0])
                    ay.insert(index,650)
                    ah.insert(index, -5*d)
                    n += 1
                    flag=i
                    break

            win.fill((0, 0, 0))
            win.blit(text, textRect)
            win.blit(text2, textRect2)
            for x in range(n):
                pygame.draw.rect(win, (255, 0, 0), (ax[x], ay[x], width, ah[x]))
                win.blit(dataLabel[x], (ax[x], ay[x] + 30))
            pygame.display.update()
            if flag == -1:
                win.blit(state1, textRect3)
            else:
                some = 'The element inserted at index: ' + str(flag)
                state = (myFont2.render((some), 1, (255, 255, 255)))
                win.blit(state, textRect3)
            pygame.display.update()
    pygame.display.update()

    pygame.quit()