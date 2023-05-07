import pygame

#initialising pygame
pygame.init()

#creating a window
win = pygame.display.set_mode((550, 550))
background_colour = (255, 255, 255)
win.fill(background_colour)
rect_color=(249, 231, 159)

pygame.display.set_caption('Tic-Tac-Toe')

#creating the grid using squares
first = pygame.draw.rect(win, rect_color, (25, 25, 150, 150))
second = pygame.draw.rect(win, rect_color, (200, 25, 150, 150))
third = pygame.draw.rect(win, rect_color, (375, 25, 150, 150))

fourth = pygame.draw.rect(win, rect_color, (25, 200, 150, 150))
fifth = pygame.draw.rect(win, rect_color, (200, 200, 150, 150))
sixth = pygame.draw.rect(win, rect_color, (375, 200, 150, 150))

seventh = pygame.draw.rect(win, rect_color, (25, 375, 150, 150))
eighth = pygame.draw.rect(win, rect_color, (200, 375, 150, 150))
ninth = pygame.draw.rect(win, rect_color, (375, 375, 150, 150))

open_1 = True
open_2 = True
open_3 = True
open_4 = True
open_5 = True
open_6 = True
open_7 = True
open_8 = True
open_9 = True

#list to check for the winner
board = [[0, 0, 0],
         [0, 0, 0],
         [0, 0, 0]]

#func to check the winner
def win_check(num):
    for row in board:
        for tile in row:
            if tile == num:
                continue
            else:
                break
        else:
            return True

    for column in range(3):
        for row in board:
            if row[column] == num:
                continue
            else:
                break
        else:
            return True

    for tile in range(3):
        if board[tile][tile] == num:
            continue
        else:
            break
    else:
        return True

    for tile in range(3):
        if board[tile][2 - tile] == num:
            continue
        else:
            break
    else:
        return True


winner = False
run = True
obj = "rect"



    
   
#main loop
while run:

    pygame.time.delay(100)  # refresh time; everytime it goes through the loop, there'll be a small delay to it
    #setting the events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # reset using spacebar
        pressed = pygame.key.get_pressed()
        
        if pressed[pygame.K_SPACE]:
            win.fill(background_colour)
            first = pygame.draw.rect(win, rect_color, (25, 25, 150, 150))
            second = pygame.draw.rect(win, rect_color, (200, 25, 150, 150))
            third = pygame.draw.rect(win, rect_color, (375, 25, 150, 150))

            fourth = pygame.draw.rect(win, rect_color, (25, 200, 150, 150))
            fifth = pygame.draw.rect(win, rect_color, (200, 200, 150, 150))
            sixth = pygame.draw.rect(win, rect_color, (375, 200, 150, 150))

            seventh = pygame.draw.rect(win, rect_color, (25, 375, 150, 150))
            eighth = pygame.draw.rect(win, rect_color, (200, 375, 150, 150))
            ninth = pygame.draw.rect(win, rect_color, (375, 375, 150, 150))
            open_1 = True
            open_2 = True
            open_3 = True
            open_4 = True
            open_5 = True
            open_6 = True
            open_7 = True
            open_8 = True
            open_9 = True
            board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
            run = True
            winner = False
            obj = "rect"

        # gets the position of the mouse cursor on the window
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if not winner:   # keeps the loop running until someone wins
                '''checks if the click happened inside of the "first" box by passing the position of cursor
                   open_1 checks if the box is empty'''
                if first.collidepoint(pos) and open_1:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (50, 50, 100, 100), 6)
                        obj = "circle"   #enables alternating usage of shapes
                        board[0][0] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (100, 100), 50, width = 6)
                        obj = "rect"
                        board[0][0] = 2
                    open_1 = False
                if second.collidepoint(pos) and open_2:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (225, 50, 100, 100), 6)
                        obj = "circle"
                        board[0][1] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (275, 100), 50, 6)
                        obj = "rect"
                        board[0][1] = 2
                    open_2 = False
                if third.collidepoint(pos) and open_3:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (400, 50, 100, 100), 6)
                        obj = "circle"
                        board[0][2] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (450, 100), 50, 6)
                        obj = "rect"
                        board[0][2] = 2
                    open_3 = False

                if fourth.collidepoint(pos) and open_4:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (50, 225, 100, 100), 6)
                        obj = "circle"
                        board[1][0] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (100, 275), 50, 6)
                        obj = "rect"
                        board[1][0] = 2
                    open_4 = False
                if fifth.collidepoint(pos) and open_5:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (225, 225, 100, 100), 6)
                        obj = "circle"
                        board[1][1] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (275, 275), 50, 6)
                        obj = "rect"
                        board[1][1] = 2
                    open_5 = False
                if sixth.collidepoint(pos) and open_6:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (400, 225, 100, 100), 6)
                        obj = "circle"
                        board[1][2] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (450, 275), 50, 6)
                        obj = "rect"
                        board[1][2] = 2
                    open_6 = False

                if seventh.collidepoint(pos) and open_7:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (50, 400, 100, 100), 6)
                        obj = "circle"
                        board[2][0] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (100, 450), 50, 6)
                        obj = "rect"
                        board[2][0] = 2
                    oepn_7 = False
                if eighth.collidepoint(pos) and open_8:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (225, 400, 100, 100), 6)
                        obj = "circle"
                        board[2][1] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (275, 450), 50, 6)
                        obj = "rect"
                        board[2][1] = 2
                    open_8 = False
                if ninth.collidepoint(pos) and open_9:
                    if obj == "rect":
                        pygame.draw.rect(win, (133, 193, 233), (400, 400, 100, 100), 6)
                        obj = "circle"
                        board[2][2] = 1
                    else:
                        pygame.draw.circle(win, (245, 183, 177), (450, 450), 50, 6)
                        obj = "rect"
                        board[2][2] = 2
                    open_9 = False
    # calling the function to disable marking shapes after a winner has been found
                if win_check(1):
                 winner = True
                 win.fill((133, 193, 233))
                 font = pygame.font.SysFont("arial", 72)
                 text = font.render("Blue Wins", True, (0, 128, 0))
                 win.blit(text,( 550 // 4, 550// 2))
                

                if win_check(2):
                 winner = True
                 win.fill((245, 183, 177))
                 
                 font = pygame.font.SysFont("arial", 72)
                 text = font.render("Pink Wins", True, (0, 128, 0))
                 win.blit(text,(550 // 4, 550 // 2))
        

   

    pygame.display.update()
    ''' whenever new things happen on the screen/ events take place, 
                                itll bring them in front so that it's actually visible '''

pygame.quit()
 