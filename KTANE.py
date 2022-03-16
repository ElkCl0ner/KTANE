import pygame
from random import randint
from random import choice

#--Initiate Pygame--#
pygame.init()
display_width = 1400
display_heigth = 700
font = pygame.font.SysFont("defusedextended", 72)
display = pygame.display.set_mode((display_width,display_heigth))
pygame.display.set_caption("Keep Talking and Nobody Explodes")
clock = pygame.time.Clock()

#--Initiate Variables--#
dead = False
close = False
won = False
strikes = 0
time_left = 181
prev_time = 0
prev_strikes = 0
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
serial_number = str(randint(0,9))
serial_number += alphabet[randint(0,25)]
serial_number += str(randint(0,9))
serial_number += alphabet[randint(0,25)]
serial_number += alphabet[randint(0,25)]
serial_number += str(randint(0,9))

#Colors
white = (255,255,255)
black = (0,0,0)

#--Initiate Images--#
moduleImg = pygame.image.load('Grey Module.png')
backgroundImg = pygame.image.load('Background.png')
strike = font.render("X",False,(255,0,0))
label = pygame.image.load('Label.png')

#--Set Modules--#
origins = [250,50,550,50,850,50,250,350,550,350,850,350]
modules = [0,2,4,6,8,10]

timer_origin = modules.pop(randint(0,5))
wires_origin = modules.pop(randint(0,4))
button_origin = modules.pop(randint(0,3))
keypads_origin = modules.pop(randint(0,2))
simon_origin = modules.pop(randint(0,1))
first_origin = modules.pop(0)

wires_defused = False
keypads_defused = False
simon_defused = True
who_defused = False
button_defused = True

#--Modules--#
#Wires
#Initiate Variables
colors = ['red','blue','white','yellow','black']

#Color of Wires(3 - 6)
num_wires = randint(3,6)

wires = [choice(colors),choice(colors),choice(colors)]

if num_wires > 3:
    wires.append(choice(colors))
    
if num_wires > 4:
    wires.append(choice(colors))
    
if num_wires > 5:
    wires.append(choice(colors))

#Determine Wire Stats
red = 0
blue = 0
white = 0
yellow = 0
black = 0

for wire in wires:
    if wire == 'red':
        red += 1
    if wire == 'blue':
        blue += 1
    if wire == 'white':
        white += 1
    if wire == 'yellow':
        yellow += 1
    if wire == 'black':
        black += 1

#Wire wires_solution
if num_wires == 3:
    if red == 0:
        wires_solution = 2
    elif wires[2] == 'white':
        wires_solution = 3
    elif blue > 1:
        if wires[2] == 'blue':
            wires_solution = 3
        else:
            wires_solution = 2
    else:
        wires_solution = 3

elif num_wires == 4:
    if red > 1 and int(serial_number[len(serial_number) - 1]) % 2 == 1:
        if wires[3] == 'red':
            wires_solution = 4
        elif wires[2] == 'red':
            wires_solution = 3
        else:
            wires_solution = 2
    elif wires[3] == 'yellow' and red == 0:
        wires_solution = 1
    elif blue == 1:
        wires_solution = 1
    elif yellow > 1:
        wires_solution = 4
    else:
        wires_solution = 2

elif num_wires == 5:
    if wires[4] == 'black' and int(serial_number[len(serial_number) - 1]) % 2 == 1:
        wires_solution = 4
    elif red == 1 and yellow > 1:
        wires_solution = 1
    elif black == 0:
        wires_solution = 2
    else:
        wires_solution = 1

else:
    if yellow == 0 and int(serial_number[len(serial_number) - 1]) % 2 == 1:
        wires_solution = 3
    elif yellow == 1 and white > 1:
        wires_solution = 4
    elif red == 0:
        wires_solution = 6
    else:
        wires_solution = 4
wires_y = [50,90,130,170,210,250]
wires_Img = []

#Keypads
c1 = ["Q", "AT", "ppl", "N", "complex", "H", "C-dot-inversed"]
c2 = ["E", "Q", "C-dot-inversed", "fancy_Q", "star", "H", "?"]
c3 = ["copy", "W", "fancy_Q", "double_K", "R", "ppl", "star"]
c4 = ["6", "para", "PT", "complex", "double_K", "?", "smiley"]
c5 = ["tri", "smiley", "PT", "C-dot", "para", "3", "STAR"]
c6 = ["6", "E", "not=", "ae", "tri", "kitchen", "omega"]
c = [c1,c2,c3,c4,c5,c6]

which_c = randint(0,5)

c_list = [c[which_c][0],c[which_c][1],c[which_c][2],c[which_c][3],c[which_c][4],c[which_c][5],c[which_c][6]]

s1 = choice(c_list)
c_list.remove(s1)
s2 = choice(c_list)
c_list.remove(s2)
s3 = choice(c_list)
c_list.remove(s3)
s4 = choice(c_list)
symbols = [s1,s2,s3,s4]

#keypads_solution
keypads_solution = [s1]

if c[which_c].index(keypads_solution[0]) < c[which_c].index(s2):
    keypads_solution.append(s2)
else:
    keypads_solution.insert(0,s2)

if c[which_c].index(keypads_solution[0]) > c[which_c].index(s3):
    keypads_solution.insert(0,s3)
elif c[which_c].index(keypads_solution[1]) > c[which_c].index(s3):
    keypads_solution.insert(1,s3)
else:
    keypads_solution.append(s3)

if c[which_c].index(keypads_solution[0]) > c[which_c].index(s4):
    keypads_solution.insert(0,s4)
elif c[which_c].index(keypads_solution[1]) > c[which_c].index(s4):
    keypads_solution.insert(1,s4)
elif c[which_c].index(keypads_solution[2]) > c[which_c].index(s4):
    keypads_solution.insert(2,s4)
else:
    keypads_solution.append(s4)

keypads_pos = [40,60,40,160,140,60,140,160]
ks = 0

#Simon
colors = ["blue", "yellow", "red", "green"]
randomcolors = [choice(colors),choice(colors),choice(colors),choice(colors)]
solution0 = []
solution1 = []
solution2 = []
# solution
if alphabet.index(serial_number[1]) < 6 or alphabet.index(serial_number[3]) < 6 or alphabet.index(serial_number[4]) < 6:
    for c in randomcolors:
        if c == "red":
            solution0.append("blue")
            solution1.append("yellow")
            solution2.append("green")
        elif c == "blue":
            solution0.append("red")
            solution1.append("green")
            solution2.append("red")
        elif c == "green":
            solution0.append("yellow")
            solution1.append("blue")
            solution2.append("yellow")
        elif c == "yellow":
            solution0.append("green")
            solution1.append("red")
            solution2.append("blue")
        
else:
    for c in randomcolors:
        if c == "red":
            solution0.append("blue")
            solution1.append("red")
            solution2.append("yellow")
        elif c == "blue":
            solution0.append("yellow")
            solution1.append("blue")
            solution2.append("green")
        elif c == "green":
            solution0.append("green")
            solution1.append("yellow")
            solution2.append("blue")
        elif c == "yellow":
            solution0.append("red")
            solution1.append("green")
            solution2.append("red")

#Who
def who():
    #--STEP 1--#
    random_display = ['YES','FIRST','DISPLAY','OKAY','SAYS','NOTHING','','BLANK','NO','LED','LEAD','READ','RED','REED','LEED','HOLD ON','YOU','YOU ARE','YOUR',"YOU'RE",'UR','THERE',"THEY'RE",'THEIR','THEY ARE','SEE','C','CEE']

    not_display = choice(random_display)


    if not_display is 'UR':
        case = 0
    elif not_display is 'YES' or not_display is 'NOTHING' or not_display is 'LED' or not_display is 'THEY ARE':
        case = 1
    elif not_display is '' or not_display is 'REED' or not_display is 'LEED' or not_display is "THEY'RE":
        case = 2
    elif not_display is 'FIRST' or not_display is 'OKAY' or not_display is 'C':
        case = 3
    elif not_display is 'BLANK' or not_display is 'READ' or not_display is 'RED' or not_display is 'YOU' or not_display is 'YOUR' or not_display is "YOU'RE" or not_display is "THEIR" :
        case = 4
    else :
        case = 5

    #--STEP 2--#

    #Variables

    ready_list = ['YES','OKAY','WHAT','MIDDLE','LEFT','PRESS','RIGHT','BLANK','READY','NO','FIRST','UHHH','NOTHING','WAIT']
    first_list = ['LEFT','OKAY','YES','MIDDLE','NO','RIGHT','NOTHING','UHHH','WAIT','READY','BLANK','WHAT','PRESS','FIRST']
    no_list = ['BLANK','UHHH','WAIT','FIRST','WHAT','READY','RIGHT','YES','NOTHING','LEFT','PRESS','OKAY','NO','MIDDLE']
    blank_list = ['WAIT','RIGHT','OKAY','MIDDLE','BLANK','PRESS','READY','NOTHING','NO','WHAT','LEFT','UHHH','YES','FIRST']
    nothing_list = ['UHHH','RIGHT','OKAY','MIDDLE','YES','BLANK','NO','PRESS','LEFT','WHAT','WAIT','FIRST','NOTHING','READY']
    yes_list = ['OKAY','RIGHT','UHHH','MIDDLE','FIRST','WHAT','PRESS','READY','NOTHING','YES','LEFT','BLANK','NO','WAIT']
    what_list = ['UHHH','WHAT','LEFT','NOTHING','READY','BLANK','MIDDLE','NO','OKAY','FIRST','WAIT','YES','PRESS','RIGHT']
    uhhh_list = ['READY','NOTHING','LEFT','WHAT','OKAY','YES','RIGHT','NO','PRESS','BLANK','UHHH','MIDDLE','WAIT','FIRST']
    left_list = ['RIGHT','LEFT','FIRST','NO','MIDDLE','YES','BLANK','WHAT','UHHH','WAIT','PRESS','READY','OKAY','NOTHING']
    right_list = ['YES','NOTHING','READY','PRESS','NO','WAIT','WHAT','RIGHT','MIDDLE','LEFT','UHHH','BLANK','OKAY','FIRST']
    middle_list = ['BLANK','READY','OKAY','WHAT','NOTHING','PRESS','NO','WAIT','LEFT','MIDDLE','RIGHT','FIRST','UHHH','YES']
    okay_list = ['MIDDLE','NO','FIRST','YES','UHHH','NOTHING','WAIT','OKAY','LEFT','READY','BLANK','PRESS','WHAT','RIGHT']
    wait_list = ['UHHH','NO','BLANK','OKAY','YES','LEFT','FIRST','PRESS','WHAT','WAIT','NOTHING','READY','RIGHT','MIDDLE']
    press_list = ['RIGHT','MIDDLE','YES','READY','PRESS','OKAY','NOTHING','UHHH','BLANK','LEFT','FIRST','WHAT','NO','WAIT']
    you_list = ['SURE','YOU ARE','YOUR',"YOU'RE",'NEXT','UH HUH','UR','HOLD','WHAT?','YOU','UH UH','LIKE','DONE','U']
    youare_list = ['YOUR','NEXT','LIKE','UH HUH','WHAT?','DONE','UH UH','HOLD','YOU','U',"YOU'RE",'SURE','UR','YOU ARE']
    your_list = ['UH UH','YOU ARE','UH HUH','YOUR','NEXT',"UR",'SURE','U',"YOU'RE",'YOU','WHAT?','HOLD','LIKE','DONE']
    youre_list = ['YOU',"YOU'RE",'UR','NEXT','UH UH','YOU ARE','U','YOUR','WHAT?','UH HUH','SURE','DONE','LIKE','HOLD']
    ur_list = ['DONE','U','UR','UH HUH','WHAT?','SURE','YOUR','HOLD',"YOU'RE",'LIKE','NEXT','UH UH','YOU ARE','YOU']
    u_list = ['UH HUH','SURE','NEXT','WHAT?',"YOU'RE",'UR','UH UH','DONE','U','YOU','LIKE','HOLD','YOU ARE','YOUR']
    uhhuh_list = ['UH HUH','YOUR','YOU ARE','YOU','DONE','HOLD','UH UH','NEXT','SURE','LIKE',"YOU'RE",'UR','U','WHAT?']
    uhuh_list = ['UR','U','YOU ARE',"YOU'RE",'NEXT','UH UH','DONE','YOU','UH HUH','LIKE','YOUR','SURE','HOLD','WHAT?']
    whatoops_list = ['YOU','HOLD',"YOU'RE",'YOUR','U','DONE','UH UH','LIKE','YOU ARE','UH HUH','UR','NEXT','WHAT?','SURE']
    done_list = ['SURE','UH HUH','NEXT','WHAT?','YOUR','UR',"YOU'RE",'HOLD','LIKE','YOU','U','YOU ARE','UH UH','DONE']
    next_list = ['WHAT?','UH HUH','UH UH','YOUR','HOLD','SURE','NEXT','LIKE','DONE','YOU ARE','UR',"YOU'RE",'U','YOU']
    hold_list = ['YOU ARE','U','DONE','UH UH','YOU','UR','SURE','WHAT?',"YOU'RE",'NEXT','HOLD','UH HUH','YOUR','LIKE']
    sure_list = ['YOU ARE','DONE','LIKE',"YOU'RE",'YOU','HOLD','UH HUH','UR','SURE','U','WHAT?','NEXT','YOUR','UH UH']
    like_list = ["YOU'RE",'NEXT','U','UR','HOLD','DONE','UH UH','WHAT?','UH HUH','YOU','LIKE','SURE','YOU ARE','YOUR']

    label_list = [ready_list,first_list,no_list,blank_list,nothing_list,yes_list,what_list,uhhh_list,left_list,right_list,middle_list,okay_list,wait_list,press_list,you_list,youare_list,your_list,youre_list,ur_list,u_list,uhhuh_list,uhuh_list,whatoops_list,done_list,next_list,hold_list,sure_list,like_list]

    first_word = ['READY','FIRST','NO','BLANK','NOTHING','YES','WHAT','UHHH','LEFT','RIGHT','MIDDLE','OKAY','WAIT','PRESS','YOU','YOU ARE','YOUR',"YOU'RE",'UR','U','UH HUH','UH UH','WHAT?','DONE','NEXT','HOLD','SURE','LIKE']

    random_label = choice(label_list)
    minus_label = []
    for x in random_label:
        minus_label.append(x)

    minus_label.remove(first_word[label_list.index(random_label)])
    six_words = [choice(minus_label)]
    minus_label.remove(six_words[0])
    six_words.append(choice(minus_label))
    minus_label.remove(six_words[1])
    six_words.append(choice(minus_label))
    minus_label.remove(six_words[2])
    six_words.append(choice(minus_label))
    minus_label.remove(six_words[3])
    six_words.append(choice(minus_label))
    minus_label.remove(six_words[4])


    six_words.insert(case,first_word[label_list.index(random_label)])

    last_order = 100
    for x in six_words:
        order = random_label.index(x)
        if order < last_order:
            word_solution = x
            last_order = order

    return [not_display,six_words,six_words.index(word_solution)]#returns [str,array,int]

whodat = [who(),who(),who()]
who_at = 0

#--Main Loop--#
while not dead and not close and not won:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse = pygame.mouse.get_pos()
            #Wires
            if not wires_defused:
                if origins[wires_origin]+50 <= mouse[0] <= origins[wires_origin]+250 and origins[wires_origin+1]+wires_y[0] <= mouse[1] <= origins[wires_origin+1]+wires_y[0]+10:
                    wires_answer = 1
                    if wires_answer == wires_solution:
                        wires_defused = True
                    else:
                        strikes +=1
                elif origins[wires_origin]+50 <= mouse[0] <= origins[wires_origin]+250 and origins[wires_origin+1]+wires_y[1] <= mouse[1] <= origins[wires_origin+1]+wires_y[1]+10:
                    wires_answer = 2
                    if wires_answer == wires_solution:
                        wires_defused = True
                    else:
                        strikes +=1
                elif origins[wires_origin]+50 <= mouse[0] <= origins[wires_origin]+250 and origins[wires_origin+1]+wires_y[2] <= mouse[1] <= origins[wires_origin+1]+wires_y[2]+10:
                    wires_answer = 3
                    if wires_answer == wires_solution:
                        wires_defused = True
                    else:
                        strikes +=1
                if num_wires > 3:
                    if origins[wires_origin]+50 <= mouse[0] <= origins[wires_origin]+250 and origins[wires_origin+1]+wires_y[3] <= mouse[1] <= origins[wires_origin+1]+wires_y[3]+10:
                        wires_answer = 4
                        if wires_answer == wires_solution:
                            wires_defused = True
                        else:
                            strikes +=1
                if num_wires > 4:
                    if origins[wires_origin]+50 <= mouse[0] <= origins[wires_origin]+250 and origins[wires_origin+1]+wires_y[4] <= mouse[1] <= origins[wires_origin+1]+wires_y[4]+10:
                        wires_answer = 5
                        if wires_answer == wires_solution:
                            wires_defused = True
                        else:
                            strikes +=1
                if num_wires > 5:
                    if origins[wires_origin]+50 <= mouse[0] <= origins[wires_origin]+250 and origins[wires_origin+1]+wires_y[5] <= mouse[1] <= origins[wires_origin+1]+wires_y[5]+10:
                        wires_answer = 6
                        if wires_answer == wires_solution:
                            wires_defused = True
                        else:
                            strikes +=1

            #Keypads
            if not keypads_defused:
                if origins[keypads_origin]+40 <= mouse[0] <= origins[keypads_origin]+140 and origins[keypads_origin+1]+60 <= mouse[1] <= origins[keypads_origin+1]+160:
                    keypads_answer = 0
                    if keypads_answer == symbols.index(keypads_solution[ks]):
                        if ks == 3:
                            keypads_defused = True
                        else:
                            ks += 1
                    else:
                        strikes += 1
                elif origins[keypads_origin]+40 <= mouse[0] <= origins[keypads_origin]+140 and origins[keypads_origin+1]+160 <= mouse[1] <= origins[keypads_origin+1]+260:
                    keypads_answer = 1
                    if keypads_answer == symbols.index(keypads_solution[ks]):
                        if ks == 3:
                            keypads_defused = True
                        else:
                            ks += 1
                    else:
                        strikes += 1
                elif origins[keypads_origin]+140 <= mouse[0] <= origins[keypads_origin]+240 and origins[keypads_origin+1]+60 <= mouse[1] <= origins[keypads_origin+1]+160:
                    keypads_answer = 2
                    if keypads_answer == symbols.index(keypads_solution[ks]):
                        if ks == 3:
                            keypads_defused = True
                        else:
                            ks += 1
                    else:
                        strikes += 1
                elif origins[keypads_origin]+140 <= mouse[0] <= origins[keypads_origin]+240 and origins[keypads_origin+1]+160 <= mouse[1] <= origins[keypads_origin+1]+260:
                    keypads_answer = 3
                    if keypads_answer == symbols.index(keypads_solution[ks]):
                        if ks == 3:
                            keypads_defused = True
                        else:
                            ks += 1
                    else:
                        strikes += 1

            #Who
            if not who_defused:
                if origins[first_origin]+20 <= mouse[0] <= origins[first_origin]+120 and origins[first_origin+1]+100 <= mouse[1] <= origins[first_origin+1]+130:
                    first_answer = 0
                    if first_answer == whodat[who_at][2]:
                        who_at += 1
                        if who_at == 3:
                            who_defused = True
                            who_at -= 1
                    else:
                        strikes += 1
                elif origins[first_origin]+20 <= mouse[0] <= origins[first_origin]+120 and origins[first_origin+1]+160 <= mouse[1] <= origins[first_origin+1]+190:
                    first_answer = 1
                    if first_answer == whodat[who_at][2]:
                        who_at += 1
                        if who_at == 3:
                            who_defused = True
                            who_at -= 1
                    else:
                        strikes += 1
                elif origins[first_origin]+20 <= mouse[0] <= origins[first_origin]+120 and origins[first_origin+1]+220 <= mouse[1] <= origins[first_origin+1]+250:
                    first_answer = 2
                    if first_answer == whodat[who_at][2]:
                        who_at += 1
                        if who_at == 3:
                            who_defused = True
                            who_at -= 1
                    else:
                        strikes += 1
                elif origins[first_origin]+150 <= mouse[0] <= origins[first_origin]+250 and origins[first_origin+1]+100 <= mouse[1] <= origins[first_origin+1]+130:
                    first_answer = 3
                    if first_answer == whodat[who_at][2]:
                        who_at += 1
                        if who_at == 3:
                            who_defused = True
                            who_at -= 1
                    else:
                        strikes += 1
                elif origins[first_origin]+150 <= mouse[0] <= origins[first_origin]+250 and origins[first_origin+1]+160 <= mouse[1] <= origins[first_origin+1]+190:
                    first_answer = 4
                    if first_answer == whodat[who_at][2]:
                        who_at += 1
                        if who_at == 3:
                            who_defused = True
                            who_at -= 1
                    else:
                        strikes += 1
                elif origins[first_origin]+150 <= mouse[0] <= origins[first_origin]+250 and origins[first_origin+1]+220 <= mouse[1] <= origins[first_origin+1]+250:
                    first_answer = 5
                    if first_answer == whodat[who_at][2]:
                        who_at += 1
                        if who_at == 3:
                            who_defused = True
                            who_at -= 1
                    else:
                        strikes += 1
                        

    display.blit(backgroundImg,(0,0))
    #Wires
    display.blit(moduleImg,(origins[wires_origin],origins[wires_origin+1]))
    display.blit(font.render(serial_number,False,(0,0,0)),(0,650))
    wires_at = 0
    for w in wires:
        if w == 'red':
            pygame.draw.rect(display,(255,0,0),(origins[wires_origin]+50,origins[wires_origin+1]+wires_y[wires_at],200,10))
        if w == 'blue':
            pygame.draw.rect(display,(0,0,255),(origins[wires_origin]+50,origins[wires_origin+1]+wires_y[wires_at],200,10))
        if w == 'white':
            pygame.draw.rect(display,(255,255,255),(origins[wires_origin]+50,origins[wires_origin+1]+wires_y[wires_at],200,10))
        if w == 'yellow':
            pygame.draw.rect(display,(255,211,0),(origins[wires_origin]+50,origins[wires_origin+1]+wires_y[wires_at],200,10))
        if w == 'black':
            pygame.draw.rect(display,(0,0,0),(origins[wires_origin]+50,origins[wires_origin+1]+wires_y[wires_at],200,10))
        wires_at += 1

    #Keypads
    display.blit(moduleImg,(origins[keypads_origin],origins[keypads_origin+1]))
    keypads_at = 0
    for s in symbols:
        if s == 'Q':
            display.blit(pygame.image.load('Q.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'AT':
            display.blit(pygame.image.load('AT.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'ppl':
            display.blit(pygame.image.load('ppl.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'N':
            display.blit(pygame.image.load('N.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'complex':
            display.blit(pygame.image.load('complex.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'H':
            display.blit(pygame.image.load('H.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'C-dot-inversed':
            display.blit(pygame.image.load('C-dot-inversed.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'E':
            display.blit(pygame.image.load('E.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'fancy_Q':
            display.blit(pygame.image.load('fancy_Q.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'star':
            display.blit(pygame.image.load('star.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == '?':
            display.blit(pygame.image.load('oopsie.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'copy':
            display.blit(pygame.image.load('copy.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'W':
            display.blit(pygame.image.load('W.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'double_K':
            display.blit(pygame.image.load('double_K.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'R':
            display.blit(pygame.image.load('R.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == '6':
            display.blit(pygame.image.load('6.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'para':
            display.blit(pygame.image.load('para.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'PT':
            display.blit(pygame.image.load('PT.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'smiley':
            display.blit(pygame.image.load('smiley.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'tri':
            display.blit(pygame.image.load('tri.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'STAR':
            display.blit(pygame.image.load('star-f.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'C-dot':
            display.blit(pygame.image.load('C-dot.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'not=':
            display.blit(pygame.image.load('not=.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'ae':
            display.blit(pygame.image.load('ae.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'kitchen':
            display.blit(pygame.image.load('kitchen.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == 'omega':
            display.blit(pygame.image.load('omega.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        elif s == '3':
            display.blit(pygame.image.load('3.png'),(origins[keypads_origin]+keypads_pos[keypads_at],origins[keypads_origin+1]+keypads_pos[keypads_at+1]))
        keypads_at += 2

    #Simon
    display.blit(moduleImg,(origins[simon_origin],origins[simon_origin+1]))
    pygame.draw.rect(display,(150,0,0),(origins[simon_origin]+40,origins[simon_origin+1]+60,100,100))
    pygame.draw.rect(display,(0,0,150),(origins[simon_origin]+40,origins[simon_origin+1]+160,100,100))
    pygame.draw.rect(display,(0,150,0),(origins[simon_origin]+140,origins[simon_origin+1]+60,100,100))
    pygame.draw.rect(display,(150,150,0),(origins[simon_origin]+140,origins[simon_origin+1]+160,100,100))

    #Who
    font = pygame.font.SysFont("rockwell", 26)
    display.blit(moduleImg,(origins[first_origin],origins[first_origin+1]))
    display.blit(font.render(str(whodat[who_at][0]),False,(0,0,0)),(origins[first_origin]+20,origins[first_origin+1]+40))
    font = pygame.font.SysFont("rockwell", 18)
    display.blit(label,(origins[first_origin]+20,origins[first_origin+1]+100))
    display.blit(label,(origins[first_origin]+20,origins[first_origin+1]+160))
    display.blit(label,(origins[first_origin]+20,origins[first_origin+1]+220))
    display.blit(label,(origins[first_origin]+150,origins[first_origin+1]+100))
    display.blit(label,(origins[first_origin]+150,origins[first_origin+1]+160))
    display.blit(label,(origins[first_origin]+150,origins[first_origin+1]+220))
    display.blit(font.render(str(whodat[who_at][1][0]),False,(0,0,0)),(origins[first_origin]+20,origins[first_origin+1]+100))
    display.blit(font.render(str(whodat[who_at][1][1]),False,(0,0,0)),(origins[first_origin]+20,origins[first_origin+1]+160))
    display.blit(font.render(str(whodat[who_at][1][2]),False,(0,0,0)),(origins[first_origin]+20,origins[first_origin+1]+220))
    display.blit(font.render(str(whodat[who_at][1][3]),False,(0,0,0)),(origins[first_origin]+150,origins[first_origin+1]+100))
    display.blit(font.render(str(whodat[who_at][1][4]),False,(0,0,0)),(origins[first_origin]+150,origins[first_origin+1]+160))
    display.blit(font.render(str(whodat[who_at][1][5]),False,(0,0,0)),(origins[first_origin]+150,origins[first_origin+1]+220))

    #Button
    display.blit(moduleImg,(origins[button_origin],origins[button_origin+1]))

    #Defused
    if wires_defused:
        pygame.draw.circle(display,(0,255,0),(origins[wires_origin]+257,origins[wires_origin+1]+35),13)
    if button_defused:
        pygame.draw.circle(display,(0,255,0),(origins[button_origin]+257,origins[button_origin+1]+35),13)
    if who_defused:
        pygame.draw.circle(display,(0,255,0),(origins[first_origin]+257,origins[first_origin+1]+35),13)
    if keypads_defused:
        pygame.draw.circle(display,(0,255,0),(origins[keypads_origin]+257,origins[keypads_origin+1]+35),13)
    if simon_defused:
        pygame.draw.circle(display,(0,255,0),(origins[simon_origin]+257,origins[simon_origin+1]+35),13)

    #Testfor var.dead by var.strikes
    if strikes >= 3:
        dead = True

    if wires_defused and keypads_defused and simon_defused and who_defused and button_defused:
        won = True

    #Time
    font = pygame.font.SysFont("defusedextended", 72)
    time = int(pygame.time.get_ticks()/1000)
    if time != prev_time:
        prev_time = time
        time_left -= 1
        pygame.mixer.music.load('beep.mp3')
        pygame.mixer.music.play()
        if time_left == 0:
            dead = True

    #--Timer--#
    time_mins = str(int(time_left/60))
    time_secs = time_left%60
    if time_secs < 10:
        time_secs = '0'+str(time_secs)
    timer_mins_surface = font.render(time_mins,False,(0,0,0))
    timer_thing = font.render(":",False,(0,0,0))
    timer_secs_surface = font.render(str(time_secs),False,(0,0,0))
        
    display.blit(moduleImg,(origins[timer_origin],origins[timer_origin+1]))
    pygame.draw.circle(display,(0,255,0),(origins[timer_origin]+257,origins[timer_origin+1]+35),13)
    display.blit(timer_mins_surface,(origins[timer_origin]+30,origins[timer_origin+1]+100))
    display.blit(timer_thing,((origins[timer_origin]+100,origins[timer_origin+1]+100)))
    display.blit(timer_secs_surface,(origins[timer_origin]+150,origins[timer_origin+1]+100))
    if strikes > 0:
        display.blit(strike,(origins[timer_origin]+40,origins[timer_origin+1]+20))
    if strikes > 1:
        display.blit(strike,(origins[timer_origin]+120,origins[timer_origin+1]+20))

    if prev_strikes != strikes:
        pygame.mixer.music.load('Doh.mp3')
        pygame.mixer.music.play()
        prev_strikes = strikes
        display.fill((255,0,0))
    pygame.display.update()
    clock.tick(10)

while not close and not won and dead:          
    display.blit(pygame.image.load('End Screen.png'),(0,0))
    pygame.display.update()
    pygame.mixer.music.load('bomb sound.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(4000)
    close = True

while not dead and not close and won:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close = True

    font = pygame.font.SysFont("defusedextended", 32)
    display.blit(pygame.image.load('Victory Royale XD.png'),(0,0))
    display.blit(font.render('Time Remaining:',False,(0,0,0)),(400,400))
    display.blit(timer_mins_surface,(400,440))
    display.blit(timer_thing,((470,440)))
    display.blit(timer_secs_surface,(500,440))
    pygame.display.update()
    pygame.mixer.music.load('yay.mp3')
    pygame.mixer.music.play()
    pygame.time.wait(5000)
    close = True
pygame.quit()
quit()
