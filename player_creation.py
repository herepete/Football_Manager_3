#!/usr/bin/python3

squad_of_players_list=[]

class print_nicer_output():

	def default_squad(self,squad_to_print):
		for k in squad_of_players_list:
			try:
				temp_position=' '.join(k[0])
				print('{:<20s}{:<10s}{:>10s}{:>10s}{:>10s}'.format(temp_position,k[1],k[2],str(k[3]),str(k[4])))
				pass
			except:
				import pdb
				pdb.set_trace()

	def test_print(self):
		print('{:=<20}'.format('hello'))
		print('{:_^20}'.format('hello'))
		print('{:=>20}'.format('hello'))



class create_player():

	import random
	global squad_of_players_list

	def player_name(self):
		first_name_list=["Peter","Bob","James","Tony","Aj","Bo","Nathan","Gibby","Tim","Anchor"]
		last_name_list=["White","Mander","Bishop","Garrett","Winston","Mayfield","Shearer","Rooney","Tucker","Racker"]
		random_choice_first_name=self.random.choice(first_name_list)
		random_choice_last_name=self.random.choice(last_name_list)
		self.first_name=random_choice_first_name
		self.last_name=random_choice_last_name
		

	def player_skill(self):
		random_skill=self.random.randint(70,96)
		self.random_skill=random_skill

	def player_age(self):
		random_age=self.random.randint(18,36)
		self.random_age=random_age


	def create_position(self):
		defender_choice_position=["LB","RB","CB"]
		midfield_choice_position=["LM","RM","CM","Def M","Ata M"]
		attacker_choice_position=["ST","W"]
		player_selected_position=[]
		if self.play_position=="GK":
			self.final_player_position="GK"
		elif self.play_position=="DEF":
			random_player_poistions=self.random.randint(1,2)
			for i in range(random_player_poistions):
				random_position_selected=self.random.choice(defender_choice_position)
				player_selected_position.append(random_position_selected)
				defender_choice_position.remove(random_position_selected)
			self.final_player_position=player_selected_position
		elif self.play_position=="MID":
			random_player_poistions=self.random.randint(1,2)
			for i in range(random_player_poistions):
				random_position_selected=self.random.choice(midfield_choice_position)
				player_selected_position.append(random_position_selected)
				midfield_choice_position.remove(random_position_selected)
			self.final_player_position=player_selected_position

		else:
			#we are presuming a Sticker
			random_player_poistions=self.random.randint(1,2)
			for i in range(random_player_poistions):
				random_position_selected=self.random.choice(attacker_choice_position)
				player_selected_position.append(random_position_selected)
				attacker_choice_position.remove(random_position_selected)
			self.final_player_position=player_selected_position
	


	def player_creation(self,play_position):
		global squad_of_players
		self.player_name()
		self.player_skill()
		self.player_age()
		self.play_position=play_position
		self.create_position()
		try:
			temp_build=[self.final_player_position,self.first_name,self.last_name,self.random_age,self.random_skill]
			squad_of_players_list.append(temp_build)
		except:
			import pdb
			pdb.set_trace
			
		#print(self.final_player_position,end=" ")
		#print(self.first_name,end=" ")
		#print(self.last_name,end=" ")
		#print(self.random_age,end=" ")
		#print(self.random_skill,end=" ")
		#print ()
		
		
		




create_default_list=create_player()

default_squad_GK=3
default_squad_DEF=8
default_squad_MID=7
default_squad_ATA=4

for j in range(1,default_squad_GK):
	create_default_list.player_creation(play_position="GK")
for k in range(1,default_squad_DEF):
	create_default_list.player_creation(play_position="DEF")
for k in range(1,default_squad_MID):
	create_default_list.player_creation(play_position="MID")
for k in range(1,default_squad_ATA):
	create_default_list.player_creation(play_position="ATA")

nicer_output=print_nicer_output()
nicer_output.default_squad(squad_to_print=squad_of_players_list)
#nicer_output.test_print()
#for k in squad_of_players_list:
#	print(k)

#create 23 players, 3GK,8DEF (LB/DB/RB), 7 MID(LM/DM/AM/CM/RM) , 5 ATA(ST,Winger)
