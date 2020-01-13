from graph import *

def Eye(x,y,radius): #Eye
	brushColor("white")
	circle(x,y,radius) #Ball
	brushColor("black")
	circle(x,y,radius/2) #Pupil

brushColor("yellow")
circle(200,200,150) #Head
Eye(150,150,50) #Eye -left
Eye(250,150,30)	#Eye -right
	
	


run()