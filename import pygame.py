import pygame
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Table Tennis (Pong)')

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Paddle settings
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
player_x, player_y = 30, HEIGHT // 2 - PADDLE_HEIGHT // 2
ai_x, ai_y = WIDTH - 40, HEIGHT // 2 - PADDLE_HEIGHT // 2
PLAYER_PADDLE_SPEED = 6
AI_PADDLE_SPEED = 4  # Slower AI paddle

# Ball settings
BALL_SIZE = 16
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 4, 4  # Slower ball

# Score
player_score = 0
ai_score = 0
font = pygame.font.SysFont(None, 48)

clock = pygame.time.Clock()

def reset_ball():
    global ball_x, ball_y, ball_dx, ball_dy
    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    ball_dx *= -1
    ball_dy = 4 if ball_dy > 0 else -4

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

def main():
    global player_y, ai_y, ball_x, ball_y, ball_dx, ball_dy, player_score, ai_score
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Player controls
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player_y > 0:
            player_y -= PLAYER_PADDLE_SPEED
        if keys[pygame.K_DOWN] and player_y < HEIGHT - PADDLE_HEIGHT:
            player_y += PLAYER_PADDLE_SPEED

        # AI movement (slower)
        if ai_y + PADDLE_HEIGHT // 2 < ball_y:
            ai_y += AI_PADDLE_SPEED
        elif ai_y + PADDLE_HEIGHT // 2 > ball_y:
            ai_y -= AI_PADDLE_SPEED
        ai_y = max(0, min(HEIGHT - PADDLE_HEIGHT, ai_y))

        # Ball movement
        ball_x += ball_dx
        ball_y += ball_dy

        # Ball collision with top/bottom
        if ball_y <= 0 or ball_y >= HEIGHT - BALL_SIZE:
            ball_dy *= -1

        # Ball collision with paddles
        if (player_x < ball_x < player_x + PADDLE_WIDTH and
            player_y < ball_y + BALL_SIZE and ball_y < player_y + PADDLE_HEIGHT):
            ball_dx *= -1
            ball_x = player_x + PADDLE_WIDTH

        if (ai_x < ball_x + BALL_SIZE < ai_x + PADDLE_WIDTH and
            ai_y < ball_y + BALL_SIZE and ball_y < ai_y + PADDLE_HEIGHT):
            ball_dx *= -1
            ball_x = ai_x - BALL_SIZE

        # Ball out of bounds
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