import random

while True:
	print("make your choice")
	choice = input()
	choice = choice.lower()


	print("my choice is", choice)

	choices = ["rock", "paper", "scissors"]

	computer_choice = random.choice(choices)

	print("Computer choice is", computer_choice)
	if choice in choices:
		if choice == computer_choice:
			print("it is a tie")
		if choice == "rock":
			if computer_choice == "paper":
				print("you lose, sorry :(####")
			else:
				print("You win!!!!! congrats:)$$$$")
		if choice == "paper":
			if computer_choice == "scissors":
				print("you lose, sorry :(####")
			else:
				print("You win!!!!! congrats:)$$$$")
		if choice == "scissors":
			if computer_choice == "rock":
				print("you lose, sorry :(####")
			else:
				print("You win!!!!! congrats:)$$$$")
	else:
		print("it is invalid choice, try again")

	print()

	 	

