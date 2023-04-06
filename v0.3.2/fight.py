import random

class Fight:
	def __init__(self):
		self.attacks=["rock", "paper", "scissors"]
	
	def fight(self):
		rnd=random.randint(0, 2)
		
		return self.attacks[rnd]
	
	def result(self, attack, defend):
		if attack==defend:
			return 0
		
		if (attack=="rock" and defend=="scissors") or (attack=="scissors" and defend=="paper") or (attack=="paper" and defend=="rock"):
			return 1
		else:
			return -1