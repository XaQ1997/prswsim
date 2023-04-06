import random

from fight import *
from map import *
from raport import *

def standard_variant(raport, attackers, defenders):
	fight=Fight()
	map=Map()
	
	for i in range(len(attackers)):
		row=-1
		column=-1
		
		while(row<0 or column<0 or map.fields[row][column]!="."):
			row=random.randint(6, 11)
			column=random.randint(0, 11)
		
		map.fields[row][column]="a"
		attackers[i].pos=[row, column]
	
	for i in range(len(defenders)):
		row = -1
		column = -1
		
		while (row < 0 or column < 0 or map.fields[row][column] != "."):
			row = random.randint(0, 5)
			column = random.randint(0, 11)
		
		map.fields[row][column]="d"
		defenders[i].pos = [row, column]
	
	raport.write("\n")
	
	for i in range(12):
		for j in range(12):
			raport.write(map.fields[i][j])
		raport.write("\n")
	
	for index in range(1, 101):
		if len(defenders)==0 or len(attackers)==0:
			break
		
		raport.write(f"\nTura {index} \n")
		attacker_death=0
		defender_death=0
		number_fights=0
		
		for i in range(12):
			for j in range(12):
				if map.fields[i][j]=="a":
					is_fight=False
					if is_fight==False:
						is_fight=True
						if i<11 and map.fields[i+1][j]=="d":
							number_fights+=1
							attack=fight.fight()
							defend=fight.fight()
							
							result=fight.result(attack, defend)
							
							rnd=random.randint(0, 1)
							
							if result==0 and rnd==1:
								for k in range(len(attackers)):
									if attackers[k].pos==[i, j]:
										attackers.pop(k)
										map.pop([i, j])
										attacker_death+=1
										break
								
								for k in range(len(defenders)):
									if defenders[k].pos==[i, j]:
										defenders.pop(k)
										map.pop([i+1, j])
										defender_death+=1
										break
							
							if result==1:
								for k in range(len(defenders)):
									if defenders[k].pos==[i+1, j]:
										defenders.pop(k)
										map.pop([i+1, j])
										defender_death+=1
										break
								
								if rnd==1:
									for k in range(len(attackers)):
										if attackers[k].pos==[i, j]:
											attackers.pop(k)
											map.pop([i, j])
											attacker_death+=1
											break
							
							if result==-1:
								for k in range(len(attackers)):
									if attackers[k].pos==[i, j]:
										attackers.pop(k)
										map.pop([i, j])
										attacker_death+=1
										break
								
								if rnd==1:
									for k in range(len(defenders)):
										if defenders[k].pos==[i+1, j]:
											defenders.pop(k)
											map.pop([i+1, j])
											defender_death+=1
											break
							
							continue

						if j<11 and map.fields[i][j+1]=="d":
							number_fights+=1
							attack=fight.fight()
							defend=fight.fight()
							
							result=fight.result(attack, defend)
							
							rnd=random.randint(0, 1)
							
							if result==0 and rnd==1:
								for k in range(len(attackers)):
									if attackers[k].pos==[i, j]:
										attackers.pop(k)
										map.pop([i, j])
										attacker_death+=1
										break
								
								for k in range(len(defenders)):
									if defenders[k].pos==[i, j+1]:
										defenders.pop(k)
										map.pop([i, j+1])
										defender_death+=1
										break
							
							if result==1:
								for k in range(len(defenders)):
									if defenders[k].pos==[i, j+1]:
										defenders.pop(k)
										map.pop([i, j+1])
										defender_death+=1
										break
								
								if rnd==1:
									for k in range(len(attackers)):
										if attackers[k].pos==[i, j]:
											attackers.pop(k)
											map.pop([i, j])
											attacker_death+=1
											break
							
							if result==-1:
								for k in range(len(attackers)):
									if attackers[k].pos==[i, j]:
										attackers.pop(k)
										map.pop([i, j])
										attacker_death+=1
										break
								
								if rnd==1:
									for k in range(len(defenders)):
										if defenders[k].pos==[i, j+1]:
											defenders.pop(k)
											map.pop([i, j+1])
											defender_death+=1
											break
							
							continue

				if map.fields[i][j] == "d":
					is_fight = False
					if is_fight == False:
						is_fight = True
						if i < 11 and map.fields[i + 1][j] == "a":
							number_fights+=1
							attack = fight.fight()
							defend = fight.fight()
							
							result = fight.result(attack, defend)
							
							rnd = random.randint(0, 1)
							
							if result == 0 and rnd == 1:
								for k in range(len(attackers)):
									if attackers[k].pos == [i-1, j]:
										attackers.pop(k)
										map.pop([i+1, j])
										attacker_death += 1
										break
								
								for k in range(len(defenders)):
									if defenders[k].pos == [i, j]:
										defenders.pop(k)
										map.pop([i, j])
										defender_death += 1
										break
							
							if result == 1:
								for k in range(len(defenders)):
									if defenders[k].pos == [i, j]:
										defenders.pop(k)
										map.pop([i, j])
										defender_death += 1
										break
								
								if rnd == 1:
									for k in range(len(attackers)):
										if attackers[k].pos == [i+1, j]:
											attackers.pop(k)
											map.pop([i+1, j])
											attacker_death += 1
											break
							
							if result == -1:
								for k in range(len(attackers)):
									if attackers[k].pos == [i+1, j]:
										attackers.pop(k)
										map.pop([i+1, j])
										attacker_death += 1
										break
								
								if rnd == 1:
									for k in range(len(defenders)):
										if defenders[k].pos == [i, j]:
											defenders.pop(k)
											map.pop([i, j])
											defender_death += 1
											break
							
							continue
						
						if j < 11 and map.fields[i][j + 1] == "a":
							number_fights+=1
							attack = fight.fight()
							defend = fight.fight()
							
							result = fight.result(attack, defend)
							
							rnd = random.randint(0, 1)
							
							if result == 0 and rnd == 1:
								for k in range(len(attackers)):
									if attackers[k].pos == [i, j+1]:
										attackers.pop(k)
										map.pop([i, j+1])
										attacker_death += 1
										break
								
								for k in range(len(defenders)):
									if defenders[k].pos == [i, j]:
										defenders.pop(k)
										map.pop([i, j])
										defender_death += 1
										break
							
							if result == 1:
								for k in range(len(defenders)):
									if defenders[k].pos == [i, j]:
										defenders.pop(k)
										map.pop([i, j])
										defender_death += 1
										break
								
								if rnd == 1:
									for k in range(len(attackers)):
										if attackers[k].pos == [i, j+1]:
											attackers.pop(k)
											map.pop([i, j+1])
											attacker_death += 1
											break
							
							if result == -1:
								for k in range(len(attackers)):
									if attackers[k].pos == [i, j+1]:
										attackers.pop(k)
										map.pop([i, j+1])
										attacker_death += 1
										break
								
								if rnd == 1:
									for k in range(len(defenders)):
										if defenders[k].pos == [i, j]:
											defenders.pop(k)
											map.pop([i, j])
											defender_death += 1
											break
							
							continue
		
		for i in range(len(attackers)):
			attackers[i].move(map)
		
		for i in range(len(defenders)):
			defenders[i].move(map)
		
		for i in range(12):
			for j in range(12):
				raport.write(map.fields[i][j])
			raport.write("\n")
		
		raport.write(f"\nStoczonych walk: {number_fights} \nStraty: \n\tAtakujący: {attacker_death} \n\tObrońcy: {defender_death} \n")
	
	return len(attackers), len(defenders)