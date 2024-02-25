'''
  Objective: Design a 'higher or lower' game
  To-do list:
    - Pick a random example
    - Ask the user to guess which is higher
    - Check if the user is correct
'''

import random

# Pick a random example from a dictionary and make sure it hasn't been used yet
def pick_random_example(examples, used_examples):
	example = random.choice(examples)
	while example in used_examples:
		example = random.choice(examples)
	return example

# Compare score between two examples
def compare_score(example1, example2):
	if example1['follower_count'] > example2['follower_count']:
		return True
	elif example1['follower_count'] < example2['follower_count']:
		return False

# Play the game
def play_game(data):
    