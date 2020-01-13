from graph import *

def Eye(x, y, radius): #Eye
	brushColor("white")
	circle(x ,y, radius) #Ball
	brushColor("black")
	circle(x, y, radius/2) #Pupil

brushColor("yellow")
circle(200, 200, 150) #Head
Eye(150, 150, 50) #Eye -left
Eye(250, 150, 30)	#Eye -right
	
polygon([(100, 100), (200, 80),(100, 130)]) #Brow -left
polygon([(210, 120), (300, 100),(210, 150)]) #Brow -right


run()