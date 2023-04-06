import datetime
import random

from raport import *
from unit import *
from variants import *

if __name__=="__main__":
	with open("count.txt") as count:
		text=count.read()
	
	with open("count.txt", "w") as count:
		count.write(text+"#")
	
	path=f"raporty\{len(text)}.txt"
	
	raport=Raport(path)
	
	attackers=random.randint(10, 100)
	defenders=random.randint(10, 100)
	
	count=attackers
	attackers=[]
	
	for i in range(count):
		attacker=Unit("attacker")
		attackers.append(attacker)
	
	count=defenders
	defenders=[]
	
	for i in range(count):
		defender=Unit("defender")
		defenders.append(defender)
	
	raport.write(f"Wersja: v0.3.0 \nData symulacji: {datetime.datetime.now().date()} \n\nAtakujący: {len(attackers)} \nObrońcy: {len(defenders)}\n")
	attackers, defenders=standard_variant(raport, attackers, defenders)
		
	raport.write(f"\n\n Rezultat bitwy: \n{attackers}-{defenders}")