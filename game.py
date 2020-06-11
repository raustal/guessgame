import random  # pygame, sys


# TODO:  Add pygame usage to the game so that the player has a windows come up on their screen.
# size = width, height = 640, 480

# pygame.init()
# pygame.display.set_mode(size)

counter = 0
print('Welcome to Guess Game!')
player = input('Enter your name to get started: ')  # Getting the player name.
print(f'Hi, {player}, now enter the highest number that you want to guess between.\n'
      f'The higher the number, the harder the Guess Game will be!')
game_difficulty = input('Difficulty: ')
# TODO: Complete the logic for the number of attempts the player will have.
# print('Now enter the number of tries you want to have.')
# attempts = input()
if not game_difficulty.isdecimal():
    print('You did not enter a number, try again.')

theNumber = random.randint(0, int(game_difficulty))
# print(f'Debug: {theNumber} is the number the computer picked')  # This is checking to see if the number random
print(f'Guess the number that I am thinking between 0 and {game_difficulty} to win.')
while counter < 5:
    playerGuess = int(input('Guess: '))
    tries = 4 - counter

    if playerGuess > theNumber:
        print('Your guess is too high, try again!')
        counter = counter + 1
        print(f'You have {tries} left.')
    elif playerGuess < theNumber:
        print('Your guess is too low, try again')
        counter = counter + 1
        print(f'You have {tries} left.')
    else:
        print(f'You won {player}!')
        break
