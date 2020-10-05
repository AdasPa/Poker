import random
from os import system


def ranks(): return ["2","3","4","5","6","7","8","9","T","J","Q","K","A"]
def suits(): return ["♠","♣","♥","♦"]
def ids(): return [1,2,3,4]
def powers(): return [2,3,4,5,6,7,8,9,10,11,12,13,14]

class card:

	def __init__(self, rank, suit, power, id):
		self.rank = rank
		self.suit = suit
		self.power = power
		self.id = id

	def print_a_card(self):
		print(self.rank + self.suit, end = " ")

deck=[card(rank,suit,power,id)  for power, rank in zip(powers(),ranks()) for suit,id in zip(suits(),ids())]


def shuffle_cards():
	global order 
	order = []
	for i in range (0,52):
		order.append(i)
	random.shuffle(order)

def get_a_card():
	c=deck[order[0]]
	order.pop(0)
	return c

def print_flop(flop):
	print('\nThe Flop: ', end='')
	flop[0].print_a_card()
	flop[1].print_a_card()
	flop[2].print_a_card()
	print('\n')

def print_turn(turn):
	print('\nThe Turn: ', end='')
	turn.print_a_card()
	print('\n')

def print_river(river):
	print('\nThe River: ', end='')
	river.print_a_card()
	print('\n')

class player:

	def __init__ (self, money=1000, cards=[card, card]):
		self.money = money
		self.cards = cards

	def new_hand(self, card1, card2):
		self.cards = [card1, card2]
			
	def print_cards(self):
		print('Your hand: ', end='')
		for i in self.cards:
			i.print_a_card()
		print('\n')

	def blind(self, amount):
		self.money-=amount
		return amount

	def p_raise(self):
		amount = int(input("You have " + str (self.money)+"$. " + "How much do you want to raise? " + "\n"))
		if int(amount)<self.money:
			self.money -= amount
			return amount
		else: #all in - special func??
			amount=self.money
			self.money=0
			return amount

	def p_fold(self):
		return 'fold'

	def p_check(self, amount):  # all in problem
		self.money -= amount
		return int(amount)

	def p_bet(self, difference=0):
		is_correct=False
		while(is_correct==False):
			b=input("You have " + str(self.money) + "$. If you want to stay in the game, you have to bet at least " + str(difference) + "$. If you want to fold, press F, if you want to check, press C, if you want to raise, press R.\n")
			if b == 'F' or b == 'f':
				decision = player.p_fold(self)
				return decision
			elif b == 'C' or b == 'c':
				decision = player.p_check(self, difference)
				return decision
			elif b == 'R' or b == 'r':
				decision = player.p_raise(self)
				return decision
			else:
				print("Your input is incorrect.\n")
			

	def p_last_check(self, difference=0):
		is_correct=False
		while(is_correct==False):
			b=input("You have " + str(self.money) + "$. If you want to stay in the game, you have to bet " + str(difference) + "$. If you want to fold, press F, if you want to check, press C.\n")
			if b == 'F':
				decision = player.p_fold(self)
				return decision
			elif b == 'C':
				decision = player.p_check(self)
				return decision
			else:
				print("Your input is incorrect.\n")

class computer_player (player):

	def __init__ (self, money=1000, cards=[card, card]):
		super().__init__(money=1000, cards=[card, card])

	def c_decision(self, difference = 0):
		decision = -difference
		return decision
	###making a decision first
	def c_preflop(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b

	def c_flop(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b

	def c_turn(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b

	def c_river(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b
	### answer for players decision
	def c_preflop_ans(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b

	def c_flop_ans(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b

	def c_turn_ans(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b

	def c_river_ans(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b
	###
	def c_last_check(self, difference = 0):
		b = self.c_decision(difference = difference)
		return b


def new_deal(player_1=player, computer_player_1 = computer_player, pot=0, blind=10, player_pot=0, computer_player_pot=0):
	#
	# BLINDS
	#

	if counter == 0: #both BB
		pot += player_1.blind(blind)
		player_pot += player_1.blind(blind)
		pot += computer_player_1.blind(blind)
		computer_player_pot += computer_player_1.blind(blind)
	elif counter % 2 == 0: #computer BB
		pot += player_1.blind(blind/2)
		player_pot += player_1.blind(blind/2)
		pot += computer_player_1.blind(blind)
		computer_player_pot += computer_player_1.blind(blind)
	else: #player BB
		pot += player_1.blind(blind)
		player_pot += player_1.blind(blind)
		pot += computer_player_1.blind(blind/2)
		computer_player_pot += computer_player_1.blind(blind/2)

	#
	# CARDS
	#

	shuffle_cards()
	player_1.new_hand(get_a_card(), get_a_card())
	computer_player_1.new_hand(get_a_card(), get_a_card())
	player_1.print_cards()

	#
	# PRE FLOP
	#

	difference = computer_player_pot - player_pot
	if counter % 2 == 0: #computer BB or both BB

		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		answer = computer_player_1.c_preflop_ans(difference = difference)
		if  answer == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(answer == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += answer
			difference += answer

		if difference != 0:
			last_check = player_1.p_last_check(difference = difference)
			if last_check == 'fold':
				computer_player_1.money += pot
				return 'computer', pot
			else:
			   pot += int(bet)
			   difference=0
	########
	else: #player BB
		bet = computer_player_1.c_preflop(difference = difference)
		if bet == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(bet == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += int(bet)
			difference += int(bet)
		bet = player_1.p_bet(difference = difference)

		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		if difference != 0:
			last_check = computer_player_1.c_last_check(difference = difference)
			if last_check == 'fold':
				print('Computer folds.')
				player_1.money += pot
				return 'player', pot
			else:
			   pot += int(last_check)
			   difference = 0
			   print('Computer checks.')

	#
	# FLOP
	#
	
	flop = get_a_card(), get_a_card(), get_a_card()
	table = []
	for i in flop:
		table.append(i)
	print_flop(flop)

	if counter % 2 == 0: #computer BB or both BB

		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		answer = computer_player_1.c_flop_ans(difference = difference)
		if  answer == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(answer == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += answer
			difference += answer

		if difference != 0:
			last_check=player_1.p_last_check(difference = difference)
			if last_check == 'fold':
				computer_player_1.money += pot
				return 'computer', pot
			else:
			   pot += int(bet)
			   difference=0
	########
	else: #player BB
		bet = computer_player_1.c_flop(difference = difference)
		if bet == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(bet == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += int(bet)
			difference += int(bet)

		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		if difference != 0:
			last_check = computer_player_1.c_last_check(difference = difference)
			if last_check == 'fold':
				print('Computer folds.')
				player_1.money += pot
				return 'player', pot
			else:
			   pot += int(last_check)
			   difference = 0
			   print('Computer checks.')

	#
	# TURN
	#

	turn = get_a_card()
	table.append(turn)
	print_turn(turn)

	if counter % 2 == 0: #computer BB or both BB
		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		answer = computer_player_1.c_turn_ans(difference = difference)
		if  answer == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(answer == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += answer
			difference += answer

		if difference != 0:
			last_check=player_1.p_last_check(difference = difference)
			if last_check == 'fold':
				computer_player_1.money += pot
				return 'computer', pot
			else:
			   pot += int(bet)
			   difference=0
	########
	else: #player BB
		bet = computer_player_1.c_turn(difference = difference)
		if bet == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(bet == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += int(bet)
			difference += int(bet)

		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		if difference != 0:
			last_check = computer_player_1.c_last_check(difference = difference)
			if last_check == 'fold':
				print('Computer folds.')
				player_1.money += pot
				return 'player', pot
			else:
			   pot += int(last_check)
			   difference = 0
			   print('Computer checks.')

	#
	# RIVER
	#

	river = get_a_card()
	table.append(river)
	print_river(river)

	if counter % 2 == 0: #computer BB or both BB
		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:
			pot += int(bet)
			difference -= int(bet)

		answer = computer_player_1.c_river_ans(difference = difference)
		if  answer == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(answer == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += answer
			difference += answer

		if difference != 0:
			last_check=player_1.p_last_check(difference = difference)
			if last_check == 'fold':
				computer_player_1.money += pot
				return 'computer', pot
			else:
			   pot += int(bet)
			   difference=0
	########
	else: #player BB
		bet = computer_player_1.c_river(difference = difference)
		if bet == 'fold':
			print('Computer folds.')
			player_1.money += pot
			return 'player', pot
		else:
			if(bet == abs(difference)):
				print('Computer checks.')
			else:
				print('Computer raises ' + str(abs(difference)) + '$.')	
			pot += int(bet)
			difference += int(bet)

		bet = player_1.p_bet(difference = difference)
		if bet == 'fold':
			computer_player_1.money += pot
			return 'computer', pot
		else:

			pot += int(bet)
			difference -= int(bet)

		if difference != 0:
			last_check = computer_player_1.c_last_check(difference = difference)
			if last_check == 'fold':
				print('Computer folds.')
				player_1.money += pot
				return 'player', pot
			else:
			   pot += int(last_check)
			   difference = 0
			   print('Computer checks.')
	#
	# SHOWDOWN
	#

	return 'draw', pot



		#increase counter
player_1 = player()
computer_player_1 = computer_player()
counter = 0
winner, pot = new_deal(player_1, computer_player_1)
print(winner, str(pot))

#if(bet == abs(difference)):
#	print('Computer checks.')
#else:
#	print('Computer raises ' + str(abs(difference)) + '$.')	