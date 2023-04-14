import random

from fight import *
from map import *
from raport import *

def standard_variant(raport, attackers, defenders):
	fight=Fight()
	map=Map()
	
	biomes={"plains": [0, 0], "forest": [0, 0], "mountains": [0, 0], "water": [0, 0]}
	
	for i in range(20):
		for j in range(20):
			if map.fields[i][j][0]=="p":
				biomes["plains"][0]+=1
				biomes["plains"][1]+=map.fields[i][j][1]
			if map.fields[i][j][0]=="f":
				biomes["forest"][0]+=1
				biomes["forest"][1] += map.fields[i][j][1]
			if map.fields[i][j][0]=="m":
				biomes["mountains"][0]+=1
				biomes["mountains"][1] += map.fields[i][j][1]
			if map.fields[i][j][0]=="w":
				biomes["water"][0]+=1
				biomes["water"][1] += map.fields[i][j][1]
	
	raport.write("\n")
	
	for i in biomes:
		raport.write(f"\n{i}: {biomes[i][0]/4}")
	
	raport.write("\n")
	raport.write("\n")
	
	sum=0
	
	for i in biomes:
		raport.write(f"\n\t{i}: {biomes[i][1]/biomes[i][0]}")
		sum+=biomes[i][1]
	
	raport.write(f"\n\nProdukcja pożywienia na pole: {sum/400} \n")
	
	for i in range(20):
		raport.write("\n")
		for j in range(20):
			raport.write(map.fields[i][j][0])
	
	raport.write("\n")
	for i in range(20):
		raport.write("\n")
		for j in range(20):
			raport.write(str(map.fields[i][j][1]))
	
	raport.write("\n")
	
	for i in range(len(attackers)):
		row=-1
		column=-1
		
		while(row<0 or column<0 or map.occupied[row][column]!="."):
			row=random.randint(10, 19)
			column=random.randint(0, 19)
		
		map.occupied[row][column]="a"
		attackers[i].pos=[row, column]
	
	for i in range(len(defenders)):
		row = -1
		column = -1
		
		while (row < 0 or column < 0 or map.occupied[row][column] != "."):
			row = random.randint(0, 9)
			column = random.randint(0, 19)
		
		map.occupied[row][column]="d"
		defenders[i].pos = [row, column]
	
	raport.write("\n")
	
	for i in range(20):
		for j in range(20):
			raport.write(map.occupied[i][j])
		raport.write("\n")
		
		attack_resources=0
		defend_resources=0
	
	for index in range(1, 251):
		att_resources=attack_resources
		def_resources=defend_resources
		att=int(len(attackers))
		deff=int(len(defenders))
		
		if len(defenders)==0 or len(attackers)==0:
			break
		
		raport.write(f"\nTura {index} \n")
		attacker_death=0
		defender_death=0
		number_fights=0
		
		for i in range(20):
			for j in range(20):
				if map.occupied[i][j]=="a":
					is_fight=False
					if is_fight==False:
						is_fight=True
						defender=[]
						if i<19 and map.occupied[i+1][j]=="d":
							number_fights+=1
							att_option=fight.option()
							def_option=fight.option()
							
							defender.append(i+1)
							defender.append(j)
							
							if att_option!=def_option:
								attack = fight.fight()
								defend = fight.fight()
								
								result = fight.result(attack, defend, map.fields[i][j], map.fields[i+1][j])
								
								if att_option=="attack":
									if result==1:
										for k in range(len(defenders)):
											if defenders[k].pos == [i+1, j]:
												defenders.pop(k)
												map.pop([i + 1, j])
												defender_death += 1
												break
								if att_option=="defend":
									if result==-1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
							
							if att_option==def_option and att_option=="attack":
								attack=fight.fight()
								defend=fight.fight()
								
								result=fight.result(attack, defend, map.fields[i][j], map.fields[i+1][j])
								
								rnd=random.randint(0, 1)
								
								if result==0 and rnd==1:
									for k in range(len(attackers)):
										if attackers[k].pos==[i, j]:
											attackers.pop(k)
											map.pop([i, j])
											attacker_death+=1
											break
									
									for k in range(len(defenders)):
										if defenders[k].pos==[i+1, j]:
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
								
								raport.write(f"Walka nr {number_fights} \n{map.fields[i][j][0]}[{i}; {j}] vs {map.fields[defender[0]][defender[1]][0]}[{defender[0]}; {defender[1]}] \n{att_option} vs {def_option} \n")
								
								if att_option == "attack" or def_option == "attack":
									raport.write(f"{attack} vs {defend} \n")
								
								continue
	
							if j<19 and map.occupied[i][j+1]=="d":
								number_fights+=1
								att_option=fight.option()
								def_option=fight.option()
								
								defender.append(i)
								defender.append(j+1)
								
								if att_option != def_option:
									attack = fight.fight()
									defend = fight.fight()
									
									result = fight.result(attack, defend, map.fields[i][j], map.fields[i][j+1])
									
									if att_option == "attack":
										if result == 1:
											for k in range(len(defenders)):
												if defenders[k].pos == [i, j+1]:
													defenders.pop(k)
													map.pop([i, j+1])
													defender_death += 1
													break
									if att_option == "defend":
										if result == -1:
											for k in range(len(attackers)):
												if attackers[k].pos == [i, j]:
													attackers.pop(k)
													map.pop([i, j])
													attacker_death += 1
													break
								
								if att_option == def_option and att_option == "attack":
									attack = fight.fight()
									defend = fight.fight()
									
									result = fight.result(attack, defend, map.fields[i][j], map.fields[i][j+1])
									
									rnd = random.randint(0, 1)
									
									if result == 0 and rnd == 1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
										
										for k in range(len(defenders)):
											if defenders[k].pos == [i, j+1]:
												defenders.pop(k)
												map.pop([i, j+1])
												defender_death += 1
												break
									
									if result == 1:
										for k in range(len(defenders)):
											if defenders[k].pos == [i, j+1]:
												defenders.pop(k)
												map.pop([i, j+1])
												defender_death += 1
												break
										
										if rnd == 1:
											for k in range(len(attackers)):
												if attackers[k].pos == [i, j]:
													attackers.pop(k)
													map.pop([i, j])
													attacker_death += 1
													break
									
									if result == -1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
										
										if rnd == 1:
											for k in range(len(defenders)):
												if defenders[k].pos == [i, j+1]:
													defenders.pop(k)
													map.pop([i, j+1])
													defender_death += 1
													break
							
							raport.write(
								f"Walka nr {number_fights} \n{map.fields[i][j][0]}[{i}; {j}] vs {map.fields[defender[0]][defender[1]][0]}[{defender[0]}; {defender[1]}] \n{att_option} vs {def_option} \n")
							
							if att_option == "attack" or def_option == "attack":
								raport.write(f"{attack} vs {defend} \n")
					
					continue

				if map.occupied[i][j] == "d":
					is_fight = False
					if is_fight == False:
						is_fight = True
						defender=[]
						if i < 19 and map.occupied[i + 1][j] == "a":
							number_fights += 1
							att_option = fight.option()
							def_option = fight.option()
							
							defender.append(i + 1)
							defender.append(j)
							
							if att_option != def_option:
								attack = fight.fight()
								defend = fight.fight()
								
								result = fight.result(attack, defend, map.fields[i][j], map.fields[i+1][j])
								
								if att_option == "attack":
									if result == 1:
										for k in range(len(defenders)):
											if defenders[k].pos == [i + 1, j]:
												defenders.pop(k)
												map.pop([i + 1, j])
												defender_death += 1
												break
								if att_option == "defend":
									if result == -1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
							
							if att_option == def_option and att_option == "attack":
								attack = fight.fight()
								defend = fight.fight()
								
								result = fight.result(attack, defend, map.fields[i][j], map.fields[i+1][j])
								
								rnd = random.randint(0, 1)
								
								if result == 0 and rnd == 1:
									for k in range(len(attackers)):
										if attackers[k].pos == [i, j]:
											attackers.pop(k)
											map.pop([i, j])
											attacker_death += 1
											break
									
									for k in range(len(defenders)):
										if defenders[k].pos == [i + 1, j]:
											defenders.pop(k)
											map.pop([i + 1, j])
											defender_death += 1
											break
								
								if result == 1:
									for k in range(len(defenders)):
										if defenders[k].pos == [i + 1, j]:
											defenders.pop(k)
											map.pop([i + 1, j])
											defender_death += 1
											break
									
									if rnd == 1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
								
								if result == -1:
									for k in range(len(attackers)):
										if attackers[k].pos == [i, j]:
											attackers.pop(k)
											map.pop([i, j])
											attacker_death += 1
											break
									
									if rnd == 1:
										for k in range(len(defenders)):
											if defenders[k].pos == [i + 1, j]:
												defenders.pop(k)
												map.pop([i + 1, j])
												defender_death += 1
												break
								
								raport.write(f"Walka nr {number_fights} \n{map.fields[i][j][0]}[{i}; {j}] vs {map.fields[defender[0]][defender[1]][0]}[{defender[0]}; {defender[1]}] \n{att_option} vs {def_option} \n")
								
								if att_option == "attack" or def_option == "attack":
									raport.write(f"{attack} vs {defend} \n")
								
								continue
							
							if j < 19 and map.occupied[i][j + 1] == "a":
								number_fights += 1
								att_option = fight.option()
								def_option = fight.option()
								
								defender.append(i + 1)
								defender.append(j)
								
								if att_option != def_option:
									attack = fight.fight()
									defend = fight.fight()
									
									result = fight.result(attack, defend, map.fields[i][j], map.fields[i][j+1])
									
									if att_option == "attack":
										if result == 1:
											for k in range(len(defenders)):
												if defenders[k].pos == [i, j + 1]:
													defenders.pop(k)
													map.pop([i, j + 1])
													defender_death += 1
													break
									if att_option == "defend":
										if result == -1:
											for k in range(len(attackers)):
												if attackers[k].pos == [i, j]:
													attackers.pop(k)
													map.pop([i, j])
													attacker_death += 1
													break
								
								if att_option == def_option and att_option == "attack":
									attack = fight.fight()
									defend = fight.fight()
									
									result = fight.result(attack, defend, map.fields[i][j], map.fields[i][j+1])
									
									rnd = random.randint(0, 1)
									
									if result == 0 and rnd == 1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
										
										for k in range(len(defenders)):
											if defenders[k].pos == [i, j + 1]:
												defenders.pop(k)
												map.pop([i, j + 1])
												defender_death += 1
												break
									
									if result == 1:
										for k in range(len(defenders)):
											if defenders[k].pos == [i, j + 1]:
												defenders.pop(k)
												map.pop([i, j + 1])
												defender_death += 1
												break
										
										if rnd == 1:
											for k in range(len(attackers)):
												if attackers[k].pos == [i, j]:
													attackers.pop(k)
													map.pop([i, j])
													attacker_death += 1
													break
									
									if result == -1:
										for k in range(len(attackers)):
											if attackers[k].pos == [i, j]:
												attackers.pop(k)
												map.pop([i, j])
												attacker_death += 1
												break
										
										if rnd == 1:
											for k in range(len(defenders)):
												if defenders[k].pos == [i, j + 1]:
													defenders.pop(k)
													map.pop([i, j+1])
													defender_death += 1
													break
							
							raport.write(
								f"Walka nr {number_fights} \n{map.fields[i][j][0]}[{i}; {j}] vs {map.fields[defender[0]][defender[1]][0]}[{defender[0]}; {defender[1]}] \n{att_option} vs {def_option} \n")
							
							if att_option == "attack" or def_option == "attack":
								raport.write(f"{attack} vs {defend} \n")
		
		attack_resources=0
		defend_resources=0
		
		for i in range(len(attackers)):
			pos=attackers[i].pos
			attackers[i].gather(map.fields[pos[0]][pos[1]][1])
			attack_resources+=attackers[i].resources
			
			attackers[i].move(map)
		
		for i in range(len(defenders)):
			pos=defenders[i].pos
			defenders[i].gather(map.fields[pos[0]][pos[1]][1])
			defend_resources+=defenders[i].resources
			
			defenders[i].move(map)
		
		if attack_resources==len(attackers):
			for a in range(len(attackers)):
				attackers[a].resources=0
		else:
			tmp=[]
			
			for i in range(len(attackers)):
				tmp.append(i)
			
			for i in range(len(tmp)-1):
				for j in range(i+1, len(tmp)):
					if attackers[tmp[j-1]].resources<attackers[tmp[j]].resources:
						temp=tmp[j]
						tmp[j]=tmp[j-1]
						tmp[j-1]=temp
					elif attackers[tmp[j-j]].hunger>attackers[tmp[j]].hunger:
						temp=tmp[j]
						tmp[j]=tmp[j-1]
						tmp[j-1]=temp
			
			difference=attack_resources%len(attackers)
			
			if attack_resources>len(attackers):
				for i in range(len(attackers)):
					if attackers[tmp[i]].resources>0:
						attackers[tmp[i]].resources-=1
			
			if attack_resources<len(attackers):
				for a in range(len(attackers)):
					attackers[a].resources=0
					
				for i in range(difference, len(attackers)):
					attackers[tmp[i]].hunger-=1
		
		if defend_resources == len(defenders):
			for d in range(len(defenders)):
				defenders[d].resources = 0
		else:
			tmp = []
			
			for i in range(len(defenders)):
				tmp.append(i)
			
			for i in range(len(tmp) - 1):
				for j in range(i, len(tmp)):
					if defenders[tmp[j-1]].resources < defenders[tmp[j]].resources:
						temp = tmp[j]
						tmp[j] = tmp[j - 1]
						tmp[j - 1] = temp
					elif defenders[tmp[j-1]].hunger > defenders[tmp[j]].hunger:
						temp = tmp[j]
						tmp[j] = tmp[j - 1]
						tmp[j - 1] = temp
			
			difference = defend_resources % len(defenders)
			
			if defend_resources > len(defenders):
				for d in range(len(defenders)):
					defenders[d].resources = 0
				
				for i in range(len(defenders)):
					if defenders[tmp[i]].resources>0:
						defenders[tmp[i]].resources -= 1
			
			if defend_resources < len(defenders):
				for i in range(difference, len(defenders)):
					defenders[tmp[i]].hunger-=1
		
		tmp=[]
		
		for i in range(len(attackers)):
			if attackers[i].hunger<=0:
				tmp.append(i)
		
		attacker_death+=len(tmp)
		
		hunger_att_deaths=len(tmp)
		
		for i in range(len(tmp)-1, -1, -1):
			pos=attackers[tmp[i]].pos
			map.pop(pos)
			
			attackers.pop(tmp[i])
		
		tmp = []
		
		for i in range(len(defenders)):
			if defenders[i].hunger <=0:
				tmp.append(i)
		
		defender_death += len(tmp)
		
		hunger_def_deaths=len(tmp)
		
		for i in range(len(tmp)-1, -1, -1):
			pos = defenders[tmp[i]].pos
			map.pop(pos)
			
			defenders.pop(tmp[i])
		
		raport.write("\n")
		for i in range(20):
			for j in range(20):
				raport.write(map.occupied[i][j])
			raport.write("\n")
		
		raport.write(f"\nZebrali: \n\tAtakujący: {attack_resources-att_resources+att} \n\tBroniący: {defend_resources-def_resources+deff} \nZ głodu umarło {hunger_att_deaths} atakujących oraz {hunger_def_deaths} broniących \n\nStraty: \n\tAtakujący: {attacker_death} \n\tObrońcy: {defender_death} \n")
	
	return len(attackers), len(defenders)