import random
print('The Cat of the Day is: ')
with open('list.txt', 'r') as f:
	content = [line.strip() for line in f.readlines()] 
	print(random.choice(content))
