import random

from fight import *
from raport import *

def standard_variant(raport, attackers, defenders):
	fight=Fight()
	for i in range(1, 101):
		if len(defenders)==0 or len(attackers)==0:
			break
		
		count=min(len(defenders), len(attackers))
		
		raport.write(f"\nTura {i}")
		attacker_death=0
		defender_death=0
		
		for j in range(count):
			attack=fight.fight()
			defend=fight.fight()
			
			result=fight.result(attack, defend)
			
			if result==0:
				rnd=random.randint(0, 1)
				
				if rnd==1:
					attacker_death+=1
					defender_death+=1
			
			if result==1:
				defender_death+=1
				
				rnd=random.randint(0, 1)
				
				if rnd==1:
					attacker_death+=1
			
			if result==-1:
				attacker_death+=1
				
				rnd=random.randint(0, 1)
				
				if rnd==1:
					defender_death+=1
			
			raport.write(f"\nPara {j} \n\tAtakujący: {attack} \n\tObrońca: {defend}\n")
			
		for j in range(attacker_death):
			if len(attackers)==0:
				break
			
			attackers.pop()
		
		for j in range(defender_death):
			if len(defenders)==0:
				break
			
			defenders.pop()
		
		raport.write(f"\nStraty: \n\tAtakujący: {attacker_death} \n\tObrońcy: {defender_death} \n")
	
	return len(attackers), len(defenders)