# Snake Game!
# our modules

import pygame #everything that is needed for game that is gui and sound etc
import sys, random, time

#check for initializing errors
check_errors=pygame.init()#initializing pygame
if check_errors[1]>0:
	print("(!) Had {0} initializing errors,exiting...".format(check_errors[1]))
	sys.exit(-1)
# # 8u9
#file
#score
score=0

tm =int(round(time.time() * 1000))
increse = random.randrange(10,15)*1000
tm+=increse
upto =10000
bonusFood=[random.randrange(12,70)*10,random.randrange(5,40)*10]
bonusE=False

#play surface
playSurface=pygame.display.set_mode((720,460))
pygame.display.set_caption("Snake Game")

#colors
disp=pygame.Color(255,255,123) #background
snake=pygame.Color(0,255,0) #snake color
red=pygame.Color(255,0,0) #game over
black=pygame.Color(0,123,255) #score
brown=pygame.Color(165,42,42)#food
# black=pygame.Color(0,0,0)#bonus

# FPS Controller (frame per second)
fpsController=pygame.time.Clock()
#snakePos =[random.randint(120,700),random.randint(50,400)]
snakePos=[100,50]
snakeBody=[[100,50],[90,50],[80,50]]

foodPos=[random.randrange(12,70)*10,random.randrange(5,40)*10]
foodSpawn=True

direction ='RIGHT'
changeto = direction

#function to give bonus food
# # def bonus(x,y):
# 	pygame.draw.rect(playSurface,red,pygame.Rect(x,y,10,10))

#score function
def showScore(choice=1):
	sfont=pygame.font.SysFont("monaco",25)
	ssurf=sfont.render('Score {0}'.format(score),True,red)
	srect=ssurf.get_rect()
	if choice ==1:
		srect.midtop=(80,10)
	else:
		srect.midtop=(360,120)
	playSurface.blit(ssurf,srect)
	#pygame.display.flip()
#Game Over Function
def gameOver():
	myFont= pygame.font.SysFont("monaco",72)
	GoSurf=myFont.render('Game Over! ',True,red)
	Gorect=GoSurf.get_rect()
	Gorect.midtop=(360,15)
	playSurface.blit(GoSurf,Gorect)
	showScore(2)
	label=pygame.font.SysFont("monaco",20).render('Developer.. Raghvendra',True,red)
	labelRect=label.get_rect()
	labelRect.midtop=(610,430)
	playSurface.blit(label,labelRect)
	pygame.display.flip()
	time.sleep(5)
	pygame.quit() #pygame exit
	sys.exit() # console exit

# main logic of the game
while True:
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type==pygame.KEYDOWN:
			if event.key== pygame.K_RIGHT or event.key == ord('d') or event.key == ord('D'):
				changeto="RIGHT"
			if event.key== pygame.K_LEFT or event.key == ord('a') or event.key == ord('A'):
				changeto="LEFT"
			if event.key== pygame.K_UP or event.key == ord('w') or event.key == ord('W'):
				changeto="UP"
			if event.key== pygame.K_DOWN or event.key == ord('s') or event.key == ord('S'):
				changeto="DOWN"
			if event.key== pygame.K_ESCAPE :
				pygame.event.post(pygame.event.Event(pygame.QUIT))

	if changeto =='RIGHT' and not direction=='LEFT':
		direction='RIGHT'
	elif changeto =='LEFT' and not direction=='RIGHT':
		direction='LEFT'
	elif changeto =='UP' and not direction=='DOWN':
		direction='UP'
	elif changeto =='DOWN' and not direction=='UP':
		direction='DOWN'

	# UPdate snake position
	if direction=='RIGHT':
		snakePos[0]+=10
	elif direction=='LEFT':
		snakePos[0]-=10
	elif direction=='UP':
		snakePos[1]-=10
	elif direction=='DOWN':
		snakePos[1]+=10

	#Snake  body mechanism
	snakeBody.insert(0,list(snakePos))

	if snakePos[0]==bonusFood[0] and snakePos[1]==bonusFood[1]:
		bonusE=False
		if score==0:
			score=120
		else:
			score= score +int((random.randrange(3,9)/10.0)*score)

	if snakePos[0]==foodPos[0]and snakePos[1]==foodPos[1]:
		#print("Eaten")
		score+=10
		foodSpawn=False
	else:
		snakeBody.pop()

	#Bonus
	# print(bonusE,tm-int(round(time.time() * 1000)),abs(tm-int(round(time.time() * 1000))))
	if bonusE==False and abs((tm-int(round(time.time() * 1000)))<300):
		# print("*")
		bonusE=True
		bonusFood=[random.randrange(12,70)*10,random.randrange(5,40)*10]

	if bonusE==True and abs((tm+upto-int(round(time.time() * 1000)))<300):
		# print("#")
		bonusE=False
		tm =int(round(time.time() * 1000))+random.randrange(10,15)*5000


	#Food Spawn
	if foodSpawn==False:
		foodPos=[random.randrange(12,70)*10,random.randrange(5,40)*10]
		#print("new food",foodPos)
		foodSpawn=True

	#background
	playSurface.fill(disp)

	#Draw Snake
	for pos in snakeBody:
		pygame.draw.rect(playSurface,snake,pygame.Rect(pos[0],pos[1],10,10))
	pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))
	if bonusE:
		pygame.draw.rect(playSurface,black,pygame.Rect(bonusFood[0],bonusFood[1],10,10))
	if snakePos[0]>=720 or snakePos[0]<=0 or snakePos[1] >=460 or snakePos[1]<=0:
		gameOver()
	for blocks in snakeBody[1:]:
		if blocks[0]==snakePos[0] and blocks[1]==snakePos[1]:
			gameOver()
	showScore()
	pygame.display.flip()
	fpsController.tick(22)

	#pyinstaller