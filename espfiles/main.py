import ssd1306
import machine
from serialtalk.auto import SerialTalk

# Set up the display
display = ssd1306.SSD1306_I2C(128, 64, machine.SoftI2C(scl=4, sda=5))

# Set up the paddles
PAD_SIZE = 15
def pads(a, b):
    global paddle_a_y, paddle_b_y
    paddle_a_y = max(0, min(a, 64 - PAD_SIZE))
    paddle_b_y = max(0, min(b, 64 - PAD_SIZE))
pads(0,0)

# Set up the ball
BASE_SPEED = 1
def reset_ball():
    global ball_dx, ball_dy, ball_x, ball_y
    ball_x = 64
    ball_y = 32
    ball_dx = BASE_SPEED
    ball_dy = BASE_SPEED
reset_ball()

# Reset score
def reset_score():
    global score
    score = [0,0]
reset_score()

# Main game loop
while True:
    # Update the paddles
    # Auto mode
    pads(ball_y-7, ball_y-7)

    # Update the ball
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with the paddles
    if ball_x < 10:
        if paddle_a_y < ball_y < paddle_a_y + PAD_SIZE:
            ball_dx *= -1
    elif ball_x > 122:
        if paddle_b_y < ball_y < paddle_b_y + PAD_SIZE:
            ball_dx *= -1

    # Check for collisions with the walls
    if ball_y < 0 or ball_y > 64:
        ball_dy *= -1

    # Clear the display
    display.fill(0)

    # Draw the paddles
    display.rect(0, paddle_a_y, 5, PAD_SIZE, 1)
    display.rect(122, paddle_b_y, 5, PAD_SIZE, 1)

    # Draw the ball
    display.rect(ball_x, ball_y, 3, 3, 1)

    # Update the display
    display.show()
