''' ---------- IMPORT WORD FROM WORD LIST ---------- '''

import random, time
import words as w
import asyncio

random.seed(time.time())
L = w.word_list
word = L[random.randint(0,len(L))]


''' ---------- GAME SETTINGS ---------- '''

import pygame as pg
pg.init()

# Add in colour variables

# Set the full window width and height
win_width = 500
win_height = 700
screen = pg.display.set_mode((win_width, win_height))
pg.display.set_caption('Guess The Word')
5
white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
yellow = (250,250,0)
gray = (128,128,128)

font = pg.font.Font(None, 70)

time_font = pg.font.Font(None, 30)
start_time = pg.time.get_ticks()
get_time = False
end_time = 0
# Add in main game variables
game_board = [[' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' '],
              [' ', ' ', ' ', ' ', ' ']]



''' ---------- DRAW_BOARD FUNCTION ---------- '''
count = 0
letters = 0
winner = False
game_over = False
running = True


def draw_board():
    for col in range(5):
        for row in range(6):

            square = pg.Rect(col * 100 + 12, row * 100 + 12, 75, 75)
            pg.draw.rect(screen, white, square, width = 2)
            letter_text = font.render(game_board[row][col],True,gray)
            screen.blit(letter_text,(col*100+30,row*100+30))
    rectangle = pg.Rect(5,count*100+5,win_width-10,90)
    pg.draw.rect(screen,green,rectangle,width = 2)
            



''' ---------- CHECK_MATCH FUNCTION ---------- '''

def check_match():
    
    global game_over, winner

    for col in range(5):
        for row in range(6):
            highlight = pg.Rect(col * 100 + 12, row * 100 + 12, 75, 75)

            if word[col] == game_board[row][col] and count>row:
                 # Draw in green highlight rectangle
                 pg.draw.rect(screen,green,highlight)
            elif game_board[row][col] in word and count>row:
                pg.draw.rect(screen,yellow,highlight)
                # Draw in yellow highlight rectangle
    for row in range(6):
        guess = ''.join(game_board[row])
        if guess == word and row<count:
            game_over = True
            winner = True
##         # Join individual characters back to a single string
##         # Ends game if word guessed correctly
    


''' ---------- DRAW_WIN FUNCTION ---------- '''

        
def draw_win():
    global game_over, get_time, end_time

    if count == 6 and not winner:
        game_over = True
        text = font.render('Loser! Word: '+ word, True, white)
        screen.blit(text,(15, 610))

    if game_over and winner:
        if not get_time:
            end_time =(pg.time.get_ticks()  - start_time) / 1000
            get_time = True
        text = font.render('Winner!',True, white)
        screen.blit(text,(15, 610))
        time_text = time_font.render(f'Time:{end_time:.2f}s',True, white)
        screen.blit(time_text,(220,610))
    # Updates text on the screen



        
    



''' ---------- EVENT HANDLERS ---------- '''


async def main():

    global running, game_board, letters, count, game_over, winner, word, start_time, get_time

    while running:


        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

            if event.type == pg.TEXTINPUT and letters<5 and not game_over:
                entry = event.text
                if entry != ' 'and entry != '2'and entry != '3'and entry != '4'and entry != '5'and entry != '1':
                    game_board[count][letters] = entry
                    letters += 1

                
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE and letters>0:
                    game_board[count][letters - 1] = ' '
                    letters -= 1

                if event.key == pg.K_SPACE and not game_over:
                    count += 1
                    letters = 0
                
                if event.key == pg.K_1 and not game_over:
                    count += 1
                    letters = 0
                    game_board[count][letters] = word[0]
                    letters = 1
                if event.key == pg.K_2 and not game_over:
                    count += 1
                    letters = 1
                    game_board[count][letters] = word[1]
                    letters = 2
                if event.key == pg.K_3 and not game_over:
                    count += 1
                    letters = 2
                    game_board[count][letters] = word[2]
                    letters = 3
                if event.key == pg.K_4 and not game_over:
                    count += 1
                    letters = 3
                    game_board[count][letters] = word[3]
                    letters = 4
                if event.key == pg.K_5 and not game_over:
                    count += 1
                    letters = 4
                    game_board[count][letters] = word[4]
                    letters = 5
                    
                if event.key == pg.K_SPACE and game_over:
                    count = 0
                    letters = 0
                    game_over = False
                    winner = False
                    word = random.choice(w.word_list)
                    game_board = [[' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' '],
                                [' ', ' ', ' ', ' ', ' ']]
                    start_time = pg.time.get_ticks()
                    get_time = False


            
        screen.fill(black)
        check_match()
        draw_board()
        draw_win()

        await asyncio.sleep(0)

asyncio.run(main())