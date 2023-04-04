import datetime
import random

from fight import *
from raport import *

if __name__=="__main__":
	with open("count.txt") as count:
		text=count.read()
	
	with open("count.txt", "w") as count:
		count.write(text+"#")
	
	path=f"raporty\{len(text)}.txt"
	
	raport=Raport(path)
	
	attackers=random.randint(10, 100)
	defenders=random.randint(10, 100)
	
	raport.write(f"Wersja: v0.1.0 \nData symulacji: {datetime.datetime.now().date()} \n\nAtakujący: {attackers} \nObrońcy: {defenders}\n")
	
	if attackers>=2*defenders:
		raport.write("Obrona twierdzy \n")
		for i in range(1, 101):
			if defenders == 0 or attackers == 0:
				break
			
			fight = Fight()
			
			attack = fight.fight()
			defend = fight.fight()
			
			result = fight.result(attack, defend)
			
			count = min(defenders, attackers)
			
			if result == 0:
				attacker_losses = random.randint(0, count)
				attackers -= attacker_losses
				
				if attacker_losses>0.6*count:
					defender_losses=random.randint(4*count, 6*count)
					defender_losses//=10
				else:
					defender_losses=attacker_losses
				
				defenders-=defender_losses
			
			if result == 1:
				attacker_losses = random.randint(0, count)
				attackers -= attacker_losses
				
				if attacker_losses>0.8*count and count>=10 and defenders<attackers:
					defender_losses=random.randint(7*count, 8*count)
					defender_losses//=10
				elif attacker_losses>0.8*count and count<10 or defenders>attackers:
					defender_losses=random.randint(5*count, 9*count)
					defender_losses//=10
				else:
					defender_losses=random.randint(attacker_losses, count)
				
				defenders-=defender_losses
			
			if result == -1:
				defender_losses = random.randint(0, 3*count)
				defender_losses//=10
				defenders -= defender_losses
				
				attacker_losses = random.randint(defender_losses, count)
				attackers -= attacker_losses
			
			raport.write(
				f"\nTura {i} \nAtakujący: {attack} \nObrońcy: {defend} \nStraty: \n\tatakujących: {attacker_losses} \n\tobrońców: {defender_losses} \n")
	else:
		raport.write("Wariant standardowy \n")
		for i in range(1, 101):
			if defenders==0 or attackers==0:
				break
			
			fight=Fight()
			
			attack=fight.fight()
			defend=fight.fight()
			
			result=fight.result(attack, defend)
			
			count=min(defenders, attackers)
			
			if result==0:
				losses=random.randint(0, count)
				attackers-=losses
				defenders-=losses
				
				attacker_losses=losses
				defender_losses=losses
			
			if result==1:
				attacker_losses=random.randint(0, count)
				attackers-=attacker_losses
				
				defender_losses=random.randint(attacker_losses, count)
				defenders-=defender_losses
			
			if result==-1:
				defender_losses=random.randint(0, count)
				defenders-=defender_losses
				
				attacker_losses=random.randint(defender_losses, count)
				attackers-=attacker_losses
			
			raport.write(f"\nTura {i} \nAtakujący: {attack} \nObrońcy: {defend} \nStraty: \n\tatakujących: {attacker_losses} \n\tobrońców: {defender_losses} \n")
	
	raport.write(f"\n\n Rezultat bitwy: \n{attackers}-{defenders}")
