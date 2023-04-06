class Map:
	def __init__(self):
		self.fields=[]
		
		for i in range(12):
			row=[]
			for j in range(12):
				row.append(".")
			
			self.fields.append(row)
	
	def pop(self, pos):
		self.fields[pos[0]][pos[1]]="."