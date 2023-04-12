import random

from map import *

class Unit:
	def __init__(self, team):
		self.team=team[0]
		self.movement=1
		self.pos=[0, 0]
	
	def move(self, map):
		for i in range(self.movement):
			directions=["stop", "north", "east", "south", "west"]
			removed=[]
			
			if self.pos[0]==0 or map.occupied[self.pos[0]-1][self.pos[1]]!=".":
				directions.remove("north")
				removed.append("north")
			if self.pos[0]==19 or map.occupied[self.pos[0]+1][self.pos[1]]!=".":
				directions.remove("south")
				removed.append("south")
			if self.pos[1]==0 or map.occupied[self.pos[0]][self.pos[1]-1]!=".":
				directions.remove("west")
				removed.append("west")
			if self.pos[1]==19 or map.occupied[self.pos[0]][self.pos[1]+1]!=".":
				directions.remove("east")
				removed.append("east")
			
			rnd=random.randint(0, len(directions)-1)
			
			for i in range(len(removed)):
				directions.append(removed[i])
			
			if rnd!=0:
				map.pop(self.pos)
			if directions.index("north")==rnd:
				map.occupied[self.pos[0]-1][self.pos[1]]=self.team
				self.pos[0]-=1
				continue
			if directions.index("south")==rnd:
				map.occupied[self.pos[0]+1][self.pos[1]]=self.team
				self.pos[0]+=1
				continue
			if directions.index("west")==rnd:
				map.occupied[self.pos[0]][self.pos[1]-1]=self.team
				self.pos[1]-=1
				continue
			if directions.index("east")==rnd:
				map.occupied[self.pos[0]][self.pos[1]+1]=self.team
				self.pos[1]+=1