45

import pygame,random,sys	
pygame.init()	
def salva(p):		
	f=open(sys.argv[0],"r")
	x=f.readline()
	x=f.readlines()
	f.close()
	f=open(sys.argv[0],"w")
	f.write(str(p)+"\n")
	for i in x:
		f.write(i)
	f.close()
	
def record():	
	f=open(sys.argv[0],"rb")
	x=int(f.readline())
	f.close()
	return x
def gameover(x):	
	global m,snake
	if m==False:		
		global size,w,h,verdanabig,fontino
		s=verdanabig.render(str(len(snake.s)-3),True,(0,0,0))	
		if record()>len(snake.s)-3:	
			s2=fontino.render("Current record: "+str(record()),True,(0,0,0))	
		else:
			s2=fontino.render("u r pro bro!",True,(0,0,0))	# si
			salva(len(snake.s)-3)	
		
		f2=mini.render("Maiusc-F2 to restart ",True,(0,0,0))
		r=s.get_rect()		
		r2=s2.get_rect()
		while not(x):		
			evento=pygame.event.poll()
			if evento.type==pygame.QUIT:	sys.exit()
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F2:	
				snake=Serpente()
				frut=frutto()
				game()
			schermo.fill((255,255,183))
			schermo.blit(s,((w-r.w)/2,(h-r.h)/2-20,r[2],r[3]))
			schermo.blit(s2,((w-r2.w)/2,(h-r2.h)/2+20,r2[2],r2[3]))
			schermo.blit(f2,(15,h-20,0,0))
			pygame.display.update()
			pygame.time.delay(100)

def testa():		
	s=pygame.Surface((20,20))
	s.fill((0,0,255))
	return s
def corpo():		
	s=pygame.Surface((20,20))
	s.fill((0,200,0))
	return s
def frutto():		
	s=pygame.Surface((20,20))
	s.fill((99,0,0))
	r=pygame.Rect(random.randrange(0,20)*20,random.randrange(0,12)*20,20,20)
	return s,r
	
class Serpente:		
	def __init__(self,w=3):
		self.dir=1,0
		self.s=[]
		for i in range(w):	
		    self.s.append((w+3-i,3))
	def Muovi(self,dir=False):	
		global size,w,h,frut		
		if dir==False:	dir=self.dir
		elif (dir[0]==self.dir[0] and dir[1]==-1*self.dir[1]) or (dir[1]==self.dir[1] and dir[0]==-1*self.dir[0]):	dir=self.dir
		else:	self.dir=dir
		x=[[self.s[0][0]+dir[0],self.s[0][1]+dir[1]]]
		
		z=-1	
		if x[0][0]<0:	x[0][0]=w/20-1		
		elif x[0][1]<0:	x[0][1]=h/20-1
		elif x[0][0]>w/20-1:	x[0][0]=0
		elif x[0][1]>h/20-1:	x[0][1]=0
		r=[(self.s[0][0]+dir[0])*20,(self.s[0][1]+dir[1])*20]
		if r[0]==w:	r[0]=0
		elif r[0]==-20:	r[0]=w-20
		elif r[1]==h:	r[1]=0
		elif r[1]==-20:	r[1]=h-20
		r=pygame.Rect(r[0],r[1],20,20)
		
		if frut[1].colliderect(r)==1:		
			z=None
			frut=frutto()	
		
		for i in self.s[:z]:
			x.append(i)
			
		self.s=x			
		x=[]
		for i in self.s:
			x.append(pygame.Rect(i[0]*20,i[1]*20,20,20))
			
		for i in x[2:]:	
			if x[0].colliderect(i)==True:	return False
		return None	
			
	def Stampa(self,sc):	
		sc.blit(testa(),(self.s[0][0]*20,self.s[0][1]*20,20,20))
		for i in self.s[1:]:
			sc.blit(corpo(),(i[0]*20,i[1]*20,20,20))


size=w,h=400,240
schermo=pygame.display.set_mode(size)	
pygame.display.set_caption("Snake")	
snake=Serpente()	
frut=frutto()		

try:
	verdanabig=pygame.font.SysFont("verdana.ttf",50)
	fontino=pygame.font.SysFont("verdana.ttf",25)
	mini=pygame.font.SysFont("verdana.ttf",20)
except:
	try:
		verdanabig=pygame.font.SysFont(pygame.font.get_default_font(),50)
		fontino=pygame.font.SysFont(pygame.font.get_default_font(),25)
		mini=pygame.font.SysFont(pygame.font.get_default_font(),20)
	except:
		verdanabig=pygame.font.Font(pygame.font.get_default_font(),50)
		fontino=pygame.font.Font(pygame.font.get_default_font(),25)
		mini=pygame.font.Font(pygame.font.get_default_font(),20)
def game():
	global snake,frut,m
	pausa=False	
	while 1:	
		m=True		
		evento=pygame.event.poll()		
		if evento.type==pygame.QUIT:	break
		elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F2:	
			snake=Serpente()
			frut=frutto()
		elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_p:	
			if pausa==False:	pausa=True
			else:	pausa=False
			
		if pausa==False:
			keys=pygame.key.get_pressed()
			if evento.type==pygame.KEYDOWN and evento.key==pygame.K_UP:	m=snake.Muovi((0,-1))	
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_DOWN:	m=snake.Muovi((0,1))
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_RIGHT:	m=snake.Muovi((1,0))
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_LEFT:	m=snake.Muovi((-1,0))
			else:	m=snake.Muovi()
			if m==False:	break		
			schermo.fill((255,255,183))	
			snake.Stampa(schermo)		
			schermo.blit(frut[0],frut[1])	
			pt=mini.render(str(len(snake.s)-3),True,(0,0,0))
			schermo.blit(pt,(15,h-20,0,0))
			pygame.display.update()				
			pygame.time.delay(100)				
	gameover(m)					
game()
