import pygame
import sys

pygame.init()

#window setting
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Table Tennis')

#color
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
player_x, player_y = 30, HEIGHT // 2 - PADDLE_HEIGHT // 2
ai_x, ai_y = WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2
PLAYER_PADDLE_SPEED = 6
AI_PADDLE_SPEED = 4  #default(Expert)

#ball settings
BALL_SIZE = 16
ball_x,ball_y = WIDTH // 2, HEIGHT // 2
ball_dx,ball_dy = 4, 4  #lower ball

#score
player_score = 0
ai_score = 0
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

#reset ball position and direction
def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx *= -1
    ball_dy = 4 if ball_dy > 0 else -4

#draw everything
def draw():
    screen.fill(BLACK)
    pygame.draw.rect(screen, WHITE, (player_x, player_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (ai_x, ai_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.ellipse(screen, WHITE, (ball_x, ball_y, BALL_SIZE, BALL_SIZE))
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    player_text = font.render(str(player_score), True, WHITE)
    ai_text = font.render(str(ai_score), True, WHITE)
    screen.blit(player_text, (WIDTH // 4, 20))
    screen.blit(ai_text, (WIDTH * 3 // 4, 20))
    pygame.display.flip()

#difficulty selection menu
def choose_difficulty():
    global AI_PADDLE_SPEED
    menu_font = pygame.font.SysFont(None, 36)
    difficulties = [
        ("Beginner (Press 1)", 2),
        ("Intermediate (Press 2)", 3),
        ("Expert (Press 3)", 4),
        ("Impossible (Press 4)", 10)]
    
    selecting = True #menu loop
    while selecting:
        screen.fill(BLACK)
        title = font.render("Select Difficulty", True, WHITE)
        screen.blit(title, (WIDTH//2 - title.get_width()//2, 100))
        #display options
        for i, (label, _) in enumerate(difficulties):
            text = menu_font.render(label, True, WHITE)
            screen.blit(text, (WIDTH//2 - text.get_width()//2, 200 + i*50))
        
        pygame.display.flip()
        
        #event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    AI_PADDLE_SPEED = 2
                    selecting = False
                elif event.key == pygame.K_2:
                    AI_PADDLE_SPEED = 3
                    selecting = False
                elif event.key == pygame.K_3:
                    AI_PADDLE_SPEED = 4
                    selecting = False
                elif event.key == pygame.K_4:
                    AI_PADDLE_SPEED = 10
                    selecting = False

#main game loop
def main():
    global player_y, ai_y, ball_x, ball_y, ball_dx, ball_dy, player_score, ai_score
    
    choose_difficulty()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #player control
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= PLAYER_PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_y < HEIGHT - PADDLE_HEIGHT:
            player_y += PLAYER_PADDLE_SPEED

        #AI
        if ai_y + PADDLE_HEIGHT // 2 < ball_y:
            ai_y += AI_PADDLE_SPEED
        elif ai_y + PADDLE_HEIGHT // 2 > ball_y:
            ai_y -= AI_PADDLE_SPEED
        ai_y = max(0, min(HEIGHT - PADDLE_HEIGHT, ai_y))

        #ball movement
        ball_x += ball_dx
        ball_y += ball_dy

        #ball collision with edges
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_dy *= -1

        #ball collision with paddles
        if (player_x < ball_x < player_x + PADDLE_WIDTH and
            player_y < ball_y + BALL_SIZE and ball_y < player_y + PADDLE_HEIGHT):
            ball_dx *= -1
            ball_x = player_x + PADDLE_WIDTH
        if (ai_x < ball_x + BALL_SIZE < ai_x + PADDLE_WIDTH and
            ai_y < ball_y + BALL_SIZE and ball_y < ai_y + PADDLE_HEIGHT):
            ball_dx *= -1
            ball_x = ai_x - BALL_SIZE

        #out of bounds
        if ball_x < 0:
            ai_score += 1
            reset_ball()
        if ball_x > WIDTH:
            player_score += 1
            reset_ball()

        draw()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()