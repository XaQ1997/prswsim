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
			row=random.randint(10, 19)
			column=random.randint(0, 19)
		
		map.fields[row][column]="a"
		attackers[i].pos=[row, column]
	
	for i in range(len(defenders)):
		row = -1
		column = -1
		
		while (row < 0 or column < 0 or map.fields[row][column] != "."):
			row = random.randint(0, 9)
			column = random.randint(0, 19)
		
		map.fields[row][column]="d"
		defenders[i].pos = [row, column]
	
	raport.write("\n")
	
	for i in range(20):
		for j in range(20):
			raport.write(map.fields[i][j])
		raport.write("\n")
	
	for index in range(1, 251):
		if len(defenders)==0 or len(attackers)==0:
			break
		
		raport.write(f"\nTura {index} \n")
		attacker_death=0
		defender_death=0
		number_fights=0
		
		for i in range(20):
			for j in range(20):
				if map.fields[i][j]=="a":
					is_fight=False
					if is_fight==False:
						is_fight=True
						defender=[]
						if i<19 and map.fields[i+1][j]=="d":
							number_fights+=1
							att_option=fight.option()
							def_option=fight.option()
							
							defender.append(i+1)
							defender.append(j)
							
							if att_option!=def_option:
								attack = fight.fight()
								defend = fight.fight()
								
								result = fight.result(attack, defend)
								
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
								
								raport.write(
									f"Walka nr {number_fights} \nAtakujący na pozycji [{i}; {j}] vs Broniący na pozycji [{defender[0]}; {defender[1]}] \n             {att_option}              vs              {def_option} \n")
								
								if att_option == "attack" or def_option == "attack":
									raport.write(f"             {attack}              vs              {defend} \n")
								
								continue
	
							if j<19 and map.fields[i][j+1]=="d":
								number_fights+=1
								att_option=fight.option()
								def_option=fight.option()
								
								defender.append(i)
								defender.append(j+1)
								
								if att_option != def_option:
									attack = fight.fight()
									defend = fight.fight()
									
									result = fight.result(attack, defend)
									
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
									
									result = fight.result(attack, defend)
									
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
					
							raport.write(f"Walka nr {number_fights} \nAtakujący na pozycji [{i}; {j}] vs Broniący na pozycji [{defender[0]}; {defender[1]}] \n             {att_option}              vs              {def_option} \n")
							
							if att_option == "attack" or def_option  == "attack":
								raport.write(f"             {attack}              vs              {defend} \n")
					
					continue

				if map.fields[i][j] == "d":
					is_fight = False
					if is_fight == False:
						is_fight = True
						defender=[]
						if i < 19 and map.fields[i + 1][j] == "a":
							number_fights += 1
							att_option = fight.option()
							def_option = fight.option()
							
							defender.append(i + 1)
							defender.append(j)
							
							if att_option != def_option:
								attack = fight.fight()
								defend = fight.fight()
								
								result = fight.result(attack, defend)
								
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
								
								result = fight.result(attack, defend)
								
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
												
								raport.write(f"Walka nr {number_fights} \nAtakujący na pozycji [{i}; {j}] vs Broniący na pozycji [{defender[0]}; {defender[1]}] \n             {att_option}              vs              {def_option} \n")
								
								if att_option == "attack" or def_option == "attack":
									raport.write(f"             {attack}              vs              {defend} \n")
								
								continue
							
							if j < 19 and map.fields[i][j + 1] == "a":
								number_fights += 1
								att_option = fight.option()
								def_option = fight.option()
								
								defender.append(i + 1)
								defender.append(j)
								
								if att_option != def_option:
									attack = fight.fight()
									defend = fight.fight()
									
									result = fight.result(attack, defend)
									
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
									
									result = fight.result(attack, defend)
									
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
													
							raport.write(f"Walka nr {number_fights} \nAtakujący na pozycji [{i}; {j}] vs Broniący na pozycji [{defender[0]}; {defender[1]}] \n             {att_option}              vs              {def_option} \n")
							
							if att_option == "attack" or def_option  == "attack":
								raport.write(f"             {attack}              vs              {defend} \n")
		
		for i in range(len(attackers)):
			attackers[i].move(map)
		
		for i in range(len(defenders)):
			defenders[i].move(map)
		
		raport.write("\n")
		for i in range(20):
			for j in range(20):
				raport.write(map.fields[i][j])
			raport.write("\n")
		
		raport.write(f"\nStraty: \n\tAtakujący: {attacker_death} \n\tObrońcy: {defender_death} \n")
	
	return len(attackers), len(defenders)