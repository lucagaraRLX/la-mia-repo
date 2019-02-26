45
# il record viene salvato nella prima riga del file
import pygame,random,sys	# importo i moduli necessari
pygame.init()	# inizializzo pygame
def salva(p):		# funzione che legge il file e poi lo riscrive col nuovo record
	f=open(sys.argv[0],"r")
	x=f.readline()
	x=f.readlines()
	f.close()
	f=open(sys.argv[0],"w")
	f.write(str(p)+"\n")
	for i in x:
		f.write(i)
	f.close()
	
def record():	# funzione che legge il record
	f=open(sys.argv[0],"rb")
	x=int(f.readline())
	f.close()
	return x
def gameover(x):	# funzione che inizia quando si perde e stampa il punteggio e il record, o se si e' superato quest'ultimo
	global m,snake
	if m==False:		# m e' true se si e' chiusa la finestra e false se il giocatore ha perso
		global size,w,h,verdanabig,fontino
		s=verdanabig.render(str(len(snake.s)-3),True,(0,0,0))	# creo la superficie col punteggio
		if record()>len(snake.s)-3:	# verifico se e' stato battuto il record
			s2=fontino.render("Current record: "+str(record()),True,(0,0,0))	# no
		else:
			s2=fontino.render("u r pro bro!",True,(0,0,0))	# si
			salva(len(snake.s)-3)	# salva il nuovo record nella prima riga del file
		
		f2=mini.render("Maiusc-F2 to restart ",True,(0,0,0))
		r=s.get_rect()		# rect delle scritte
		r2=s2.get_rect()
		while not(x):		# stampo le scritte e metto i comandi per la chiusura
			evento=pygame.event.poll()
			if evento.type==pygame.QUIT:	sys.exit()
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F2:	# regolo la pausa
				snake=Serpente()
				frut=frutto()
				game()
			schermo.fill((255,255,183))
			schermo.blit(s,((w-r.w)/2,(h-r.h)/2-20,r[2],r[3]))
			schermo.blit(s2,((w-r2.w)/2,(h-r2.h)/2+20,r2[2],r2[3]))
			schermo.blit(f2,(15,h-20,0,0))
			pygame.display.update()
			pygame.time.delay(100)

def testa():		# ritorna una superficie di colore rosso per la testa
	s=pygame.Surface((20,20))
	s.fill((0,0,255))
	return s
def corpo():		# ritorna una superficie di colore verde per il corpo
	s=pygame.Surface((20,20))
	s.fill((0,200,0))
	return s
def frutto():		# ritorna una superficie di colore blu per i frutti con il suo rect
	s=pygame.Surface((20,20))
	s.fill((99,0,0))
	r=pygame.Rect(random.randrange(0,20)*20,random.randrange(0,12)*20,20,20)
	return s,r
	
class Serpente:		# la classe del nostro snake!
	def __init__(self,w=3):
		self.dir=1,0
		self.s=[]
		for i in range(w):	# con questo ciclo creo il serpente
			self.s.append((w+3-i,3))
	def Muovi(self,dir=False):	# muove la testa in base la direzione, poi scorre tutte le altre parti
		global size,w,h,frut		# nella lista self.s
		if dir==False:	dir=self.dir
		elif (dir[0]==self.dir[0] and dir[1]==-1*self.dir[1]) or (dir[1]==self.dir[1] and dir[0]==-1*self.dir[0]):	dir=self.dir
		else:	self.dir=dir
		x=[[self.s[0][0]+dir[0],self.s[0][1]+dir[1]]]
		
		z=-1	
		if x[0][0]<0:	x[0][0]=w/20-1		# valuto se trapassa una parete
		elif x[0][1]<0:	x[0][1]=h/20-1
		elif x[0][0]>w/20-1:	x[0][0]=0
		elif x[0][1]>h/20-1:	x[0][1]=0
		r=[(self.s[0][0]+dir[0])*20,(self.s[0][1]+dir[1])*20]
		if r[0]==w:	r[0]=0					# se deve sbucare correggo le cordinate o ci sara' un errore con il frutto
		elif r[0]==-20:	r[0]=w-20
		elif r[1]==h:	r[1]=0
		elif r[1]==-20:	r[1]=h-20
		r=pygame.Rect(r[0],r[1],20,20)
		
		if frut[1].colliderect(r)==1:		# controllo se becca il frutto
			z=None	# se lo becca
			frut=frutto()	# non elimina l'ultimo pezzo di snake, altrimenti procede normalmente
		
		for i in self.s[:z]:
			x.append(i)
			
		self.s=x			# aggiorno la lista con i pezzi di snake
		x=[]
		for i in self.s:
			x.append(pygame.Rect(i[0]*20,i[1]*20,20,20))
			
		for i in x[2:]:	# controllo se tocca uno dei suoi stessi pezzi
			if x[0].colliderect(i)==True:	return False
		return None	# se fosse cosi' una verifica nel ciclo di gioco eseguira' la funzione gameover
			
	def Stampa(self,sc):	# gli do una superficie e ci stampa snake
		sc.blit(testa(),(self.s[0][0]*20,self.s[0][1]*20,20,20))
		for i in self.s[1:]:
			sc.blit(corpo(),(i[0]*20,i[1]*20,20,20))

# variabili delle dimensioni
size=w,h=400,240
schermo=pygame.display.set_mode(size)	# creo la finestra
pygame.display.set_caption("Snake")	# imposto il titlop
snake=Serpente()	# creo snake
frut=frutto()		# creo il frutto
# creo i due font per la comunica del punteggio
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
	pausa=False	# true se il gioco e' in pausa
	while 1:		# ciclo del gioco
		m=True		# se e' true la finestra e' stata chiusa, se e' false il giocatore ha perso
		evento=pygame.event.poll()		# prima di tutto verifico se si vuole chiudere
		if evento.type==pygame.QUIT:	break
		elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_F2:	# regolo la pausa
			snake=Serpente()
			frut=frutto()
		elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_p:	# regolo la pausa
			if pausa==False:	pausa=True
			else:	pausa=False
			
		if pausa==False:
			keys=pygame.key.get_pressed()
			if evento.type==pygame.KEYDOWN and evento.key==pygame.K_UP:	m=snake.Muovi((0,-1))	# scelgo la direzione del movimento
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_DOWN:	m=snake.Muovi((0,1))
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_RIGHT:	m=snake.Muovi((1,0))
			elif evento.type==pygame.KEYDOWN and evento.key==pygame.K_LEFT:	m=snake.Muovi((-1,0))
			else:	m=snake.Muovi()
			if m==False:	break		# se m diventa m dopo la funzione Muovi vuol dire che la testa ha fatto collisione con un pezzo
			schermo.fill((255,255,183))	# quindi game over!	|	riempio lo sfondo
			snake.Stampa(schermo)		# stampo snake
			schermo.blit(frut[0],frut[1])	# stampo frutto
			pt=mini.render(str(len(snake.s)-3),True,(0,0,0))
			schermo.blit(pt,(15,h-20,0,0))
			pygame.display.update()				# aggiorno
			pygame.time.delay(100)				# pausa di un decimo di sec tra un fotogramma e l'altro
	gameover(m)					# parte gameover
game()