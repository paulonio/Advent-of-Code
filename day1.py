from itertools import cycle, accumulate

def input(): 
	return map(int, open("day1.txt"))
	
print(sum(input()))

frequencies = set()

for frequency in accumulate(cycle(input())):
	if frequency in frequencies or frequencies.add(frequency):
		print(frequency)
		break
