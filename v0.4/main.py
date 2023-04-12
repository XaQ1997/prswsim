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
	now=datetime.datetime.now()
	
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
	
	raport.write(f"Wersja: v0.4.0 \nData symulacji: {now.date()} \n\nAtakujący: {len(attackers)} \nObrońcy: {len(defenders)}\n")
	attackers, defenders=standard_variant(raport, attackers, defenders)
		
	raport.write(f"\n\n Rezultat bitwy: \n{attackers}-{defenders} \nCzas działania: {datetime.datetime.now()-now}")