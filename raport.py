class Raport:
	def __init__(self, path):
		self.path=path
	
	def write(self, description):
		with open(self.path, "a+") as file:
			text=file.write(description)