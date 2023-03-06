#Kardo Tamm
import pygame
import random

# initialiseerib pygame
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

# aluse suurus ja kiirus
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

# skoor
score = 0

# Paneb mängu loop'i
clock = pygame.time.Clock()
running = True
while running:

    # Kontrollib eventi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Liigutab palli
    ballX += ballSpeedX
    ballY += ballSpeedY

    # Põrkab seintelt
    if ballX <= 0 or ballX >= screenWidth - ballSize:
        ballSpeedX *= -1
    if ballY <= 0:
        ballSpeedY *= -1

    # kontrollige, kas pall puudutab alust
    if ballY >= screenHeight - ballSize:
        score -= 1
        ballX = random.randint(0, screenWidth - ballSize)
        ballY = 0
        ballSpeedY = 5

    # aeruga kokku põrkumine
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

    # Limiteerib mängu fps'i
    clock.tick(60)

# Lahkub pygamest
pygame.quit()
