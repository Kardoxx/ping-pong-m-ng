#Kardo Tamm
import pygame
import random

# initsialiseeri pygame
pygame.init()

# Ekraani suurus
screenWidth = 640
screenHeight = 480
screen = pygame.display.set_mode([screenWidth, screenHeight])

# Tausta värv
bgColor = (200, 200, 200)

# Palli suurus ja kiirus
ballSize = 20
ballSpeedX = 5
ballSpeedY = 5

# Aluse suurus ja kiirus
paddleWidth = 120
paddleHeight = 20
paddleSpeed = 5

# Laeb pildid
ballImg = pygame.image.load("ball.png").convert_alpha()
ballImg = pygame.transform.scale(ballImg, [ballSize, ballSize])
paddleImg = pygame.image.load("pad.png").convert_alpha()
paddleImg = pygame.transform.scale(paddleImg, [paddleWidth, paddleHeight])

# Aluse positsioon
paddleX = screenWidth / 2 - paddleWidth / 2
paddleY = screenHeight - paddleHeight - 10

# Palli positsioon
ballX = random.randint(0, screenWidth - ballSize)
ballY = 0

# Skoor
score = 0

# Mängu tsükkel
clock = pygame.time.Clock()
running = True
while running:

    # Kontrollib eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # mLiigutab palli
    ballX += ballSpeedX
    ballY += ballSpeedY

    # Põrkab seintelt
    if ballX <= 0 or ballX >= screenWidth - ballSize:
        ballSpeedX *= -1
    if ballY <= 0:
        score += 1
        ballX = random.randint(0, screenWidth - ballSize)
        ballY = 0
        ballSpeedY = 5

    # Kontrollib kas pall läks alusest mooda
    if ballY >= screenHeight:
        running = False

    # collide with paddle
    if ballY + ballSize >= paddleY and ballX + ballSize >= paddleX and ballX <= paddleX + paddleWidth:
        ballSpeedY *= -1
        score += 1

    # Liigutab alust
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddleX > 0:
        paddleX -= paddleSpeed
    if keys[pygame.K_RIGHT] and paddleX < screenWidth - paddleWidth:
        paddleX += paddleSpeed

    # Joonistab asjad ekraanile
    screen.fill(bgColor)
    screen.blit(ballImg, (ballX, ballY))
    screen.blit(paddleImg, (paddleX, paddleY))

    # Seadistab skoori
    font = pygame.font.Font(None, 36)
    scoreText = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(scoreText, (10, 10))

    # Uuendab ekraani
    pygame.display.flip()

    # Limiteerib frame
    clock.tick(60)

# Lahkub pygamest
pygame.quit()
