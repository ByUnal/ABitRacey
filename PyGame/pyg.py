import pygame
import time
import random

pygame.init()

crash_eff = pygame.mixer.Sound("Crash.wav")
pygame.mixer.music.load("Bond.wav")

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255) #r-g-b kuralına göre yapıyoruz
red = (200,0,0)
green = (0,200,0)
blue = (0,0,200)

color_thing = (0,20,240)
color_go = (50,80,250)

bright_red = (255,0,0)
bright_green = (0,240,0)

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption("A bit racey")
clock = pygame.time.Clock()

carimg = pygame.image.load("car12.png")
car_width = 87

iconImg = pygame.image.load("gameicon.png")
gameIcon = pygame.display.set_icon(iconImg)

pause = False

def thing_dodged(count):
    font = pygame.font.SysFont("cooperblack",24)
    font_inf = pygame.font.SysFont("comicsansms",14)
    text = font.render("Dodged: "+str(count),True,black)
    text2 = font_inf.render("( ' P ' for Pause )", True, blue)
    gameDisplay.blit(text,(10,10))
    gameDisplay.blit(text2,(10,35))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx,thingy,thingw,thingh])

def car(x,y):
    gameDisplay.blit(carimg,(x,y))

def text_objects(text,font,color):
    textSurface = font.render(text, True, color)
    return textSurface,textSurface.get_rect()


def crash():

    pygame.mixer.music.stop()
    pygame.mixer.Sound.play(crash_eff)

    largeTxt = pygame.font.SysFont("calibri", 115)
    txtSurf, txtRect = text_objects("You Crashed!", largeTxt, red)
    txtRect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(txtSurf, txtRect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Play Again", 150, 420, 120, 50, green, bright_green,game_loop)  # we don't use pharanthesis. If we do, function will work directly
        button("QUIT", 550, 420, 100, 50, red, bright_red, quitgame)

        pygame.display.update()
        clock.tick(15)


def button(msg, x, y, width, height, interactive_color, active_color, action = None):
    mouse = pygame.mouse.get_pos()
    # mouse[0] is x-axis element , mouse[1] is y-axis element

    click = pygame.mouse.get_pressed()

    if x + width > mouse[0] > x and y + height > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(gameDisplay, interactive_color, (x, y, width, height))

    smallText = pygame.font.SysFont("comicsansms", 23)
    txtSurf, txtRect = text_objects(msg, smallText, color_go)
    txtRect.center = ((x + (width / 2)), (y + (height / 2)))
    gameDisplay.blit(txtSurf, txtRect)

def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause = False

def paused():

    pygame.mixer.music.pause()

    largeTxt = pygame.font.SysFont("calibri", 115)
    txtSurf, txtRect = text_objects("A bit Racey", largeTxt, red)
    txtRect.center = (display_width / 2, display_height / 2)
    gameDisplay.blit(txtSurf, txtRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Continue",150,450,100,50,green,bright_green,unpaused) # we don't use pharanthesis. If we do, function will work directly
        button("QUIT", 550, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeTxt = pygame.font.SysFont("calibri", 115)
        txtSurf, txtRect = text_objects("A bit Racey", largeTxt,red)
        txtRect.center = (display_width / 2, display_height / 2)
        gameDisplay.blit(txtSurf, txtRect)

        button("GO!",150,450,100,50,green,bright_green,game_loop) # we don't use pharanthesis. If we do, function will work directly
        button("QUIT", 550, 450, 100, 50, red, bright_red,quitgame)

        pygame.display.update()
        clock.tick(15)

def quitgame():
    pygame.quit()
    quit()

def game_loop():

    pygame.mixer.music.play(-1)

    x = display_width * 0.45
    y = display_height * 0.75

    x_change = 0

    thing_startx = random.randrange(0,display_width)
    thing_starty = -600
    thing_speed = 8
    thing_width = 100
    thing_height = 100

    dodged = 0

    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_p:
                    global pause
                    pause = True
                    paused()


            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change

        gameDisplay.fill(white)

        # things(thingx, thingy, thingw, thingh, color)
        things(thing_startx,thing_starty,thing_width,thing_height, color_thing)
        thing_starty += thing_speed

        thing_dodged(dodged)

        car(x,y)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height - 50:
            thing_starty = 0 - display_height
            thing_startx = random.randrange(0, display_width)
            dodged += 1
            if dodged > 5:
                thing_speed = 11
                thing_width = 120
            elif dodged > 13:
                thing_speed = 15
                thing_width = 125
            elif dodged > 25:
                thing_speed = 18
                thing_width = 140
                clock.tick(50)


        if y < thing_starty + thing_height - 6: #y crossover
            if x > thing_startx and x < thing_startx + thing_width or x+car_width > thing_startx and x+car_width < thing_startx + thing_width: #x crossover
                crash()


        pygame.display.update() #.flip olabilirdi
        clock.tick(60)


intro()
game_loop()
pygame.quit()
quit()