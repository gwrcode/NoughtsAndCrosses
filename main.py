import pygame, time, sys, random, os
def setup():
    pygame.init()
    win = pygame.display.set_mode((500, 600))
    pygame.display.set_caption("Noughts and Crosses")
    win.fill((255, 255, 255))
    im = [pygame.image.load("noughtsandcrossesboard.jpg").convert(), pygame.image.load("crosses.PNG").convert(), pygame.image.load("nought.PNG").convert()]
    im[0] = pygame.transform.scale(im[0], (500, 500))
    pygame.font.init()
    font2 = pygame.font.Font("font1.ttf", 50)
    title = font2.render('Noughts and Crosses!', False, (0, 0, 0))
    win.blit(title, (0, 0))
    playbtn = pygame.draw.rect(win, (0, 255, 255), (100, 75, 300, 200))
    font2 = pygame.font.Font("font1.ttf", 100)
    playtxt = font2.render('Play!', False, (0, 0, 0))
    win.blit(playtxt, (150, 125))
    aibtn = pygame.draw.rect(win, (0, 255, 255), (100, 300, 300, 200))
    font2 = pygame.font.Font("font1.ttf", 50)
    aitxt0 = font2.render('Play with ', False, (0, 0, 0))
    aitxt1 = font2.render('computer!', False, (0, 0, 0))
    win.blit(aitxt0, (125, 350))
    win.blit(aitxt1, (125, 400))
    menu(win, im, playbtn, aibtn)
def menu(win, im, playbtn, aibtn):
    run = True
    while run:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_position = pygame.mouse.get_pos()
                if (playbtn.collidepoint(mouse_position)):
                    normal(win, im)
                if (aibtn.collidepoint(mouse_position)):
                    ai(win, im)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()
def normal(win, im):
    run = True
    turn = 1
    log = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    symbol = ["___", "Noughts", "Crosses"]
    places = [[0, 100, 163, 166], [173, 100, 155, 166], [338, 100, 155, 166], [0, 276, 163, 155], [173, 276, 155, 155], [338, 276, 155, 155], [0, 441, 163, 155], [173, 441, 155, 155], [338, 441, 155, 155]]
    win.fill((255, 255, 255))
    win.blit(im[0], (0, 100))
    for i in range (0, len(places)):
        places[i] = pygame.draw.rect(win, (255, 255, 255), (places[i]))
    while run:
        pygame.display.update()
        win.fill((255, 255, 255), (0,0, 500, 100))
        font2 = pygame.font.Font("font1.ttf", 60)
        turntxt = font2.render("It's {} turn!".format(symbol[turn]), False, (0, 0, 0))
        win.blit(turntxt, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_position = pygame.mouse.get_pos()
                for i in range (0, len(places)):
                    if (places[i].collidepoint(mouse_position)):
                        if log[i] == "_":
                            if testwin(im, turn, win, log, i, symbol, places, 70) == "end":
                                run = False
                            if turn == 1:
                                turn += 1
                            elif turn == 2:
                                turn -= 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()
    pygame.display.quit()
    setup()
def ai(win, im):
    run = True
    turn = 1
    log = ["_", "_", "_", "_", "_", "_", "_", "_", "_"]
    symbol = ["___", "The Challenger", "The Computer"]
    places = [[0, 100, 163, 166], [173, 100, 155, 166], [338, 100, 155, 166], [0, 276, 163, 155], [173, 276, 155, 155],[338, 276, 155, 155], [0, 441, 163, 155], [173, 441, 155, 155], [338, 441, 155, 155]]
    win.fill((255, 255, 255))
    win.blit(im[0], (0, 100))
    for i in range(0, len(places)):
        places[i] = pygame.draw.rect(win, (255, 255, 255), (places[i]))
    while run:
        pygame.display.update()
        win.fill((255, 255, 255), (0, 0, 500, 100))
        font2 = pygame.font.Font("font1.ttf", 50)
        turntxt = font2.render("It's {} turn!".format(symbol[turn]), False, (0, 0, 0))
        win.blit(turntxt, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_position = pygame.mouse.get_pos()
                for i in range(0, len(places)):
                    if (places[i].collidepoint(mouse_position)):
                         if log[i] == "_":
                            if testwin(im, turn, win, log, i, symbol, places, 35) == "end":
                                pygame.display.quit()
                                setup()
                            turn += 1
                            win.fill((255, 255, 255), (0, 0, 500, 100))
                            font2 = pygame.font.Font("font1.ttf", 35)
                            turntxt = font2.render("{} is thinking about it!".format(symbol[turn]), False, (0, 0, 0))
                            win.blit(turntxt, (0, 0))
                            pygame.display.update()
                            time.sleep(1)
                            if testwin(im, turn, win, log, processing(log), symbol, places, 35) == "end":
                                pygame.display.quit()
                                setup()
                            turn-=1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            pygame.display.quit()
            sys.exit()
def renderplace(log):
    ck1 = str(log[0]) + str(log[1]) + str(log[2])
    ck2 = str(log[0]) + str(log[3]) + str(log[6])
    ck3 = str(log[0]) + str(log[4]) + str(log[8])
    ck4 = str(log[2]) + str(log[5]) + str(log[8])
    ck5 = str(log[2]) + str(log[4]) + str(log[6])
    ck6 = str(log[1]) + str(log[4]) + str(log[7])
    ck7 = str(log[3]) + str(log[4]) + str(log[5])
    ck8 = str(log[6]) + str(log[7]) + str(log[8])
    return ck1, ck2, ck3, ck4, ck5, ck6, ck7, ck8
def testwin(im, turn, win, log, i, symbol, places, size):
    winning = False
    im[turn] = pygame.transform.scale(im[turn], (150, 150))
    win.blit(im[turn], places[i])
    pygame.display.update()
    log[i] = turn
    ck1, ck2, ck3, ck4, ck5, ck6, ck7, ck8 = renderplace(log)
    if ck1 == "111" or ck1 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 0, 2, 0, 75, 150, 75
    elif ck2 == "111" or ck2 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 0, 6, 75, 0, 75, 150
    elif ck3 == "111" or ck3 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 0, 8, 0, 0, 150, 150
    elif ck4 == "111" or ck4 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 2, 8, 75, 0, 75, 150
    elif ck5 == "111" or ck5 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 2, 6, 150, 0, 0, 150
    elif ck6 == "111" or ck6 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 1, 7, 75, 0, 75, 150
    elif ck7 == "111" or ck7 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 3, 5, 0, 75, 150, 75
    elif ck8 == "111" or ck8 == "222":
        winning, one, two, mod1, mod2, mod3, mod4 = True, 6, 8, 0, 75, 150, 75
    if winning:
        font2 = pygame.font.Font("font2.ttf", size)
        pygame.draw.line(win, (255, 0, 0), (list(places[one])[0]+mod1, list(places[one])[1]+mod2), (list(places[two])[0]+mod3, list(places[two])[1]+mod4), 10)
        pygame.display.update()
        time.sleep(1)
        win.fill((255, 255, 255))
        for i in range(0, 20):
            wintxt = font2.render("{} Won!".format(symbol[turn]), False, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            win.blit(wintxt, (0, 250))
            pygame.display.update()
            time.sleep(0.1)
        return "end"
    elif "_" not in log:
        font2 = pygame.font.Font("font2.ttf", size)
        time.sleep(1)
        win.fill((255, 255, 255))
        for i in range(0, 20):
            drawtxt = font2.render("Draw!", False,(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            win.blit(drawtxt, (0, 250))
            pygame.display.update()
            time.sleep(0.1)
        return "end"
def processing(log):
    proc = True
    placement = random.randint(0, 8)
    while proc:
        if log[placement] != "_":
            placement = random.randint(0, 8)
        else:
            proc = False
    ck1, ck2, ck3, ck4, ck5, ck6, ck7, ck8 = renderplace(log)
    if "22_" in ck1 or "2_2" in ck1 or "_22" in ck1:
        placement = list(ck1).index("_")
    elif "22_" in ck2 or "2_2" in ck2 or "_22" in ck2:
        placement = list(ck2).index("_")
        placement += 2 * placement
    elif "22_" in ck3 or "2_2" in ck3 or "_22" in ck3:
        placement = list(ck3).index("_")
        placement += 3 * placement
    elif "22_" in ck4 or "2_2" in ck4 or "_22" in ck4:
        placement = list(ck4).index("_")
        placement += 2 * (placement + 1)
    elif "22_" in ck5 or "2_2" in ck5 or "_22" in ck5:
        placement = list(ck5).index("_")
        placement += (placement + 2)
    elif "22_" in ck6 or "2_2" in ck6 or "_22" in ck6:
        placement = list(ck6).index("_")
        placement += (2 * placement) + 1
    elif "22_" in ck7 or "2_2" in ck7 or "_22" in ck7:
        placement = list(ck7).index("_")
        placement += 3
    elif "22_" in ck8 or "2_2" in ck8 or "_22" in ck8:
        placement = list(ck8).index("_")
        placement += 6
    elif "11_" in ck1 or "1_1" in ck1 or "_11" in ck1:
        placement = list(ck1).index("_")
    elif "11_" in ck2 or "1_1" in ck2 or "_11" in ck2:
        placement = list(ck2).index("_")
        placement += 2 * placement
    elif "11_" in ck3 or "1_1" in ck3 or "_11" in ck3:
        placement = list(ck3).index("_")
        placement += 3 * placement
    elif "11_" in ck4 or "1_1" in ck4 or "_11" in ck4:
        placement = list(ck4).index("_")
        placement += 2 * (placement + 1)
    elif "11_" in ck5 or "1_1" in ck5 or "_11" in ck5:
        placement = list(ck5).index("_")
        placement += (placement + 2)
    elif "11_" in ck6 or "1_1" in ck6 or "_11" in ck6:
        placement = list(ck6).index("_")
        placement += (2 * placement) + 1
    elif "11_" in ck7 or "1_1" in ck7 or "_11" in ck7:
        placement = list(ck7).index("_")
        placement += 3
    elif "11_" in ck8 or "1_1" in ck8 or "_11" in ck8:
        placement = list(ck8).index("_")
        placement += 6
    return placement
setup()