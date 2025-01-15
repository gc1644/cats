with open('list.txt', 'r') as f:
	content = f.read()
with open('list.txt', 'r') as f:
	text = len(f.readlines())
print('The book already contain ', text, ' names: ' + '\n' + content)
Cats = []
while True:
	print('Enter the name of your cat (or press enter on empty to stop)')
	name = input()
	if name == '':
		print('Done!')
		break
	Cats = Cats + [name]
print('names added:')
for name in Cats:
	print(' ' + name)

with open('list.txt', 'a') as f:
	for items in Cats:
	    f.write(items + '\n')
