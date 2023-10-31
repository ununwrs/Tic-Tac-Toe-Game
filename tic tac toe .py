#CHAYANAN WAREESRI CODING GAME FOR PORTFOLIO

from turtle import color
import pygame, sys
import numpy as np

pygame.init()

width = 600
height = 600
width_line = 15
board_rows=3
board_cols=3
circle_radius = 60
circle_width = 15
space = 55

 #rgb  red  green blue                  #สีพื้นหลัง
BG_color = (50, 150, 150)
line_color = (50, 50, 50)
cross_color = (66,66,66)
circle_color = (100,50,50)
cross_width = 25

screen = pygame.display.set_mode( (width, height) ) #ืทำหน้าจอ
pygame.display.set_caption( 'TIC TAC TOE' ) #ทำชื่อหน้าต่าง
screen.fill(BG_color)
board = np.zeros((board_rows,board_cols))
print(board)
#pygame.draw.line( screen, line_color, (400, 1), (400,600), 10 )#สร้างเส้น

def draw_figures():
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col]==1:
                pygame.draw.circle(screen,circle_color,(int(col * 200 +100),int(row * 200 +100)),circle_radius,circle_width)
            elif board[row][col] ==2:
                pygame.draw.line(screen,cross_color,(col*200 +space ,row * 200+200-space),(col * 200 +200 - space,row*200+space),cross_width)
                pygame.draw.line(screen,cross_color,(col*200 +space ,row * 200+space),(col * 200 +200 - space,row*200+200-space),cross_width)
def draw_line1():
    #เส้นแนวขวางที่1 
    pygame.draw.line(screen,line_color,(0,200),(600,200),width_line)
    #เส้นแนวขวางที่2
    pygame.draw.line(screen,line_color,(0,400),(600,400),width_line)
    #เส้นลากลงที่1
    pygame.draw.line(screen,line_color,(200,0),(200,600),width_line)
    #เส้นลากลงที่2
    pygame.draw.line(screen,line_color,(400,0),(400,600),width_line)
draw_line1()
def mark_square(row,col,player):
    board[row][col] = player 
def available_square(row,col):
    if board[row][col] == 0:
        return True             #return board[row][col] == 0 เขียนได้2แบบ
    else:
        return False
def is_board_full(): # เช็คว่าบอร์ดเต็มยัง
    for row in range(board_rows):
        for col in range(board_cols):
            if board[row][col] == 0:
                return False
    return True
def check_win(player):
    # vertical win check
    for col in range(board_cols):
        if board[0][col] == player and board[1][col] == player and  board[2][col] == player:
            draw_vertical_winning_line(col,player)
            return True
    for row in range(board_rows):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            draw_horizontal_winning_line(row,player)
            return True
    if board[2][0] == player and board[1][1] == player and board[0][2]==player:
        draw_asc_diagonal(player)
        return True
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        draw_desc_diagonal(player)
        return True
    return False
def draw_vertical_winning_line(col,player):
    posX =  col * 200 + 100
    if player ==1:
        color = circle_color  
    elif player ==2:
        color = cross_color
    pygame.draw.line( screen, color, (posX,15),(posX, height - 15 ), 15)
def draw_horizontal_winning_line(row,player):
    posY = row * 200 +100
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
    pygame.draw.line( screen,color, (15,posY), (width - 15, posY),15  )
def draw_asc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
    pygame.draw.line( screen,color, (15,height-15),(width - 15,15),15 )
def draw_desc_diagonal(player):
    if player == 1:
        color = circle_color
    elif player ==2:
        color = cross_color
    pygame.draw.line( screen, color, (15, 15),(width - 15, height - 15), 15)
# is the middel square availabel??
def restart():
    screen.fill( BG_color )
    draw_line1()
    player =1
    for row in range(board_rows):
        for col in range(board_cols):
            board[row][col] = 0

#print(available_square(1,1))
player = 1
game_over = True
#main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
              sys.exit()                                  
        if event.type == pygame.MOUSEBUTTONDOWN and  game_over: #ถ้าเราคลิ้กหน้าจอ
           mouseX = event.pos[0] #X
           mouseY = event.pos[1]  #Y   
           clicked_row = int(mouseY // 200)
           clicked_col = int(mouseX // 200)
           print(clicked_row)
           print(clicked_col)           
           if available_square(clicked_row,clicked_col):
                if player == 1:
                    mark_square(clicked_row,clicked_col,1)
                    draw_figures()
                    if check_win(player):
                        game_over = False
                    player = 2
                elif player == 2:
                    mark_square(clicked_row,clicked_col,2)
                    draw_figures()
                    if check_win(player):
                        game_over = False
                    player = 1
                print(board)
                print(check_win(1))
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                restart()
    
    pygame.display.update()











