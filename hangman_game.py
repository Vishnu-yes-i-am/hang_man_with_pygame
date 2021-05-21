import pygame,sys
import time
import string
import random
from PIL import Image
pygame.init()
display=pygame.display.set_mode((1540,800))
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)
pygame.display.set_caption('My First Game-By Vishnu Mali')
clock = pygame.time.Clock() 
font=pygame.font.SysFont("Serif",22)
font2=pygame.font.SysFont("Serif",28)
#----------------------------------------------------------------------------------------
IMAGES = [r"step0.jpg",r"step1.jpg",r"step2.jpg",r"step3.jpg",r"step4.jpg",r"step5.jpg",r"step6.jpg",r"death.jpg"]
def load_words(): 
    F = open("easywords.txt", 'r')
    line = F.readline()
    word_list = line.split(" ")
    return word_list
def choose_word():
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word
def is_word_guessed(secret_word, letters_guessed,sourav):
    if len(secret_word)==sourav:
        return True
    return False
def get_guessed_word(secret_word, letters_guessed):
    index = 0
    guessed_word = ""
    while (index < len(secret_word)):
        if secret_word[index] in letters_guessed:
            guessed_word += secret_word[index]
        else:
            guessed_word += "_"
        index += 1
    return guessed_word
def get_available_letters(letters_guessed):
    letters_left = list(string.ascii_lowercase)
    for el in letters_guessed:
        letters_left.remove(el)
    return letters_left
def hangman(secret_word):
    display.blit(font.render("Starting The Game.Please  wait...", True, blue), (250,670))
    display.blit(pygame.image.load("logo.png"),(250,0))
    pygame.display.update()
    pygame.time.wait(2*1000)
    newgame=True
    rect1=pygame.Rect(150, 150, 70, 50)
    won=0
    lose=0
    while  newgame:
        secret_word = choose_word()
        display.fill(white)
        color=white
        display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
        msg2="Welcome to the game, Hangman!.I am thinking of a word that is "+str(len(secret_word))+ " letters long."
        display.blit(font.render(msg2, True, blue), (80,100))
        pygame.display.update()
        pygame.time.wait(1*1000)
        letters_guessed = []
        imagecount=0
        sourav=0
        gamefinish=False
        while imagecount<=len(IMAGES) and not gamefinish:      
            available_letters = get_available_letters(letters_guessed)
            display.blit(font.render("Available letters are =="+str(available_letters), True, blue), (50,150))
            pygame.display.update()
            guess=''
            letter=""
            apple=True
            while apple:
                for el in pygame.event.get():
                    if el.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                    if el.type==pygame.KEYDOWN:
                        if el.key==pygame.K_BACKSPACE:
                            display.fill(color)
                            display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                            display.blit(font.render("Available letters are =="+str(available_letters), True, blue), (50,150))
                            pygame.display.update()
                            guess=guess[:-1]
                        elif el.key==pygame.K_RETURN:
                            if len(guess)==1:
                                letter=guess
                                apple=False
                                break 
                            else:
                                display.fill(white)
                                display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                                display.blit(font.render("Enter a single letter only", True, red), (50,100))
                                pygame.display.update()
                                pygame.time.wait(2*1000)
                                guess=''  
                        else:                            
                            guess += el.unicode
                display.blit(font2.render("guess a letter------>"+guess, True,(0,0,0)), (100,400))   
                pygame.display.flip()
            
            if letter not in available_letters:
                display.fill(white)
                color=white
                display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                status="This letter is already guessed you can't guess it again.Try again with a different letter."
                display.blit(font.render(status, True, red), (50,200))
                display.blit(font.render("you gussed word till now as :---> "+get_guessed_word(secret_word, letters_guessed), True, blue), (50,250))
                pygame.display.update()
                continue
            if letter in secret_word:
                letters_guessed.append(letter)
                sourav+=secret_word.count(letter)
                display.fill(green)
                display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                color=green
                display.blit(font.render("Ohh Yeah ! Good Guess:-).Keep it up :--->  "+get_guessed_word(secret_word, letters_guessed), True, blue), (50,250))
                if is_word_guessed(secret_word, letters_guessed,sourav) == True:
                    status2=" * * Congratulations, you won! * * "
                    display.fill(pygame.Color(255,255,0))
                    display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                    display.blit(font2.render(status2, True, blue), (50,50))
                    display.blit(pygame.image.load("won.jpg"),(100,180))
                    gamefinish=True
                    display.blit(font2.render("Press 'y' to play again else press 'n'", True, green), (140,130))
                    display.blit(font.render("You are a Champion.The word was :---> "+get_guessed_word(secret_word, letters_guessed), True, blue), (50,100))
                    won+=1
                    pygame.display.update()
                    pygame.time.wait(1*1000)
                    newgame=False
                    banana=True
                    while banana:
                        for el in pygame.event.get():
                            if el.type==pygame.QUIT:
                                pygame.quit()
                                quit()
                            if el.type==pygame.KEYDOWN:
                                if el.key==pygame.K_y:
                                    newgame=True
                                    banana=False
                                    break  
                                elif  el.key==pygame.K_n:                            
                                    pygame.quit()  
                                    quit()
            else:
                display.fill(red)
                color=red
                display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                display.blit(font.render("Oops! That letter is not in my word: ---> "+get_guessed_word(secret_word, letters_guessed), True, blue), (50,250))
                letters_guessed.append(letter)
                display.blit(pygame.image.load(IMAGES[imagecount]),(500,350))
                pygame.display.update()
                imagecount+=1
                if imagecount>=len(IMAGES):
                    display.fill(white)
                    display.blit(font.render("WON: "+ str(won) +"   LOSE: "+str(lose), True, blue), (1100,100))
                    display.blit(font2.render("The Word i thinking was:---->"+secret_word, True, red), (180,150))
                    display.blit(font2.render("YOU LOOSE . NOW SHUT YOUR SHITTY MOUTH AND GO AWAY", True, red), (180,200))
                    display.blit(pygame.image.load(IMAGES[-1]),(350,300))
                    gamefinish=True
                    lose+=1
                    display.blit(font2.render("Press 'y' to play again else press 'n'", True, green), (180,250))
                    pygame.display.update()
                    pygame.time.wait(1*1000)
                    newgame=False
                    banana=True
                    while banana:
                        for el in pygame.event.get():
                            if el.type==pygame.QUIT:
                                pygame.quit()
                                quit()
                            if el.type==pygame.KEYDOWN:
                                if el.key==pygame.K_y:
                                    newgame=True  
                                    banana=False
                                    break
                                elif  el.key==pygame.K_n:                            
                                    pygame.quit()  
                                    quit()
while True: 
    display.fill(white)
    secret_word = choose_word()
    hangman(secret_word)
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:  
            pygame.quit()     
            quit()    
        pygame.display.update() 