import random

class Map:
	def __init__(self):
		self.occupied=[]
		
		for i in range(20):
			row=[]
			for j in range(20):
				row.append(".")
			
			self.occupied.append(row)
		
		self.fields=[]
		
		biomes=["plains", "forest", "montains", "water"]
		
		for i in range(20):
			row=[]
			for j in range(20):
				rnd=random.randint(0, len(biomes)-1)
				
				if biomes[rnd]=="plains":
					row.append("p")
				if biomes[rnd]=="forest":
					row.append("f")
				if biomes[rnd]=="montains":
					row.append("m")
				if biomes[rnd]=="water":
					row.append("w")
				
			self.fields.append(row)
	
	def pop(self, pos):
		self.occupied[pos[0]][pos[1]]="."