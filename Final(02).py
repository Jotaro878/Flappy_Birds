import pygame
from sys import exit
import random

pygame.init()

#variables:--------------------------------------------------------------------------------------------------------
game_active= False
temp1= False
start_time = 0
score_value=0
hs=0
speed=9
player_gravity = 0
player_speed =  0
t=24
t2=0
player_index =0 
t3=0
t4=True

#random--------------------------------------------------------------------------------------------------------
rand1=(random.randrange(1,1000))
rand2=(random.randrange(-30,100))
fixed1= rand1
fixed2= rand2

# def obstacle_movement(obstacle_list):
#     if obstacle_list:
#         for obstacle_rect in obstacle_list:
#             obstacle_rect.x -=15
#             screen.blit(vamp2,obstacle_rect)
#             screen.blit(vamp2_scaled,obstacle_rect)
        
#         return obstacle_list
#     else:
#         return []

#player animation--------------------------------------------------------------------------------------------------------
def player_animation(x):
    global vamp1, player_index,t4
    
    if game_active and t4:
        player_index += x
        if player_index>3:
            player_index=0
    if game_active and t4==False:
        player_index += x
        if player_index>4:
            t4=True 
            player_index=0
    vamp1=vamp1_list[int(player_index)]    
    
    

# def player_animation_jump(x):
#     global vamp1, player_index,t3,t4
#     if game_active and t4:
#         player_index += x
#         if player_index>3:
#             player_index=0
#         if player_index>2:
#             while t3<10:
#                 t3+=1
#         t3=0
#         vamp1=vamp1_list[int(player_index)]



def display_score(): 
        score = (pygame.time.get_ticks()-start_time)/1200
        if score>0 and score%10==0:
            t2=score
        score1 = test_font2.render(f'{int(score)}',False,(255, 255, 255))
        # score1_rect = text_surface.get_rect(topleft= (540-t2,5))
        screen.blit(score1 ,score1_rect)
        return(int(score))

screen = pygame.display.set_mode((2*288 ,512 )) 
   
clock= pygame.time.Clock()

test_surface1 = pygame.image.load('Assets/sprites/Background-day.png').convert_alpha()
test_surface2 = pygame.image.load('Assets/sprites/Background-night.png').convert_alpha()
test_surface11 = pygame.image.load('Assets/sprites/Background-day.png').convert_alpha()
test_surface12 = pygame.image.load('Assets/sprites/Background-day.png').convert_alpha()

vamp11  = pygame.image.load('Assets/sprites/yellowbird-upflap.png').convert_alpha()
vamp12 = pygame.image.load('Assets/sprites/yellowbird-midflap.png').convert_alpha()
vamp121 = pygame.transform.rotozoom(vamp12, 15, 1)
vamp13 = pygame.image.load('Assets/sprites/yellowbird-downflap.png').convert_alpha()

vamp1_list=[vamp11,vamp12,vamp13,vamp121]
vamp1=vamp1_list[player_index]

vamp2 = pygame.image.load('Assets/sprites/pipe-green.png').convert_alpha()
testground = pygame.image.load('Assets/sprites/Base.png').convert_alpha()
gameover = pygame.image.load('Assets/sprites/gameover.png').convert_alpha()
gameover_scaled = pygame.transform.rotozoom(gameover, 0, 1.5)

test_font = pygame.font.Font('Assets/Font/Minecraft.ttf', 50)
test_font2 = pygame.font.Font('Assets/Font/ARCADECLASSIC.TTF', 50)
test_font3 = pygame.font.Font('Assets/Font/PT_Serif/PTSerif-Regular.ttf', 50)


text_surface = test_font.render('My First Game',False,(64,64,64))
text_rect = text_surface.get_rect(center= (400,50))

score1 = test_font.render('My First Game',False,(64,64,64))
score1_rect = text_surface.get_rect(center= (400,50))

obstacle_rect_list=[]

vamp2_scaled = pygame.transform.rotozoom(vamp2, 180, 1)

gameover_rect= gameover.get_rect(center= (114+144-20,60))

player_rect1 = vamp1.get_rect(center = (30,400))
player_rect2 = vamp2.get_rect(topleft = (620,200))
player_rect22 = vamp2_scaled.get_rect(bottomleft = (620,120))
testground_rect = testground.get_rect(topleft = (0,400))
testground_rect2 = testground.get_rect(topleft = (288,400))
testground_rect3 = testground.get_rect(topleft = (288*2,400))

test_surface_rec1 = test_surface1.get_rect(topleft = (0,0))
test_surface_rec2 = test_surface11.get_rect(topleft = (288,0))
test_surface_rec3 = test_surface12.get_rect(topleft = (288*2,0))



#timer:--------------------------------------------------------------------------------------------------------
obstacle_timer =  pygame.USEREVENT + 1
pygame.time.set_timer(obstacle_timer , 900)

while True:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if player_rect1.collidepoint(event.pos) and player_rect1.top==200:
                player_gravity = -20
        if game_active: 
            if event.type == pygame.KEYDOWN:
                # print("key down")
                if event.key == pygame.K_SPACE:
                    # print("Jump")
                    player_gravity = -12
                    #for animating when flying ---------------------------------------------------------------------------------------------
                    

                if event.key == pygame.K_ESCAPE:
                    game_active = False
                    temp1 = False
            # if event.type == pygame.KEYUP:
            #     player_animation(0.2)
        if game_active==False:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    player_rect2.left=600+rand1
                    player_rect22.left=595+rand1
                    player_rect2.top=200+rand2
                    player_rect22.bottom=120-rand2
                    player_rect1.top=200
                    game_active=True
        # if event.type==obstacle_timer and game_active:
        #     obstacle_rect_list.append(vamp2.get_rect(topleft = (random.randrange(900,1100),200)))
        #     obstacle_rect_list.append(vamp2_scaled.get_rect(bottomleft = (random.randrange(900,1100),120)))
        
                    
    
 
    if game_active:
        #random no.--------------------------------------------------------------------------------------------------------
        rand2=(random.randrange(1,50))
        rand1=(random.randrange(1,1000))
        fixed1= rand1
        fixed2= rand2

        #you have not lost the game--------------------------------------------------------------------------------------------------------
        temp1 = True

        #surface background--------------------------------------------------------------------------------------------------------
        screen.blit(test_surface1,test_surface_rec1)
        screen.blit(test_surface12,test_surface_rec2)
        screen.blit(test_surface11,test_surface_rec3)

        #Displaying score:--------------------------------------------------------------------------------------------------------
        score_value=display_score()

        if score_value==10:
            t2=25
        if score_value==100:
            t2=50

        score1_rect = text_surface.get_rect(topleft= (540-t2,5))

        #sprites--------------------------------------------------------------------------------------------------------
        screen.blit(vamp1,player_rect1)
        screen.blit(vamp2,player_rect2)
        screen.blit(vamp2_scaled,player_rect22)
        screen.blit(testground,testground_rect)
        screen.blit(testground,testground_rect2)
        screen.blit(testground,testground_rect3)

        #flying animation:--------------------------------------------------------------------------------------------------------

        player_animation(0.2)
        key= pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            player_index=3
            t4=False 

        #controling speed:--------------------------------------------------------------------------------------------------------
        if score_value>0 and score_value%10==0 and speed <100 and score_value/5>9:
            speed=score_value/5

        player_rect22.left -=speed
        player_rect2.left  -=speed
        testground_rect.left  -= 10 
        testground_rect2.left -= 10 
        testground_rect3.left -= 10

        # test_surface_rec1.left  -= 1
        # test_surface_rec2.left -= 1
        # test_surface_rec3.left -= 1

        if player_rect2.left <= -100: 
            player_rect2.left=600
            player_rect22.left=595
            player_rect2.top=200+rand2
            player_rect22.bottom=120-rand2
        if testground_rect.left <= -288:
            testground_rect.left=288*2
        if testground_rect2.left <= -288:
            testground_rect2.left=288*2
        if testground_rect3.left <= -288:
            testground_rect3.left=288*2

        if test_surface_rec1.left <= -288:
            test_surface_rec1.left=288*2
        if test_surface_rec2.left <= -288:
            test_surface_rec2.left=288*2
        if testground_rect3.left <= -288:
            testground_rect3.left=288*2
            
        
        #Player Falling:--------------------------------------------------------------------------------------------------------
        player_rect1.bottom += player_gravity
        if player_rect1.top<=380:
            player_gravity += 2             
        else:
            player_gravity=0
            player_rect1.top=380


        #player collision:--------------------------------------------------------------------------------------------------------
        if player_rect2.colliderect(player_rect1) or player_rect22.colliderect(player_rect1) or player_rect1.colliderect(testground_rect) or player_rect1.colliderect(testground_rect2) or player_rect1.colliderect(testground_rect3) or player_rect1.collidepoint((30,-40)):
            game_active = False

            
#losing the game--------------------------------------------------------------------------------------------------------
    else:
        #change is variables after losing--------------------------------------------------------------------------------------------------------
        t2=0
        speed=9

        #surface--------------------------------------------------------------------------------------------------------
        screen.blit(test_surface2,(0,0))
        screen.blit(test_surface2,(288,0))
        start_time=pygame.time.get_ticks()

        if temp1:
            score1 = test_font.render(f'{int(score_value)}',False,(255, 244, 233))
            score1_rect = text_surface.get_rect(center= (120+144+150+30,170))
            screen.blit(score1 ,score1_rect)
            screen.blit(gameover_scaled ,gameover_rect)


            #CHANGE IS HIGHSCORE--------------------------------------------------------------------------------------------------------
            if(score_value>=hs):
                txt2 = test_font2.render('HIGHSCORE',False,(255, 244, 233))
                txt2_rec = text_surface.get_rect(topleft= (19+144,220))
                screen.blit(txt2 ,txt2_rec)
                hs=score_value
            
        
            key= pygame.key.get_pressed()
            if key[pygame.K_ESCAPE]:
                temp1=False
                

        elif temp1==False:
            start1 = test_font2.render('PRESS   ENTER   TO   PLAY',False,(255, 244, 233))
            start4 = test_font2.render('By  Yashasvi',False,(198, 215, 158))
            start5 = test_font.render('Flappy',False,(255, 244, 233))
            start6 = test_font.render('Birds',False,(255, 244, 233))

            start12 = pygame.transform.rotozoom(start1, 0, 0.8)
            start42 = pygame.transform.rotozoom(start4, 0, 0.7)

            start1_rect = text_surface.get_rect(topleft= (90,210))
            start4_rect = text_surface.get_rect(topleft= (50+288,460))
            start5_rect = text_surface.get_rect(topleft= (10+200,30))
            start6_rect = text_surface.get_rect(topleft= (30+200,90))

            screen.blit(start12 ,start1_rect)
            screen.blit(start42 ,start4_rect)
            screen.blit(start5 ,start5_rect)
            screen.blit(start6 ,start6_rect)
            
            
        player_rect1.top=200
   
        

        

    pygame.display.update()
    clock.tick(t)      