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
					row.append(["p", random.randint(0, 1)])
				if biomes[rnd]=="forest":
					row.append(["f", random.randint(1, 3)])
				if biomes[rnd]=="montains":
					row.append(["m", 0])
				if biomes[rnd]=="water":
					row.append(["w", random.randint(0, 2)])
				
			self.fields.append(row)
	
	def pop(self, pos):
		self.occupied[pos[0]][pos[1]]="."