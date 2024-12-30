import pgzrun
import random
from time import time

HEIGHT=600
WIDTH=800

TITLE="Satelites"

satellites=[]
lines=[]
next_satellite=0

total_time=0
end_time=0
start_time=0

number_of_satellites=8

def create_satellites():
    global start_time
    for i in range(number_of_satellites):
        satellite=Actor("satellite")
        satellite.pos=random.randint(40,760),random.randint(40,560)
        satellites.append(satellite)
    start_time=time()

def draw():
    global total_time
    num=1
    screen.blit("bg",(0,0))
    for satellite in satellites:
        satellite.draw()
        screen.draw.text(num,(satellite.pos[0],satellite.pos[1]+20))
        num+=1
    for line in lines:
        screen.draw.line(line[0],line[1],"white")
                        



               
    


                                                        
pgzrun.go()

        


