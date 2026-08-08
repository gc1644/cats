#!/usr/bin/env python3

with open('list.txt', 'r') as f:
    cats = f.readlines()

print('The book already contains', len(cats), 'names:\n')

for cat in cats:
    print(cat, end='')

cats = []

while True:
    print('Enter the name of your cat (or press enter on empty to stop)')
    name = input()

    if name == '':
        print('Done!')
        break

    cats.append(name)

print('names added:')

for cat in cats:
    print(' ' + cat)

with open('list.txt', 'a') as f:
    for cat in cats:
        f.write(cat + '\n')
