from string import ascii_lowercase
import re

regexp = '|'.join([c + c.upper() for c in ascii_lowercase] + [c.upper() + c for c in ascii_lowercase])

def get_input():
	return open("day5.txt").readlines()[0]

	
def react_polymer(p):
	n = 1
	while(n > 0):
		p, n = re.subn(regexp, '', p)
	return p

	
p = get_input()
print(len(react_polymer(p)))

p = get_input()
units_regexes = [c + '|' + c.upper() for c in ascii_lowercase]
print(min([len(react_polymer(re.sub(regex, '', p))) for regex in units_regexes]))

	