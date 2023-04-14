import random

class Fight:
	def __init__(self):
		self.attacks=["rock", "paper", "scissors"]
		self.options=["attack", "defend"]
	
	def option(self):
		rnd=random.randint(0, 1)
		
		return self.options[rnd]
	
	def fight(self):
		rnd=random.randint(0, 2)
		
		return self.attacks[rnd]
	
	def result(self, attack, defend, attack_field, defend_field):
		if attack==defend:
			return 0
		
		if attack_field=="p" and defend_field=="p":
			if (attack=="rock" and defend=="scissors") or (attack=="scissors" and defend=="paper") or (attack=="paper" and defend=="rock"):
				return 1
			else:
				return -1
		
		if attack_field=="p" and defend_field=="f":
			if attack=="paper" and defend=="rock":
				return 1
			if defend=="scissors":
				return 0
			else:
				return -1
		
		if attack_field=="p" and defend_field=="m":
			if attack=="rock" and defend=="scissors":
				return 1
			if defend=="paper":
				return 0
			else:
				return -1
		
		if attack_field=="p" and defend_field=="w":
			if attack=="scissors" and defend=="paper":
				return 1
			if defend=="rock":
				return 0
			else:
				return -1
		
		if attack_field=="f" and defend_field=="f":
			if (attack=="paper" and defend=="rock") or (attack=="rock" and defend=="scissors"):
				return 1
			else:
				return -1
		
		if attack_field=="f" and defend_field=="p":
			if attack=="scissors" and defend_field=="paper":
				return 1
			if defend=="rock":
				return 0
			else:
				return -1
		
		if attack_field=="f" and defend_field=="m":
			if attack=="rock" and defend=="scissors":
				return 1
			if defend=="paper":
				return 0
			else:
				return -1
		
		if attack_field=="f" and defend_field=="w":
			if attack=="paper" and defend=="rock":
				return 1
			if defend=="scissors":
				return 0
			else:
				return -1
		
		if attack_field=="m" and defend_field=="m":
			if (attack=="rock" and defend=="scissors") or (attack=="scissors" and defend=="paper"):
				return 1
			else:
				return -1
		
		if attack_field=="m" and defend_field=="p":
			if attack=="rock" and defend=="scissors":
				return 1
			if defend=="rock":
				return 0
			else:
				return -1
		
		if attack_field=="m" and defend_field=="f":
			if attack=="paper" and defend=="rock":
				return 1
			if defend=="paper":
				return 0
			else:
				return -1
		
		if attack_field=="m" and defend_field=="w":
			if attack=="scissors" and defend=="paper":
				return 1
			if defend=="scissors":
				return 0
			else:
				return -1
		
		if attack_field=="w" and defend_field=="w":
			if (attack=="paper" and defend=="rock") or (attack=="scissors" and defend=="paper"):
				return 1
			else:
				return -1
		
		if attack_field=="w" and defend_field=="p":
			if attack=="scissors" and defend=="paper":
				return 1
			if defend=="rock":
				return 0
			else:
				return -1
		
		if attack_field=="w" and defend_field=="f":
			if attack=="paper" and defend=="rock":
				return 1
			if defend=="scissors":
				return 0
			else:
				return -1
		
		if attack_field=="w" and defend_field=="m":
			if attack=="rock" and defend=="scissors":
				return 1
			if defend=="paper":
				return 0
			else:
				return -1