import pygame
import random
pygame.init() # initialize the pygame module
 # R G B colour code in python
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (0,0,255)
 # height and width of display screen
d_width = 600 
d_height = 500
 
d = pygame.display.set_mode((d_width, d_height))
pygame.display.set_caption('Snake Game')
 
 
snake_block = 10 # size box of snake  len=10 and width=10 
snake_speed = 15
 
font_style = pygame.font.SysFont("Arial", 25,1)
score_font = pygame.font.SysFont("comicsansms", 35,1)
 
 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, black)
    d.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(d, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    d.blit(mesg, [d_width / 6, d_height / 3])
 
 
def gameLoop():
    game_over = False
    game_close = False
 
    x1 = d_width / 2
    y1 = d_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0
 
    while not game_over:
 
        while game_close == True:
            d.fill(yellow)
            message("You Lost!   Press c for Play Again or q for Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
 
        if x1 >= d_width or x1 < 0 or y1 >= d_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        d.fill(yellow)
        pygame.draw.rect(d, blue, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]
 
        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True
 
        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
 
        pygame.display.update()
 
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, d_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, d_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1
 
        pygame.time.Clock().tick(snake_speed) # snake_speed is running speed of snake
 
    pygame.quit()
    quit()
 
gameLoop()


