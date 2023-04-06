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
			row=random.randint(25, 49)
			column=random.randint(0, 49)
		
		map.fields[row][column]="a"
		attackers[i].pos=[row, column]
	
	for i in range(len(defenders)):
		row = -1
		column = -1
		
		while (row < 0 or column < 0 or map.fields[row][column] != "."):
			row = random.randint(0, 25)
			column = random.randint(0, 49)
		
		map.fields[row][column]="d"
		defenders[i].pos = [row, column]
	
	raport.write("\n")
	
	for i in range(50):
		for j in range(50):
			raport.write(map.fields[i][j])
		raport.write("\n")
	
	for index in range(1, 101):
		if len(defenders)==0 or len(attackers)==0:
			break
		
		raport.write(f"\nTura {index}")
		attacker_death=0
		defender_death=0
		
		for i in range(50):
			for j in range(50):
				if map.fields[i][j]=="a":
					is_fight=False
					if is_fight==False:
						is_fight=True
						if i<49 and map.fields[i+1][j]=="d":
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

						if j<49 and map.fields[i][j+1]=="d":
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
						if i < 49 and map.fields[i + 1][j] == "a":
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
						
						if j < 49 and map.fields[i][j + 1] == "a":
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
		
		for i in range(50):
			for j in range(50):
				if map.fields[i][j]=="a" or map.fields[i][j]=="d":
					directions=["north", "east", "south", "west", "stop"]
					
					if i==0:
						directions.pop(3)
					if i==49:
						directions.pop(1)
					if j==0:
						directions.pop(0)
					if j==49:
						directions.pop(2)
					
					rnd=0
					
					while directions[rnd]!="stop" and len(directions)>0:
						rnd=random.randint(0, len(directions)-1)
						
						if directions[rnd]=="north":
							if map.fields[i][j-1] == "a" or map.fields[i][j-1]=="d":
								map.fields[i][j-1]=map.fields[i][j]
								map.pop([i, j])
								break
							if directions[rnd]=="east":
								if map.fields[i+1][j] == "a" or map.fields[i+1][j]=="d":
									map.fields[i+1][j]=f"m{map.fields[i][j]}"
									map.pop([i, j])
									break
							if directions[rnd] == "south":
								if map.fields[i][j+1] == "a" or map.fields[i][j+1]=="d":
									map.fields[i][j+1] = f"m{map.fields[i][j]}"
									map.pop([i, j])
									break
							if directions[rnd] == "west":
								if map.fields[i-1][j] == "a" or map.fields[i-1][j]=="d":
									map.fields[i+1][j] = map.fields[i][j]
									map.pop([i, j])
									break
						
						directions.pop(rnd)
						
				if len(map.fields[i][j])==2:
					map.fields[i][j]=map.fields[i][j][1]
		
		raport.write("\n")
		
		for i in range(50):
			for j in range(50):
				raport.write(map.fields[i][j])
			raport.write("\n")
		
		raport.write(f"\nStraty: \n\tAtakujący: {attacker_death} \n\tObrońcy: {defender_death} \n")
	
	return len(attackers), len(defenders)