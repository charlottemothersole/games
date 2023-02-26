#A game of rock, paper, scissors with an ongoing scoreboard and repeating indefinitely

import random

choices = ('rock','paper','scissors')
player_score = int(0)
computer_score = int(0)
current_winner = 'a draw'
repeat = True
first_game = True

name = input("Welcome! What's your name?")
print(f'Hello {name}!')

def play_game(your_choice, my_choice) :
    global player_score
    global computer_score
    print(f'You chose {your_choice}. Nice choice!\nI chose {my_choice}.')
    if your_choice == 'rock' and my_choice == 'scissors' :
        print(f'Rock blunts scissors. {name} wins!')
        player_score += 1
    if your_choice == 'rock' and my_choice == 'paper' :
        print('Paper wraps rock. I win!')
        computer_score += 1
    if your_choice == 'scissors' and my_choice == 'rock' :
        print('Rock blunts scissors. I win!')
        computer_score += 1
    if your_choice == 'scissors' and my_choice == 'paper' :
        print(f'Scissors cut paper. {name} wins!')
        player_score += 1
    if your_choice == 'paper' and my_choice == 'rock' :
        print(f'Paper wraps rock. {name} wins!')
        player_score += 1
    if your_choice == 'paper' and my_choice == 'scissors' :
        print(f'Scissors cut paper. I win!')
        computer_score += 1
    elif your_choice == my_choice :
        print(f"You chose {your_choice}, and I chose {my_choice}. It's a draw!")
    
    if first_game == False :
        calculate_score()

def make_choice() :
    print('--------------------------------------------')
    player_choice = input(str(f'Please choose one: {choices} '))
    computer_choice = random.choice(choices)

    while not player_choice in choices :
        print(f"Hey, no cheating! You chose '{player_choice}' which isn't a valid choice.")
        player_choice = input(str(f'Please make another choice from {choices}'))
        print(player_choice)    
    
    play_game(player_choice, computer_choice)
    

if first_game == True :
    make_choice()

def calculate_score() :
    print(f"The score is:\n{name}: {player_score}\nMe: {computer_score}")

    if player_score > computer_score : 
        current_winner = name 
    elif computer_score > player_score : 
        current_winner = 'me' 
    elif player_score == computer_score : 
        current_winner = 'a tie'
    
    global first_game
    first_game = False

    print(f"The current winner is {current_winner}! Shall we play again?")
    make_choice()

if first_game == True :
    calculate_score()